# run_tests.py
import unittest
from unittest2html import HTMLTestRunner

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)
    
    def test_subtract(self):
        self.assertEqual(5 - 3, 2)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMathOperations)
    
    with open("test_report.html", "w") as f:
        runner = HTMLTestRunner(
            stream=f,
            title="Test Report",
            description="Automated test results"
        )
        runner.run(suite)