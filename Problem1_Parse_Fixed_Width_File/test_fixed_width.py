# test_fixed_width.py

import unittest
from fixed_width_generator import generate_fixed_width_file
from fixed_width_parser import parse_fixed_width_file

class TestFixedWidthProcessing(unittest.TestCase):
    def setUp(self):
        self.spec = [10, 15, 20]
        self.data = [
            ['Bill', 'Data Engineer', 'bill@example.com'],
            ['Bob', 'Data Scientist', 'bob@example.com']
        ]
        self.empty_data = []
        generate_fixed_width_file(self.spec, self.data, 'test_fixed_width.txt')
        generate_fixed_width_file(self.spec, self.empty_data, 'empty_fixed_width.txt')

    def test_fixed_width_generation_and_parsing(self):
        parse_fixed_width_file(self.spec, 'test_fixed_width.txt', 'test_output.csv')

        with open('test_output.csv', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        expected_output = [
            'Bill,Data Engineer,bill@example.com\n',
            'Bob,Data Scientist,bob@example.com\n'
        ]

        self.assertEqual(lines, expected_output)

    def test_empty_file(self):
        parse_fixed_width_file(self.spec, 'empty_fixed_width.txt', 'empty_output.csv')

        with open('empty_output.csv', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        self.assertEqual(lines, [])

if __name__ == '__main__':
    unittest.main()
