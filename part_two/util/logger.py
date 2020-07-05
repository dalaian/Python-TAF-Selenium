import logging

log_path = "UI/logs/"  # common path to keep the logs from the UI


def config_logger(name, browser_name=""):
    """ Config the logger
    :param name: str, name of the log file
    :param browser_name: str, by default ""
    :return: None
    """
    style = "%(asctime)s : %(levelname)s :: %(message)s"
    path = "{}{}_{}.log".format(log_path, name, browser_name)
    logging.basicConfig(filename=path, level=logging.INFO, filemode='w', format=style)


"""
 The common functions of the log are encapsulated in case the log changes, the maintenance will be easier
"""


def info(message):
    logging.info(message)


def warn(method, message):
    logging.warn(method.__name__ + " : " + message)


def error(message):
    logging.error(message)


def auto_log(method_class, method):
    """ Auto log a method, but the doc_string in the method is mandatory
    :param method_class: class, the class to get the name of it
    :param method: method, the method to get the name of it and the doc_string
    :return: None
    """
    # gets the doc_string of the method
    doc_string = method.__doc__.split("\n")[0]
    info(method_class.__class__.__name__ + ' : ' + method.__name__ + ' : ' + doc_string)
