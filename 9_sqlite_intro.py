import sqlite3 as dbms

con = dbms.connect('abc.db')

cur = con.cursor()

# one time task
#cur.execute("create table student (rollno text, stname text, semester int, phoneno text, deptno text)")
#cur.execute("create table grade (rollno text, course text, marks real)")

#cur.execute("insert into student (deptno, rollno, semester, stname) values ('DS', 'BSDSF22M088', 3, 'Naveed')")
#cur.execute("insert into student (deptno, rollno, semester, stname) values ('DS', 'BSDSF22M065', 3, 'Bilawal')")
#cur.execute("insert into student (rollno, stname, deptno) values ('BSDSF22M052', 'Zafar', 'DS')")
#con.commit()

cur.execute("SELECT rollno as rooolno, stname FROM student")

print(cur.description[0][0], cur.description[1][0])
for row in cur:
    print(row[0], row[1])

cur.close()
con.close()
