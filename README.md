# Flow Log Assessment

## Overview

The Flow Log Parser is a Python script designed to process network flow logs and map each row to a tag based on a lookup table. The script generates reports detailing the count of matches for each tag and the frequency of each port/protocol combination.

## Files

Script files:
- `flow_log_parser.py`: Main script for parsing flow logs and generating reports.
- `test_flow_log_parser.py`: Unit tests for verifying the script's functionality.

Data files:
- `lookup_table.csv`: Example lookup table for mapping ports/protocols to tags.
- `flow_logs.txt`: Example flow log data.
- `expected_output.txt`: Example expected output for comparison in tests.
- `test_lookup_table.csv`: Test lookup table for mapping ports/protocols to tags.
- `test_flow_logs.txt`: Test flow log data for testing.
- `expected_tes_output.txt`: Test expected output for comparison in test.


## Setup

### Prerequisites

- Python 3.x
- Standard Python libraries (no additional packages required)

### Installation

Clone the repository:
   ```bash
   git clone https://github.com/raghavendhar-899/Assessment.git
   cd Assessment
  ```

### Usage

To run the script with default filenames:
  ```bash
  python main.py
  ```
To run the script with custom files:
  ```bash
  python main.py <lookup_table> <flow_logs> <output_file_name>
  ```
example: python main.py lookup_table.csv flow_logs.txt output.txt

### Testing

Run Tests:
  ``` bash
  python -m unittest test_flow_log_parser.py
  ```
Test case 1: Default test cases mentioned in the mail  
Test case 2: Testing other protocals and case insensitivity  

## Assumptions

1. Flow Log File: Contains version 2 log entries.  
2. Lookup Table File: Maps destination ports and protocols to specific tags.  
3. Tags in the lookup table map to specific port/protocol combinations.  
4. Flow logs are matched against these combinations to assign appropriate tags.  
5. Supported protocols TCP, UDP, ICMP. If more protocols are used/require we can update the code.  
6. Tags are case sensitive.  

### Thank you for giving me this opportunity to present my skills

