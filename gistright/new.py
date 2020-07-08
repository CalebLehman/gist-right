from gistright.helper import GistObj, dump_to_global_gist

def add_parser(subparsers):
    parser = subparsers.add_parser(
        'new',
        description='Clear current global gist',
        help='Add files to current global gist',
    )
    parser.add_argument(
        '-f',
        '--force',
        action='store_true',
        dest='force',
        help='Clear current global gist without prompt',
    )

def run(args):
    if args.force:
        dump_to_global_gist(GistObj())
        print('Current global gist cleared')
        return

    choice = input('Clear current global gist (cannot be undone)? [y/n] ')
    while True:
        yes_choices = ['Y', 'y']
        no_choices  = ['N', 'n']
        if choice in yes_choices:
            dump_to_global_gist(GistObj())
            print('Current global gist cleared')
            return
        elif choice in no_choices:
            print('No change')
            return
        else:
            choice = input('Choose from (y/Y) or (n/N) ')

