import json
from datetime import datetime

def generate_report():
    # Load test data (replace with your actual test results)
    test_data = {
        "date": datetime.now().strftime("%d %b %Y"),
        "time": datetime.now().strftime("%I:%M:%S %p"),
        "version": "24.sp7 (02/06/25)",
        "results": [
            # Add your actual test results here
            {"name": "ALL", "build": "14/26 (53%)", "status": "warning", ...}
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