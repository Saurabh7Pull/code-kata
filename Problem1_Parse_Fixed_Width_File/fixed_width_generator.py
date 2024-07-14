# fixed_width_generator.py

def generate_fixed_width_file(spec, data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for row in data:
            fixed_width_row = ''.join(
                str(row[i]).ljust(spec[i])[:spec[i]] for i in range(len(spec))
            )
            file.write(fixed_width_row + '\n')

# Example usage
spec = [10, 15, 20]  # Length of each field
data = [
    ['Bill', 'Data Engineer', 'bill@example.com'],
    ['Bob', 'Data Scientist', 'bob@example.com']
]

generate_fixed_width_file(spec, data, 'fixed_width.txt')
