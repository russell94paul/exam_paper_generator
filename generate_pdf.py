from reportlab.pdfgen import canvas

fileName = 'SampleExamPaper.pdf'
documentTitle = 'Exam Paper Generator'
title = 'AP CS Sample Exam Paper'
subtitle = 'Answer all questions.'

textLines = ['This is question 1.']

pdf = canvas.Canvas(fileName)
pdf.setTitle(documentTitle)

pdf.save()

