# SGPA-analysis

## Get Started

- Since GitHub doesn't allow uploading files with size more than 25 mb, first download the PDF files from the IMS portal. [(odd semesters)](https://drive.google.com/drive/folders/1q6nU_XhFzK8HdcghuysK8_s0zN3lk4PY?usp=sharing) [(even semesters)](https://drive.google.com/drive/folders/1N124oe3kIu0wC4QF9FkECCfvz3QVGgA6)
- Rename the files as `1.pdf`, `2.pdf`, `3.pdf`, and so on for each semester.
- Place the files in the folder `data/pdf`.
- Now run `create_data.py`. This should create csv files with the roll numbers and SGPA of students. ☢️ **Note that sometimes the roll number is missing for some reason. So far, I have encountered only 2 instances and those too only in the third sem file. For now, you will have to update them manually.**
- Now that the data has been created, it is time to analyse. Open the `analysis.ipynb` file and run the code blocks in it.
