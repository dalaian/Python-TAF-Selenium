data_path = "UI/data/"  # common path where the data is saved and to be used by the UI


def read_file(path):
    """ Read a file from a given path
    :param path: str, path of the file
    :return: str, the content from the file
    """
    with open(path, 'r') as f:
        return f.read()


def read_data_file(file_path):
    """ Read a file and convert it into a json
    :param file_path: str, file of the path
    :return: json, the data of the file
    """
    # creates the file path
    path = data_path + file_path
    # reads the file
    content = read_file(path)
    # converts the content of the file in json
    return eval(content)
