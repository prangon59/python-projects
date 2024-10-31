import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    filename = Path(filepath).stem
    invoice_number, date = filename.split("-")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Main header 1st line
    pdf.set_font(family="Times", style="B", size=18)
    pdf.cell(w=50, h=8, txt=f"Invoice Number {invoice_number}", ln=1)

    # Adding date
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Date {date}", ln=1)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    # Adding a header row
    columns = list(df.columns)
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30, h=8, txt=columns[0], border=True)
    pdf.cell(w=68, h=8, txt=columns[1], border=True)
    pdf.cell(w=32, h=8, txt=columns[2], border=True)
    pdf.cell(w=30, h=8, txt=columns[3], border=True)
    pdf.cell(w=30, h=8, txt=columns[4], border=True, ln=1)

    # Adding rows to table
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=True)
        pdf.cell(w=68, h=8, txt=str(row["product_name"]), border=True)
        pdf.cell(w=32, h=8, txt=str(row["amount_purchased"]), border=True)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=True)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=True, ln=1)


    # Calculating total price row
    total_sum = df["total_price"].sum()
    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=160, h=8, txt="Total", border=True)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=True, ln=1)

    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=0, h=8, txt=f"Your Total Price is {total_sum}", ln=1)
    pdf.ln(3)

    # Add company logo
    pdf.set_font(family="Times", size=16, style="B")
    pdf.image("company.png", x=10, y=pdf.get_y(), w=8)
    pdf.set_x(19)
    pdf.cell(w=36, h=8, txt=f"Company Name") 

    pdf.output(f"PDFs/{filename}.pdf")