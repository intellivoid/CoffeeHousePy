import os


def get_location():
    """
    Returns the location for the punkt data
    :return:
    """
    return os.path.join(os.path.dirname(__file__), 'data')
