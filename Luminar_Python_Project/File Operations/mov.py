f=open('D:/Aswin/Data Science/Daily-Code-Practice\movies_cleaned_pandas.csv','r')
for i in f:
    d=i.rstrip('\n').split(',')
    