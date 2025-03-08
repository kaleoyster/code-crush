from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_bug_report_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 750, "Bug Hunt Challenge - Bug Report")

    c.setFont("Helvetica", 12)
    fields = [
        "Student Name:", "Date:", "Program Name:", "Programming Language:",
        "Bug Category:", "Bug Location:", "Bug Description:",
        "Expected Behavior:", "Actual Behavior:", "Steps to Reproduce:",
        "Screenshot (if applicable):", "Debugging Notes:",
        "Bug Severity (Rate 1-5):", "Additional Notes:"
    ]

    y = 730
    for field in fields:
        c.drawString(50, y, field)
        y -= 40  # Space between fields

    c.save()

# Generate the PDF
create_bug_report_pdf("Bug_Report_Template.pdf")
