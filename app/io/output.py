def output_to_console(text):
    """
    Function to output text to the console.

    Args:
        text (str): The text to be printed.
    """
    print(text)


def write_to_file_builtin(filename, content):
    """
    Function to write content to a file using built-in funcs.

    Args:
        filename (str): The name of the file where the content will be written.
        content (str): The content to be written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
