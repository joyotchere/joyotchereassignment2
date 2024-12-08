import unittest
from assignment2 import rss_mem_of_pid  # Import the function from assignment2.py

class TestPidMem(unittest.TestCase):
    
    def test_rss_total(self):
        # Expected result (you'll need to adjust this value based on your system's PID 1610 memory usage)
        expected = 58808  # Replace with the actual expected value for PID 1610
        
        # Call the function without arguments (uses the default PID 1610)
        given = rss_mem_of_pid()

        # Compare the result with the expected value
        self.assertEqual(given, expected, f"ERROR: {given} != {expected}")

    def test_rss_total_custom_pid(self):
        # Expected result for the custom PID (replace with actual expected value)
        expected = 12345  # Replace with the expected value for PID 1234
        
        # Call the function with a custom PID (e.g., 1234)
        given = rss_mem_of_pid('1234')  # Pass custom PID as an argument

        # Compare the result with the expected value
        self.assertEqual(given, expected, f"ERROR: {given} != {expected}")









