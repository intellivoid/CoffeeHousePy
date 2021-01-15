import sys

from coffeehouse_ping import Server


def _real_main(argv=None):
    """
    The main command-line processor

    :param argv:
    :return:
    """
    if argv[1] == '--help':
        _help_menu(argv)
    if argv[1] == '--start-server':
        _start_server(argv)


def _start_server(argv=None):
    """
    Starts the server

    :param argv:
    :return:
    """
    server = Server()
    server.start()


def _help_menu(argv=None):
    """
    Displays the help menu and commandline usage

    :param argv:
    :return:
    """
    print(
        "CoffeeHouse Ping CLI\n\n"
        "   --help\n"
        "   --start-server\n"
    )
    sys.exit()



if __name__ == '__main__':
    try:
        _real_main(sys.argv)
    except KeyboardInterrupt:
        print('\nInterrupted by user')
