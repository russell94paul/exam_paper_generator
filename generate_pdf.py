from reportlab.pdfgen import canvas
import pandas as pd


# Read in the csv
data = pd.read_csv('APCS_QuestionDB.csv', header = 0)
#print(data.head())
#print(data.columns)



# Separate out question types (columns) into their own vairables for readability
mcq = data['MCQ'] # mcqs may need to be categorized by topic so we can generate questions on all topics
frs_q1 = data['FRS_Q1']
frs_q2 = data['FRS_Q2']
frs_q3 = data['FRS_Q3']
frs_q4 = data['FRS_Q4']

# Multiple Choice - 40 questions total
random_40_mcqs = mcq.sample(n = 40)
print(random_40_mcqs)









"""
fileName = "SampleExamPaper.pdf"
documentTitle = "Exam Paper Generator"
title = "AP CS Sample Exam Paper"
subtitle = "Answer all questions."
section_one = "Section 1: Multiple Choice"
section_two = "Section 2: Free Response"




pdf = canvas.Canvas(fileName)
pdf.drawString(225,100, documentTitle)
pdf.save()

"""