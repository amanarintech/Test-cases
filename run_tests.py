# run_tests.py
import unittest
from datetime import datetime

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)
    
    def test_subtract(self):
        self.assertEqual(5 - 3, 2)

def generate_html_report(test_results):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Test Report</title>
        <style>
            body {{ font-family: Arial; margin: 20px; }}
            .pass {{ color: green; }}
            .fail {{ color: red; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ padding: 8px; border: 1px solid #ddd; }}
        </style>
    </head>
    <body>
        <h1>Test Report</h1>
        <p>Generated: {datetime.now()}</p>
        <p>Total Tests: {test_results["total"]}</p>
        <p>Passed: <span class="pass">{test_results["passed"]}</span></p>
        <p>Failed: <span class="fail">{test_results["failed"]}</span></p>
        <table>
            <tr><th>Test</th><th>Status</th></tr>
            {"".join(test_results["rows"])}
        </table>
    </body>
    </html>
    """
    with open("test_report.html", "w") as f:
        f.write(html)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMathOperations)
    result = unittest.TextTestRunner().run(suite)
    
    test_results = {
        "total": result.testsRun,
        "passed": result.testsRun - len(result.failures),
        "failed": len(result.failures),
        "rows": []
    }
    
    for test, error in result.failures:
        test_results["rows"].append(f'<tr><td>{test.id()}</td><td class="fail">FAIL</td></tr>')
    
    for test in result.passed:
        test_results["rows"].append(f'<tr><td>{test.id()}</td><td class="pass">PASS</td></tr>')
    
    generate_html_report(test_results)