

# Import necessary libraries
import pandas as pd                # For reading and analyzing the data
from fpdf import FPDF              # For creating the PDF report

# Step 1: Read the CSV file
data = pd.read_csv('data.csv')     # Loads data like names and scores from a file named "data.csv"

# Step 2: Analyze the data
average_score = data['Score'].mean()   # Calculates the average of the "Score" column

# Step 3: Create a new PDF document
pdf = FPDF()                        # Create a blank PDF
pdf.add_page()                      # Add a new page to it
pdf.set_font("Arial", size=12)      # Set the font and size

# Step 4: Add a title to the PDF
pdf.set_font("Arial", 'B', 14)      # Use bold font for the title
pdf.cell(200, 10, txt="Student Score Report", ln=True, align='C')  # Centered title

pdf.set_font("Arial", size=12)      # Switch back to normal font
pdf.ln(10)                          # Add a line break

# Step 5: Add each student's score
for index, row in data.iterrows():
    pdf.cell(200, 10, txt=f"{row['Name']}: {row['Score']}", ln=True)

# Step 6: Add the average score
pdf.ln(5)
pdf.cell(200, 10, txt=f"Average Score: {average_score:.2f}", ln=True)

# Step 7: Save the PDF
pdf.output("report.pdf")           # The report is saved as "report.pdf"

print("Report generated: report.pdf")


