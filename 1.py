
def format(input_file, output_file, line_length):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    format_lines = []

    for line in lines:
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

    with open(output_file, 'w') as file:
        file.write("\n".join(format_lines))

input_file = input("имя входного файла ")
output_file = input("имя результирующего файла ")
line_length = int(input("длина строки "))

format(input_file, output_file, line_length)
