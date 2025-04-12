from fpdf import FPDF
import pandas as pd

dataframe = pd.read_csv("topics(2).csv")
pdf = FPDF(orientation='P', unit='mm', format='A4') # Will be how each PDF page looks.
pdf.set_auto_page_break(auto=False, margin=0) # Disabled auto page breaking mode.

# print(dataframe)

for index, row in dataframe.iterrows():
    for page in range(row['Pages']):
        pdf.add_page()
        pdf.set_font(family='Times', style='B', size=24)
        pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
        pdf.line(10, 21, 200, 21)

        # To add footer.
        pdf.ln(265) # Height in mm of an A4 document.
        pdf.set_font(family='Times', style='I', size=8)
        pdf.cell(w=0, h=8, txt=row['Topic'], align='R')
pdf.output('output.pdf')