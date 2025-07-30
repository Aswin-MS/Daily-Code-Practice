"""
Question 1: Classify Each File as Image or Document

Question:
Given a list of file names, print each file name along with its type: either Image or Document.

Image files: .jpg, .jpeg, .png, .gif

Document files: .pdf, .docx, .txt


Example Input:

files = [
    "photo1.jpg", "report.pdf", "image.png", "notes.txt",
    "logo.gif", "resume.docx", "holiday.jpeg", "data.csv"
]

Expected Output:

photo1.jpg - Image
report.pdf - Document
image.png - Image
notes.txt - Document
logo.gif - Image
resume.docx - Document
holiday.jpeg - Image
data.csv - Unknown

"""
files = ["photo1.jpg", "report.pdf", "image.png", "notes.txt", "logo.gif", "resume.docx", "holiday.jpeg", "data.csv"]
img=['jpg', 'jpeg', 'png', 'gif']
doc=['pdf','docx','txt']
for i in files:
    d=i.split('.')
    if d[1] in img:
        print(i,"-Image")
    elif d[1] in doc:
        print(i,"-Document")
    else:
        print(i,"-Unknown")
