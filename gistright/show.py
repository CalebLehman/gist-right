import textwrap
from gistright import get_gist

def add_parser(subparsers):
    parser = subparsers.add_parser(
        'show',
        description='Show the details of gist',
        help='Show the details of gist',
    )
    parser.add_argument(
        'id',
        type=str,
        help='Gist id',
    )

def run(args):
    gist = get_gist(args.id)
    print('Description:')
    print('')
    if gist['description'] == '':
        print('[N/A]')
    else:
        print(textwrap.fill('  ' + gist['description'], 80))
    print('')
    print('Files:')
    print('')
    print(textwrap.fill('  '.join(gist['files'].keys()), 80))
