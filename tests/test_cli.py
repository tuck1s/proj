# Test the CLI by mocking the command-line argparse arguments and the print function

import unittest
from unittest.mock import patch
from proj.cli import main
import argparse

class TestCLI(unittest.TestCase):
    @patch('argparse.ArgumentParser.parse_args')
    def test_f1(self, mock_parse_args):
        # Mock the command-line arguments
        mock_parse_args.return_value = argparse.Namespace(function='f1', value=10)
        
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_once_with(20)  # Assuming f1(x) returns x * 2

    @patch('argparse.ArgumentParser.parse_args')
    def test_f2(self, mock_parse_args):
        # Mock the command-line arguments
        mock_parse_args.return_value = argparse.Namespace(function='f2', value=5)
        
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_once_with(10)  # Assuming f2(x) returns x * 2

if __name__ == '__main__':
    unittest.main()