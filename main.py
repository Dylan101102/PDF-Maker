from fpdf import FPDF
import pandas as pd

dataframe = pd.read_csv("topics(2).csv")
# Will be how each PDF page looks.
pdf = FPDF(orientation='P', unit='mm', format='A4')
# Disabled auto page breaking mode.
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in dataframe.iterrows():
    for page in range(row['Pages']):
        pdf.add_page()
        pdf.set_font(family='Times', style='B', size=24)
        pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)

        # To add lines.
        """
        291 is around the length of the longer side of an A4 doc in portrait mode in mm.
        7 represents a good length between each line in mm.
        Playing around with the middle number in the condition achieved desired result.
        """
        for y in range(21, 291, 7):
            pdf.line(10, y, 200, y)

        # To add footer.
        # Drops to the bottom using line breaks based on A4 document dimensions.
        pdf.ln(265)
        pdf.set_font(family='Times', style='I', size=8)
        pdf.cell(w=0, h=8, txt=row['Topic'], align='R')
pdf.output('output.pdf')
