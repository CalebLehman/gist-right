from gistright import GistObj, load_from_global_gist, dump_to_global_gist, create_gist

def add_parser(subparsers):
    parser = subparsers.add_parser(
        'push',
        description='Push the current global gist',
        help='Push the current global gist',
    )
    parser.add_argument(
        '-d',
        '--description',
        type=str,
        default='',
        help='The description of the gist',
    )
    parser.add_argument(
        '-p',
        '--public',
        action='store_true',
        dest='public',
        help='Set the gist as public',
    )

def run(args):
    # make/load gist object from arguments and current global gist
    gist_obj             = load_from_global_gist()
    gist_obj.description = args.description
    gist_obj.public      = args.public

    # create and push gist
    gist_url = create_gist(gist_obj)
    print(f'Gist created at {gist_url}')

    # clear current global gist
    gist_obj = GistObj()
    dump_to_global_gist(gist_obj)
