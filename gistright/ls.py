from gistright import get_gists

def add_parser(subparsers):
    parser = subparsers.add_parser(
        'ls',
        description='List the user\'s gists',
        help='List the user\'s gists',
    )

def run(args):
    print(f'{"id":^32} | {"description":^53}')
    print(32*'-' + '-+-' + 53*'-')
    for gist in get_gists():
        id, description = gist['id'], gist['description']
        if len(description) > 50:
            print(f'{id:<32} | {description[:50]}...')
        else:
            print(f'{id:<32} | {description}')
