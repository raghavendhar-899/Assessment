import unittest
import os
import subprocess

class TestFlowLogParser(unittest.TestCase):
    
    def setUp(self):
        self.lookup_file = 'test_lookup_table.csv'
        self.flow_file = 'test_flow_logs.txt'
        self.output_file = 'test_output.txt'
        self.expected_output_file = 'expected_test_output.txt'
        self.default_output_file = 'output.txt'
        self.default_expected_output_file = 'expected_output.txt'

    def compare_output_with_expected(self, output_file, expected_output_file):
        with open(output_file, 'r') as file:
            output_content = file.read()
        
        with open(expected_output_file, 'r') as file:
            expected_content = file.read()
        
        self.assertEqual(output_content.strip(), expected_content.strip())

    def test_main_with_custom_files(self):
        # Run the main script with custom files
        result = subprocess.run(
            ['python', 'main.py', self.lookup_file, self.flow_file, self.output_file],
            capture_output=True,
            text=True
        )

        self.assertEqual(result.returncode, 0)
        self.compare_output_with_expected(self.output_file, self.expected_output_file)


    def test_main_with_default_files(self):
        
        # Run the main script without arguments to use default files
        result = subprocess.run(
            ['python', 'main.py'],
            capture_output=True,
            text=True
        )

        self.assertEqual(result.returncode, 0)
        self.compare_output_with_expected(self.default_output_file, self.default_expected_output_file)


    def tearDown(self):
        # Remove output files after tests
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
        if os.path.exists(self.default_output_file):
            os.remove(self.default_output_file)

if __name__ == '__main__':
    unittest.main()
