import html2text
from datetime import datetime

def convert_report():
    # Read HTML report
    with open('vectorcast_report.html', 'r') as f:
        html = f.read()
    
    # Convert to Markdown
    h = html2text.HTML2Text()
    h.body_width = 0  # Don't wrap lines
    markdown = h.handle(html)
    
    # Save as README.md
    with open('TEST_REPORT.md', 'w') as f:
        f.write(f"# Test Report\n\n")
        f.write(f"Generated: {datetime.now()}\n\n")
        f.write(markdown)

if __name__ == "__main__":
    convert_report()