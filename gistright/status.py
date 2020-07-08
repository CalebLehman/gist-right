import textwrap
from gistright.helper import load_from_global_gist

def add_parser(subparsers):
    parser = subparsers.add_parser(
        'status',
        description='Display the files in the current global gist',
        help='Display the files in the current global gist',
    )

def run(args):
    gist_obj = load_from_global_gist()
    filenames = [gist_file.name for gist_file in gist_obj.files]
    print(textwrap.fill('  '.join(filenames), 80))
