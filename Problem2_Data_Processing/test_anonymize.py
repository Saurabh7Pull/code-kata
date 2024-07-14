# test_anonymize.py

import unittest
from anonymize_data import anonymize_value, anonymize_csv

class TestAnonymizeData(unittest.TestCase):
    def setUp(self):
        self.input_file = 'test_sample.csv'
        self.output_file = 'test_anonymized_sample.csv'
        with open(self.input_file, 'w', encoding='utf-8') as f:
            f.write("first_name,last_name,address,date_of_birth\n")
            f.write("John,Doe,123 Main St,1980-01-01\n")
            f.write("Jane,Doe,456 Elm St,1990-02-02\n")

    def test_anonymize_value(self):
        original = 'John Doe'
        anonymized = anonymize_value(original)
        self.assertNotEqual(original, anonymized)
        self.assertEqual(len(anonymized), 64)  # Length of SHA-256 hash

    def test_anonymize_csv(self):
        anonymize_csv(self.input_file, self.output_file)
        
        with open(self.output_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        self.assertEqual(len(lines), 3)  # Header + 2 rows
        self.assertEqual(lines[0], "first_name,last_name,address,date_of_birth\n")

        # Check that the fields are anonymized
        fields = lines[1].strip().split(',')
        self.assertEqual(len(fields), 4)
        self.assertEqual(len(fields[0]), 64)  # first_name
        self.assertEqual(len(fields[1]), 64)  # last_name
        self.assertEqual(len(fields[2]), 64)  # address

    def test_empty_csv(self):
        empty_file = 'empty_test_sample.csv'
        with open(empty_file, 'w', encoding='utf-8') as f:
            f.write("first_name,last_name,address,date_of_birth\n")
        
        anonymize_csv(empty_file, self.output_file)
        
        with open(self.output_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        self.assertEqual(len(lines), 1)  # Only header

if __name__ == '__main__':
    unittest.main()
