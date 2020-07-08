import os
from gistright.helper import GistFile, load_from_global_gist, dump_to_global_gist

def add_parser(subparsers):
    parser = subparsers.add_parser(
        'add',
        description='Add files to current global gist',
        help='Add files to current global gist',
    )
    parser.add_argument(
        'filenames',
        type=str,
        nargs='+',
        help='Paths to the files',
    )

def run(args):
    # load files
    files = []
    names = []
    for filename in args.filenames:
        try:
            with open(filename, 'r') as f:
                name = os.path.basename(filename)
                names.append(name)
                files.append(GistFile(name, f.read()))
        except FileNotFoundError:
            print(f'File \'{filename}\' not found')
        except IsADirectoryError:
            print(f'\'{filename}\' is a directory, not a file')

    # store files in current global gist
    gist_obj = load_from_global_gist()
    gist_obj.files.extend(files)
    dump_to_global_gist(gist_obj)
    if len(names) > 0:
        print(f'Added')
        for filename in names:
            print(f'  {filename}')
        print('to current global gist')
