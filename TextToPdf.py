from fpdf import FPDF
import os
import sys
import calendar
import datetime
import csv
import envVars

month_days = calendar.monthrange(datetime.datetime.now().year, datetime.datetime.now().month)[1]
present_days = calendar.monthrange(datetime.datetime.now().year, datetime.datetime.now().month)[1]

envVars.setVariables()

class PDF(FPDF):
    # main header
    def header(self):
        # Logo
        self.image('sample_logo.png', 10, 10, 10)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(50)
        # Title
        self.set_text_color(10, 100, 200)
        self.cell(0, 10, str(os.environ['title']), 0, 0, 'L')
        # Line break
        self.ln(8)

    # office address details in pay slip
    def address(self):
        pdf.set_font('Times', '', 10)
        pdf.cell(0, 5, str(os.environ['title2']), 0, 1, 'C')
        pdf.cell(0, 5, str(os.environ['title3']), 0, 1, 'C')
        pdf.cell(0, 5, str(os.environ['title4']), 0, 1, 'C')
        pdf.cell(0, 5, str(os.environ['title5']), 0, 1, 'C')

    # Decorative spacing
    def para(self):
        self.ln(10)

    # personal details and working days
    def personal_details(self):
        pdf.cell(0, 5, str(os.environ['desc2']) + row[0], 1, 0, 'L')
        pdf.cell(0, 5, str(os.environ['desc3']) + str(month_days), 1, 1, 'R')
        pdf.cell(0, 5, str(os.environ['desc4']) + row[1], 1, 0, 'L')
        pdf.cell(0, 5, str(os.environ['desc5']) + str(month_days), 1, 1, 'R')
        pdf.cell(0, 5, str(os.environ['desc6']) + row[2], 1, 0, 'L')
        pdf.cell(0, 5, str(os.environ['desc7']) + '0', 1, 1, 'R')
        pdf.cell(0, 5, str(os.environ['desc8']) + row[3], 1, 0, 'L')
        pdf.cell(0, 5, str(os.environ['desc9']) + str(month_days), 1, 1, 'R')
        pdf.para()

    # salary info details
    def salary_details(self):
        pdf.center_sub_title(str(os.environ['center']))
        for i in range(2):
            pdf.para()
        pdf.left_sub_title(str(os.environ['left']), 'L')
        pdf.para()
        pdf.set_text_color(0, 0, 0)
        pdf.set_font('Times', '', 10)
        pdf.cell(0, 5, str(os.environ['desc12']), 1, 0, 'L')
        pdf.cell(0, 5, row[4], 1, 1, 'R')
        pdf.cell(0, 5, str(os.environ['desc13']), 1, 0, 'L')
        pdf.cell(0, 5, row[5], 1, 1, 'R')
        pdf.para()
        pdf.set_font('Times', 'B', 10)
        pdf.left_sub_title(str(os.environ['right']), 'L')
        pdf.para()
        pdf.set_text_color(0, 0, 0)
        pdf.set_font('Times', '', 10)
        pdf.cell(0, 5, str(os.environ['desc15']), 1, 0, 'L')
        pdf.cell(0, 5, row[6], 1, 1, 'R')
        pdf.para()
        pdf.set_font('Times', 'B', 10)
        pdf.left_sub_title(str(os.environ['desc16']), 'L')
        pdf.para()
        pdf.set_text_color(0, 0, 0)
        pdf.set_font('Times', '', 10)
        pdf.cell(0, 5, str(os.environ['desc14']), 1, 0, 'L')
        pdf.set_font('Times', 'B', 10)
        pdf.cell(0, 5, str(int(row[4]) + int(row[5]) - int(row[6])), 1, 1, 'R')

    # footer comments
    def conclusion(self):
        for i in range(3):
            pdf.para()
        pdf.set_font('Times', '', 10)
        pdf.cell(0, 5, str(os.environ['desc17']), 0, 1, 'L')
        pdf.cell(0, 5, str(os.environ['desc18']), 0, 1, 'L')
        pdf.cell(0, 5, str(os.environ['desc19']), 0, 1, 'L')
        for i in range(2):
            pdf.para()
        pdf.cell(0, 5, str(os.environ['disc1']), 0, 1, 'L')
        pdf.cell(0, 5, str(os.environ['disc2']), 0, 1, 'L')

    # Sub heading Salary Slip
    def center_sub_title(self, item):
        self.set_font('Arial', 'B', 12)
        self.set_text_color(10, 100, 200)
        self.cell(0, 10, item, 0, 0, 'C')

    # sub title for items
    def left_sub_title(self, item, align):
        self.set_font('Arial', 'B', 10)
        self.set_text_color(0, 0, 0)
        self.cell(0, 10, item, 1, 0, align)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# Instantiation of inherited class
with open('Employee.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        pdf = PDF()
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.address()
        pdf.para()
        pdf.personal_details()
        pdf.salary_details()
        pdf.conclusion()
        pdf.output((row[0].split(" ")[0]) + '_' + datetime.datetime.now().strftime("%B") + '_' + str(datetime.datetime.now().year) + '.pdf', 'F')
