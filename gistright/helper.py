import os, getpass, requests, json

class BadTokenError(Exception):
    '''Raised when GitHub PAT fails to authenticate
    Attributes:
        message -- error message
    '''
    def __init__(self):
        self.message = f'Bad GitHub token (check {get_token_path()})'
        super().__init__(self.message)

class BadIdError(Exception):
    '''Raised when invalid gist id is used
    Attributes:
        gist_id -- the invalid id
        message -- error message
    '''
    def __init__(self, gist_id):
        self.gist_id = gist_id
        self.message = f'No gist with id \'{gist_id}\''
        super().__init__(self.message)

class GistObj():
    '''Wraps a complete gist'''
    def __init__(self, public=False, description=''):
        self.public = public
        self.description = description
        self.files = []

    def dumps_json(self):
        data = {
            'description': self.description,
            'public': self.public,
            'files': {f.name: {'content': f.content} for f in self.files},
        }
        return json.dumps(data)

    def loads_json(self, file_obj):
        data = json.loads(file_obj)
        self.description = data['description']
        self.public = data['public']
        self.files = [GistFile(f, data['files'][f]['content']) for f in data['files']]

class GistFile():
    '''Wraps the name and content of a gist file'''
    def __init__(self, name, content):
        self.name = name
        self.content = content

def get_global_gist_path():
    return os.path.join(os.environ['HOME'], '.config', 'gistright', 'gist.json')

def load_from_global_gist():
    gist_path = get_global_gist_path()
    gist_obj = GistObj()
    try:
        with open(gist_path) as f:
            gist_obj.loads_json(f.read())
    except FileNotFoundError:
        pass
    return gist_obj

def dump_to_global_gist(gist_obj):
    gist_path = get_global_gist_path()
    try:
        with open(gist_path, 'w') as f:
            f.write(gist_obj.dumps_json())
    except FileNotFoundError:
        os.makedirs(os.path.dirname(gist_path), exist_ok=True)
        fd = os.open(gist_path, os.O_CREAT | os.O_WRONLY, mode=0o600)
        with open(fd, 'w') as f:
            f.write(gist_obj.dumps_json())

def get_token_path():
    return os.path.join(os.environ['HOME'], '.config', 'gistright', 'gist_token')

def get_auth_headers():
    token_path = get_token_path()
    try:
        with open(token_path) as f:
            token = f.read().strip()
    except FileNotFoundError:
        token = getpass.getpass(prompt='Gist (GitHub) Token: ')
        os.makedirs(os.path.dirname(token_path), exist_ok=True)
        fd = os.open(token_path, os.O_CREAT | os.O_WRONLY, mode=0o600)
        with open(fd, 'w') as f:
            f.write(token)
        print(f'Token stored at {token_path}')
    return { 'Authorization': 'token ' + token }

def get_gists():
    url = 'https://api.github.com/gists'
    headers = get_auth_headers()
    try:
        return requests.get(url=url, headers=headers).json()
    except ValueError:
        raise BadTokenError() from None

def get_gist(gist_id):
    url = 'https://api.github.com/gists/' + gist_id
    headers = get_auth_headers()
    try:
        data = requests.get(url=url, headers=headers).json()
    except ValueError:
        raise BadTokenError() from None
    if data.get('message', '') == 'Not Found':
        raise BadIdError(gist_id)
    return data

def create_gist(gist_obj):
    url = 'https://api.github.com/gists'
    headers = get_auth_headers()
    try:
        req = requests.post(url=url, data=gist_obj.dumps_json(), headers=headers)
    except ValueError:
        raise BadTokenError() from None
    return req.json()['html_url']

