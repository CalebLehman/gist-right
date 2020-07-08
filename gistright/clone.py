import os, subprocess
from gistright import get_gist

def add_parser(subparsers):
    parser = subparsers.add_parser(
        'clone',
        description='Clone a gist from an id',
        help='Clone a gist from an id',
    )
    parser.add_argument(
        'id',
        type=str,
        help='Gist id',
    )
    parser.add_argument(
        'path',
        type=str,
        help='Path to subdirectory',
    )

def run(args):
    if os.path.exists(args.path):
        print(f'Cannot clone; {args.path} already exists')
    else:
        subprocess.check_call(['git', 'clone', get_gist(args.id)['git_pull_url'], args.path])
