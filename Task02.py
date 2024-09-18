file1=open("error_manual.txt",'r')
file2=open('grades_updated.txt','r+')
# file3=open('grades_updated.txt','w')
Lengthoffile2='' + file2.read()
print('Length of the File grade String is: ',len(Lengthoffile2))
Lengthoffile1='' + file1.read()
print('Length of the File error String is: ',len(Lengthoffile1))
file2.seek(0)
file1.seek(0)
Lengthofline2=''+file2.readline()
print('Length of line grade in the file: ',len(Lengthofline2))
Lengthofline1=''+file1.readline()
print('Length of line error in the file: ',len(Lengthofline1))
count_of_linesgrade=0
for i in range(len(Lengthoffile2)):
    if Lengthoffile2[i]=='\n':
        count_of_linesgrade+=1
print('The Total Number of lines in the file grade: ',count_of_linesgrade)
count_of_lineserror=0
for i in range(len(Lengthoffile1)):
    if Lengthoffile1[i]=='\n':
        count_of_lineserror+=1
print('The Total Number of lines in the file error: ',count_of_lineserror)
file1.seek(0)
file2.seek(0)
line2=file2.readlines()
for error_file in range(count_of_lineserror):
    try:
        line1=''+file1.readline()
        number,updated_line=line1.split(maxsplit=1)
        line2[int(number)-1]=updated_line
    except ValueError:
        #nothing to represent here just emitting the error after reading everything in the file
        print('The File error read is completed')
file2.seek(0)
file2.writelines(line2)
file1.close()
file2.close()