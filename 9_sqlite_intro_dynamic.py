import sqlite3 as dbms

con = dbms.connect('abc.db')

cur = con.cursor()

# one time task
#cur.execute("create table student (rollno text, stname text, semester int, phoneno text, deptno text)")
#cur.execute("create table grade (rollno text, course text, marks real)")

#cur.execute("insert into student (deptno, rollno, semester, stname) values ('DS', 'BSDSF22M088', 3, 'Naveed')")
#cur.execute("insert into student (deptno, rollno, semester, stname) values ('DS', 'BSDSF22M065', 3, 'Bilawal')")
r = 'BSDSF22M088'
n = 'Zafar'
d = 'DS'
cur.execute("insert into student (rollno, stname, deptno) values(?,?,?)", (r,n,d))
con.commit()

cur.execute("SELECT rollno, stname, deptno, semester FROM student")
for row in cur:
    print(row)

cur.close()
con.close()

'''
data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()
'''
