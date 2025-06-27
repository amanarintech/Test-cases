import json
from datetime import datetime

def generate_report():
    # Complete test data structure
    test_data = {
        "date": datetime.now().strftime("%d %b %Y"),
        "time": datetime.now().strftime("%I:%M:%S %p"),
        "version": "24.sp7 (02/06/25)",
        "results": [
            {
                "name": "ALL", 
                "build": "14/26 (53%)", 
                "build_time": "06:41",
                "expected": "4876/4894 (99%)",
                "testcases": "785/806 (97%)",
                "execute_time": "03:24",
                "statements": "2614/2758 (94%)",
                "branches": "1316/1398 (94%)",
                "status": "warning"
            },
            {
                "name": "GNU_Native_Manual__32-bit__9.x_9.2_C",
                "build": "14/14 (100%)",
                "build_time": "06:41",
                "expected": "4876/4894 (99%)",
                "testcases": "785/806 (97%)",
                "execute_time": "03:24",
                "statements": "2614/2758 (94%)",
                "branches": "1316/1398 (94%)",
                "status": "success"
            }
            # Add more test cases as needed
        ]
    }
    
    # Read template
    with open('report_template.html', 'r') as f:
        html = f.read()
    
    # Insert dynamic data
    html = html.replace("10 JUN 2025", test_data["date"])
    html = html.replace("1:53:45 PM", test_data["time"])
    
    # Save final report
    with open('vectorcast_report.html', 'w') as f:
        f.write(html)

if __name__ == "__main__":
    generate_report()