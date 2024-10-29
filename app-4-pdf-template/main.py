from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=8)
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    #adding page with main title header
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=20)
    pdf.line(10, 21, 200, 21) # line under the title

    # set the page lines and line colors
    pdf.set_draw_color(210, 210, 210)
    for y in range(30, 290, 10):
        pdf.line(10, y, 200, y)

    #set the footer
    pdf.ln(262)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)


    #add more pages mentioned in csv file under the title
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(274)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)

        # set the page lines and line colors
        pdf.set_draw_color(210, 210, 210)
        for y in range(30, 290, 10):
            pdf.line(10, y, 200, y)


pdf.output("output.pdf")
