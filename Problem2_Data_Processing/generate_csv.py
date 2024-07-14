# generate_csv.py

import csv
import random
from faker import Faker

def generate_csv(file_path, num_records):
    fake = Faker()
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'address', 'date_of_birth']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for _ in range(num_records):
            writer.writerow({
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'address': fake.address(),
                'date_of_birth': fake.date_of_birth().isoformat()
            })

# Example usage
generate_csv('sample.csv', 1000000)  # Adjust the number of records as needed
