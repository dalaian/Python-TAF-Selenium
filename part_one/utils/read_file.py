

def read_file(file_path):
    """ Read the content of a file from a given path
    :param file_path: str, path of file to read
    :return: str, the content that the file has on it
    """
    contents = None
    # opens the file and by default it sends 'r' as mode, so, it ensures the file will be used only for reading,
    # and not writing, since it's not necessary
    file_to_read = open(file_path)
    if file_to_read.mode == 'r':
        # saves the text of the file into a variable
        contents = file_to_read.read()

    # close the file
    file_to_read.close()
    return contents


def convert_file_to_list(file_path, separator="\n"):
    """ Convert the content of a file, from a given path, to a list
    :param file_path: str, path of file to read
    :param separator: str, character to separate the text that is in the file; by default \n
    :return: str[]: the content of the file as a list
    """
    # gets the content of the file
    contents = read_file(file_path)
    # splits the content by a separator
    return contents.split(separator)
