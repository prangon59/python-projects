from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=8)
df = pd.read_csv("topics.csv")

# Function to add header with title and underline
def add_header(title):
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=title, align="L", ln=1)
    pdf.line(10, 21, 200, 21)  # Line under the title

# Function to add notebook-style horizontal lines
def add_page_lines():
    pdf.set_draw_color(210, 210, 210)  # set the line color to Light gray
    for y in range(30, 290, 10):  # Draw lines with 10 mm spacing
        pdf.line(10, y, 200, y)

# Function to add footer with topic name
def add_footer(topic):
    pdf.ln(262)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=topic, align="R", ln=1)

# Main loop to iterate over each topic
for index, row in df.iterrows():
    pdf.add_page()
    add_header(row["Topic"])       # Add header with title
    add_page_lines()               # Add notebook-style lines
    add_footer(row["Topic"])       # Add footer

    # Add additional pages as specified in the CSV
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        add_page_lines()           # Add lines to additional pages
        add_footer(row["Topic"])   # Add footer to additional pages

pdf.output("output.pdf")
