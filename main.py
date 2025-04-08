from fpdf import FPDF
import pandas as pd

dataframe = pd.read_csv("topics(2).csv")
pdf = FPDF(orientation='P', unit='mm', format='A4') # Will be how each PDF page looks.

print(dataframe["Topic"], dataframe["Pages"])


"""
pdf = FPDF(orientation='P', unit='mm', format='A4')

pdf.add_page()

pdf.set_font(family='Times', style='B', size=12)
pdf.cell(w=0, h=12, txt='Hello There!', border=1, align='L', ln=1)
pdf.cell(w=0, h=12, txt='Hi There', border=1, align='L', ln=1)


pdf.output('output.pdf')
"""