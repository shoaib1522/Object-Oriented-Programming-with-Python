#python -m pip install mysql-connector-python
#pip install mysql-connector-python
#mysql-connector-python

#++++++++++++++++++++++++++++++++
# Better create your own account
# and databse at freemysqlhosting
#++++++++++++++++++++++++++++++++

import mysql.connector as dbms

try:

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

    cur = con.cursor(prepared=True)

    #one time task
    #cur.execute("create table student (rollno text, stname text, semester int, phoneno text, deptno text)")
    #cur.execute("create table grade (rollno text, course text, marks real)")

    cur.execute("insert into student (deptno, rollno, semester, stname) values ('DS', 'BSDSF22M088', 3, 'Naveed')")
    r = 'BSDSF22M088'
    n = 'Zafar'
    d = 'DS'
    cur.execute("insert into student (deptno, rollno, semester, stname) values (%s, %s, %s, %s)", (d,r,4,n))
    cur.execute("""insert into student (rollno, stname, deptno) values ('BSDSF22M088', 'Zafar', 'DS')""")
    con.commit()

    cur.execute("SELECT rollno, stname, deptno, semester FROM student")
    for row in cur:
       print(row[1], row[0], row[2], row[3])

except mysql.connector.Error as error:
    print("parameterized query failed {}".format(error))

finally:
    if con.is_connected():
        cur.close()
        con.close()
        print("MySQL connection is closed")
