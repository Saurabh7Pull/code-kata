# Data Engineering Coding Challenges
This forked repository contains solutions to two problems for Demyst Data Engineering Challenge: parsing and anonymizing fixed-width and CSV files. 

## Judgment Criteria

- Beauty of the code (beauty lies in the eyes of the beholder)
- Testing strategies
- Basic Engineering principles

## Description
This repository contains solutions to two data engineering tasks:
1. Parsing and converting fixed-width files to CSV format.
2. Anonymizing sensitive data in large CSV files, including a scalable solution using Apache Spark.

## Problem 1

### Parse fixed width file

- Generate a fixed width file using the provided spec (offset provided in the spec file represent the length of each field).
- Implement a parser that can parse the fixed width file and generate a delimited file, like CSV for example.
- DO NOT use python libraries like pandas for parsing. You can use the standard library to write out a csv file (If you feel like)
- Language choices (Python or Scala)
- Deliver source via github or bitbucket
- Bonus points if you deliver a docker container (Dockerfile) that can be used to run the code (too lazy to install stuff that you might use)
- Pay attention to encoding

### Files
- `fixed_width_generator.py`: Generates a fixed-width file based on a given specification.
- `fixed_width_parser.py`: Parses a fixed-width file and converts it to a CSV file.
- `test_fixed_width.py`: Unit tests for the fixed-width file generation and parsing.

## Problem 2

### Data processing

- Generate a csv file containing first_name, last_name, address, date_of_birth
- Process the csv file to anonymise the data
- Columns to anonymise are first_name, last_name and address
- You might be thinking  that is silly
- Now make this work on 2GB csv file (should be doable on a laptop)
- Demonstrate that the same can work on bigger dataset
- Hint - You would need some distributed computing platform
  
### Files
- `generate_csv.py`: Generates a CSV file with dummy data.
- `anonymize_data.py`: Anonymizes the sensitive data in the CSV file.
- `anonymize_data_spark.py`: Anonymizes the sensitive data in the CSV file using Apache Spark for scalability.
- `test_anonymize.py`: Unit tests for the anonymization functions.

## Choices

- Any language, any platform
- One of the above problems or both, if you feel like it.

### Repository Structure
```
code-kata/
├── Problem1_Parse_Fixed_Width_File/
│   ├── fixed_width_generator.py
│   ├── fixed_width_parser.py
│   ├── test_fixed_width.py
│   └── README.md
│
├── Problem2_Data_Processing/
│   ├── generate_csv.py
│   ├── anonymize_data.py
│   ├── anonymize_data_spark.py
│   ├── test_anonymize.py
│   └── README.md
│
└── README.md
```
