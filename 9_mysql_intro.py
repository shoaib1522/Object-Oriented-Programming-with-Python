#python -m pip install mysql-connector-python
#pip install mysql-connector-python
#mysql-connector-python

import mysql.connector as dbms

#++++++++++++++++++++++++++++++++
# Better create your own account
# and databse at freemysqlhosting
#++++++++++++++++++++++++++++++++

#pw = getpass.getpass("Enter password: ")
#print(pw)

#port 3306
con = dbms.connect(
  host="sql12.freemysqlhosting.net",
  user="usr_name_of_dbms_server",
  password="pswrd",
  database="db_name"
)
print("Successfully connected to MySQL Database")

cur = con.cursor()

#one time task
#cur.execute("create table student (rollno text, stname text, semester int, phoneno text, deptno text)")
#cur.execute("create table grade (rollno text, course text, marks real)")

cur.execute("insert into student (deptno, rollno, semester, stname) values ('DS', 'BSDSF22M088', 3, 'Naveed')")
cur.execute("insert into student (deptno, rollno, semester, stname) values ('DS', 'BSDSF22M065', 3, 'Bilawal')")
cur.execute("""insert into student (rollno, stname, deptno) values ('BSDSF22M088', 'Zafar', 'DS')""")
#con.commit()


cur.execute("SELECT rollno as rno, stname as name FROM student")
print(cur.description[0][0], cur.description[1][0])
for row in cur:
   print(row[1], row[0])

cur.close()
con.close()
