from gistright.helper import load_from_global_gist, dump_to_global_gist

def add_parser(subparsers):
    parser = subparsers.add_parser(
        'rm',
        description='Remove files from current global gist',
        help='Remove files from current global gist',
    )
    parser.add_argument(
        'filenames',
        type=str,
        nargs='+',
        help='File names',
    )

def run(args):
    gist_obj = load_from_global_gist()
    gist_obj.files = [gist_file for gist_file in gist_obj.files if not gist_file.name in args.filenames]
    dump_to_global_gist(gist_obj)
