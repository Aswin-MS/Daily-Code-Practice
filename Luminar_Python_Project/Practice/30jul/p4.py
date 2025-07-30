"""
Question 4: Classify Files Based on Size Labels in Names

Question:
Each file name ends with _small, _medium, or _large. Print the file name and its size category.

Example Input:

files = [
    "image1.jpg_small", "video.mp4_large", "report.pdf_medium",
    "presentation.pptx_large", "data.csv_small", "icon.png_medium"
]

Expected Output:

image1.jpg_small - Small
video.mp4_large - Large
report.pdf_medium - Medium
presentation.pptx_large - Large
data.csv_small - Small
icon.png_medium - Medium
"""
files = [
    "image1.jpg_small", "video.mp4_large", "report.pdf_medium",
    "presentation.pptx_large", "data.csv_small", "icon.png_medium"
]
for i in files:
    if i.endswith('small'):
        print(f'{i}-Small')
    elif i.endswith('large'):
        print(f'{i}-Large')
    elif i.endswith('medium'):
        print(f'{i}-Medium')