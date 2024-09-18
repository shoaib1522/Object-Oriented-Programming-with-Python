file1=open('grades.txt','r')
file2=open('errors.txt','w')
Lengthoffile='' + file1.read()
print('Length of the File String is: ',len(Lengthoffile))
file1.seek(0)
Lengthofline=''+file1.readline()
print('Length of line in the file: ',len(Lengthofline))
# for i in range(len(Lengthoffile)):
#     if Lengthoffile[i]=='\n':
#         count_of_lines+=1
file1.seek(0)
lines=file1.readlines()
count_of_lines=len(lines)
print('The Total Number of lines in the file: ',count_of_lines)
file1.seek(0)
file1.readline()
file1.readline()
error_count=0
for error in range(3,count_of_lines+1):
    Line=""+file1.readline()
    for index in range(len(Line)):
        if index<10:
            if Line[index]==" ":
                error_count+=1
                print("Error # ",error_count,':')
                print(Line)
                file2.write(f'{error} ' + Line)
                break
file1.seek(0)
file1.readline()
file1.readline()
for error in range(3,count_of_lines+1):
    Line=""+file1.readline()
    for i in range(len(Line)):
        if  len(Line)<58:
            error_count+=1                
            print("Error # ",error_count,':')
            print(Line)
            file2.write(f"{error} " + Line)
        break
file1.seek(0)
file1.readline()
file1.readline()
for error in range(3,count_of_lines+1):
    try:
        Line=""+file1.readline()
        roll_no,second_name,crs,md,ss,fn=Line.split(maxsplit=5)
        try:
            md_check=int(md)
            ss_check=int(ss)
            fn_check=int(fn)
        except ValueError:
            error_count+=1                
            print("Error # ",error_count,':')
            print(Line)
            file2.write(f"{error} " + Line)
    except ValueError:
            error_count+=1                
            print("Error # ",error_count,':')
            print(Line)
            file2.write(f"{error} " + Line)
file1.close()
file2.close()
print('The Total Number of errors in the file are: ',error_count)
    