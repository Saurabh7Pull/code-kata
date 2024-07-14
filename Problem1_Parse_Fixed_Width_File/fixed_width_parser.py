# fixed_width_parser.py

def parse_fixed_width_file(spec, input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(output_file, 'w', encoding='utf-8') as csv_file:
        for line in lines:
            start = 0
            parsed_fields = []
            for width in spec:
                field = line[start:start + width].strip()
                parsed_fields.append(field)
                start += width
            csv_file.write(','.join(parsed_fields) + '\n')

# Example usage
spec = [10, 15, 20]
input_file = 'fixed_width.txt'
output_file = 'output.csv'

parse_fixed_width_file(spec, input_file, output_file)
