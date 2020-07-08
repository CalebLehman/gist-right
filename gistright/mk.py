import sys
from gistright import GistFile, load_from_global_gist, dump_to_global_gist

def add_parser(subparsers):
    parser = subparsers.add_parser(
        'mk',
        description='Add contents of stdin as new file to current global gist',
        help='Add contents of stdin as new file to current global gist',
    )
    parser.add_argument(
        'filename',
        type=str,
        help='The name of the file'
    )

def run(args):
    gist_obj = load_from_global_gist()
    gist_obj.files.append(GistFile(args.filename, sys.stdin.read()))
    dump_to_global_gist(gist_obj)
    print(f'Added')
    print(f'  {args.filename}')
    print(f'to current global gist')
