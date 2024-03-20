from app.io.input import input_from_console, read_from_file_builtin, read_from_file_pandas
from app.io.output import output_to_console, write_to_file_builtin


def main():
    # Input from console
    console_text = input_from_console()
    output_to_console(console_text)
    write_to_file_builtin('data/console.txt', console_text)

    # Input from file
    file_text = read_from_file_builtin('data/example.txt')
    output_to_console(file_text)
    write_to_file_builtin('data/example_copy.txt', file_text)

    # Input from file using pandas
    csv_file = read_from_file_pandas('data/example.csv')
    output_to_console(str(csv_file))
    write_to_file_builtin('data/example_cvv.txt', str(csv_file))


if __name__ == "__main__":
    main()
