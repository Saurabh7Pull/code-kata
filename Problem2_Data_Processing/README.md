# CSV Anonymization

## Description
This folder includes scripts to generate a CSV file and anonymize its data. It also includes a Spark implementation for processing large files.

## Usage
### Generate CSV File
```bash
python generate_csv.py
```
### Anonymize CSV File
```bash
python anonymize_data.py
```
### Anonymize Large CSV File with Spark
```bash
spark-submit anonymize_data_spark.py sample.csv anonymized_sample_spark
```

### Run Tests
```bash
python -m unittest test_anonymize.py
```
