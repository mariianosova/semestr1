import unittest

def read_data(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines

def write_data(file_name, data):
    with open(file_name, 'w') as file:
        file.write("\n".join(data))

def get_format(data, line_length):
    format_lines = []
    for line in data:
        words = line.strip().split()
        format_line = ""
        current_length = 0

        for word in words:
            word_length = len(word)
            if current_length + word_length <= line_length:
                format_line += word + " "
                current_length += word_length + 1
            else:
                format_lines.append(format_line.strip())
                format_line = word + " "
                current_length = word_length + 1

        format_lines.append(format_line.strip())

    return format_lines

def main():
    input_file = input("имя входного файла ")
    output_file = input("имя результирующего файла ")
    line_length = int(input("длина строки "))

    data = read_data(input_file)
    result = get_format(data, line_length)
    write_data(output_file, result)

class TestDataFormatting(unittest.TestCase):
    def test_get_format(self):
        data = ["Hello How", "Are you from?", "I'm from good", "Thanks"]
        line_length = 10

        expected_result = ["Hello How", "Are you", "from?", "I'm from", "good", "Thanks"]
        result = get_format(data, line_length)

        self.assertEqual(result, expected_result)

    def test_write_data(self):
        file_name = "output.txt"
        data = ["Hello How", "Are you", "from?", "I'm from", "good", "Thanks"]

        write_data(file_name, data)

        with open(file_name, 'r') as file:
            lines = file.readlines()

        result = [line.strip() for line in lines]

        self.assertEqual(result, data)

if __name__ == '__main__':
    unittest.main()
