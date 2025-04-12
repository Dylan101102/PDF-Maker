from fpdf import FPDF
import pandas as pd

dataframe = pd.read_csv("topics(2).csv")
pdf = FPDF(orientation='P', unit='mm', format='A4') # Will be how each PDF page looks.

# print(dataframe)

for index, row in dataframe.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    pdf.line(10, 21, 200, 21)
pdf.output('output.pdf')