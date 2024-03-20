import pandas as pd


def input_from_console():
    """
    Function to input text from the console.

    Returns:
        str: The input text from the user.
    """
    text = input("Enter text: ")
    return text


def read_from_file_builtin(filename):
    """
    Function to read from a file using built-in funcs.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        str: The content of the file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def read_from_file_pandas(filename):
    """
    Function to read from file using the pandas library.

    Args:
        filename (str): The name of the file to be read. The file should be in CSV format.

    Returns:
        list: The content of the file.
    """
    data = pd.read_csv(filename, header=None)
    return data[0].tolist()
