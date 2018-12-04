# XML-CSV Conversion For Bandwidth's Number Utilization Review

This is a simple script that allows easy conversion from a single CSV file with any number of phone numbers to multiple XML files with a limit of 5000 numbers per file. This allows someone to programmatically assign all of their phone numbers using Bandwidth's Dashboard API after reviewing their phone numbers.


## Installation

Clone this repo, and run

```
pip install -r requirements.txt
```

to install the dependencies.

Python version: 3.7.0

## Usage

After reviewing your numbers, save them in a CSV file in this repo. Your CSV file should look like this

```
Number
9999999999
8888888888
7777777777
...
```

Make an empty directory, and then run the following command

```
python convert.py <file_name> <directory_destination> <action_value> <order_id>
```

Example:

```
python convert.py assign.csv assign-directory ASSIGN ID-123
```

The directory must already be created, and should not include an ending /


This will create multiple XML files (0.xml, 1.xml, 2.xml...) with 5000 phone numbers in each file in the given directory. You can then use these files with Bandwidth's Dashboard API to bulk assign/unassign these phone numbers
