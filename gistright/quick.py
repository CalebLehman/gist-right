import sys
from gistright import GistObj, GistFile, create_gist

def add_parser(subparsers):
    parser = subparsers.add_parser(
        'quick',
        description='Make and push a simple gist',
        help='''Make and push a simple gist consisting of a single file
Does not affect the current global gist
''',
    )
    parser.add_argument(
        'filename',
        type=str,
        help='The name of the file'
    )
    parser.add_argument(
        '-d',
        '--description',
        type=str,
        default='',
        help='The description of the gist'
    )
    parser.add_argument(
        '-p',
        '--public',
        action='store_true',
        dest='public',
        help='Set the gist as public',
    )

def run(args):
    gist_obj       = GistObj(description=args.description, public=args.public)
    gist_obj.files = [ GistFile(args.filename, sys.stdin.read()) ]
    gist_url = create_gist(gist_obj)
    print(f'Gist created at {gist_url}')
