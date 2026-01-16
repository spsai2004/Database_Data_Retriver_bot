import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# STUDENT table
cursor.execute("""
CREATE TABLE IF NOT EXISTS STUDENT(
    STUDENT_ID INTEGER,
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25)
);
""")

# MARKS table (linked by STUDENT_ID)
cursor.execute("""
CREATE TABLE IF NOT EXISTS MARKS(
    STUDENT_ID INTEGER,
    SUBJECT VARCHAR(25),
    MARKS INTEGER
);
""")

# Clear old data (important if re-running)
cursor.execute("DELETE FROM STUDENT")
cursor.execute("DELETE FROM MARKS")

# Insert STUDENT data
cursor.execute("""INSERT INTO STUDENT VALUES(1,'Krish','DataScience','A')""")
cursor.execute("""INSERT INTO STUDENT VALUES(2,'Sai','CSE','E')""")
cursor.execute("""INSERT INTO STUDENT VALUES(3,'Santhosh','CSE','A')""")
cursor.execute("""INSERT INTO STUDENT VALUES(4,'Shiva','CSE','A')""")
cursor.execute("""INSERT INTO STUDENT VALUES(5,'Harsha','DataScience','A')""")

# Insert MARKS (Sai has highest marks)

# Krish (ID = 1)
cursor.execute("""INSERT INTO MARKS VALUES(1,'Maths',85)""")
cursor.execute("""INSERT INTO MARKS VALUES(1,'AI',88)""")
cursor.execute("""INSERT INTO MARKS VALUES(1,'DBMS',86)""")

# Sai (ID = 2) → TOPPER
cursor.execute("""INSERT INTO MARKS VALUES(2,'Maths',98)""")
cursor.execute("""INSERT INTO MARKS VALUES(2,'AI',97)""")
cursor.execute("""INSERT INTO MARKS VALUES(2,'DBMS',96)""")

# Santhosh (ID = 3)
cursor.execute("""INSERT INTO MARKS VALUES(3,'Maths',82)""")
cursor.execute("""INSERT INTO MARKS VALUES(3,'AI',84)""")
cursor.execute("""INSERT INTO MARKS VALUES(3,'DBMS',85)""")

# Shiva (ID = 4)
cursor.execute("""INSERT INTO MARKS VALUES(4,'Maths',90)""")
cursor.execute("""INSERT INTO MARKS VALUES(4,'AI',92)""")
cursor.execute("""INSERT INTO MARKS VALUES(4,'DBMS',89)""")

# Harsha (ID = 5)
cursor.execute("""INSERT INTO MARKS VALUES(5,'Maths',80)""")
cursor.execute("""INSERT INTO MARKS VALUES(5,'AI',83)""")
cursor.execute("""INSERT INTO MARKS VALUES(5,'DBMS',78)""")

print("STUDENT and MARKS tables created correctly")

conn.commit()
conn.close()
