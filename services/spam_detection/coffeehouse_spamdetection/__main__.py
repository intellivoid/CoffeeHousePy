import sys

from coffeehouse_spamdetection import SpamDetection
from coffeehouse_spamdetection import Server


def _real_main(argv=None):
    """
    The main command-line processor

    :param argv:
    :return:
    """
    if argv[1] == '--help':
        _help_menu(argv)
    if argv[1] == '--test':
        _test_model(argv)
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
        "CoffeeHouse SpamDetection CLI\n\n"
        "   --help\n"
        "   --test\n"
        "   --start-servver  rrr\n"
    )
    sys.exit()


def _test_model(argv=None):
    """
    Tests the model's prediction by allowing user input and displaying the
    prediction output

    :param argv:
    :return:
    """
    print("Loading")
    spam_detection = SpamDetection()
    print("Ready\n")

    while True:
        input_text = input("> ")
        print(spam_detection.predict(input_text))


if __name__ == '__main__':
    try:
        _real_main(sys.argv)
    except KeyboardInterrupt:
        print('\nInterrupted by user')
