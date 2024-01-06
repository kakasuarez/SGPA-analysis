import PyPDF2
import re
import csv

sems = ["first sem", "third sem", "fifth sem", "seventh sem"]

def create_csv(file_name):
    pdf_file = open(f"{file_name}.pdf", "rb")
    csv_file = open(f"{file_name}.csv", "w")
    writer = csv.writer(csv_file)
    writer.writerow(["Roll number", "SGPA"])
    pdf = PyPDF2.PdfReader(pdf_file)
    regex = re.compile(r"(\d){4}(\w){3}(\d){4}")

    for page in pdf.pages:
        text = page.extract_text()
        row = []
        for i in range(len(text)):
            if i + 11 < len(text) and regex.match(text[i:i+11]):
                row.append(text[i:i+11])
            if text[i:i+2] == "RL":
                row = []
            if text[i] == "." and text[i - 1].isdigit():
                row.append(text[i-1:i+3])
                writer.writerow(row)
                row = []

    pdf_file.close()
    csv_file.close()

for sem in sems:
    create_csv(sem)