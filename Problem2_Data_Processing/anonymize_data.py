# anonymize_data.py

import csv
import hashlib

def anonymize_value(value):
    return hashlib.sha256(value.encode()).hexdigest()

def anonymize_csv(input_file, output_file):
    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                row['first_name'] = anonymize_value(row['first_name'])
                row['last_name'] = anonymize_value(row['last_name'])
                row['address'] = anonymize_value(row['address'])
                writer.writerow(row)

# Example usage
anonymize_csv('sample.csv', 'anonymized_sample.csv')
