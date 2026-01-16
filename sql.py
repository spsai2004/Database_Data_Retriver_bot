from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_resopose(question, prompt):
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content([prompt[0], question])
    return response.text.strip()

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    return rows

prompt = [
"""
You are an expert system that converts English questions into SQL queries.

Database schema:

Table: STUDENT
Columns:
- STUDENT_ID
- NAME
- CLASS
- SECTION

Table: MARKS
Columns:
- STUDENT_ID
- SUBJECT
- MARKS

Relationship:
- STUDENT.STUDENT_ID is linked to MARKS.STUDENT_ID.

Classes:
- CSE
- DataScience

Subjects:
- Maths
- AI
- DBMS

Rules:
1. Generate ONLY the SQL query.
2. Do NOT include the word 'sql'.
3. Do NOT use triple quotes or backticks.
4. Use JOINs when data from both tables is required.
5. Use double quotes for string values.
6. Do NOT generate DELETE, UPDATE, INSERT, or DROP queries.
7. Column and table names must match exactly.

Examples:

Question: Show marks of Krish.
Output:
SELECT MARKS.SUBJECT, MARKS.MARKS
FROM MARKS
JOIN STUDENT ON STUDENT.STUDENT_ID = MARKS.STUDENT_ID
WHERE STUDENT.NAME="Krish";

Question: Show marks of students from section A.
Output:
SELECT STUDENT.NAME, MARKS.SUBJECT, MARKS.MARKS
FROM STUDENT
JOIN MARKS ON STUDENT.STUDENT_ID = MARKS.STUDENT_ID
WHERE STUDENT.SECTION="A";

Question: Show average marks of each student.
Output:
SELECT STUDENT.NAME, AVG(MARKS.MARKS)
FROM STUDENT
JOIN MARKS ON STUDENT.STUDENT_ID = MARKS.STUDENT_ID
GROUP BY STUDENT.STUDENT_ID;

Question: List students who scored more than 85 in AI.
Output:
SELECT STUDENT.NAME
FROM STUDENT
JOIN MARKS ON STUDENT.STUDENT_ID = MARKS.STUDENT_ID
WHERE MARKS.SUBJECT="AI" AND MARKS.MARKS > 85;

Question: Who is topper in DataScience class?
Output:
SELECT STUDENT.NAME
FROM STUDENT
JOIN MARKS ON STUDENT.STUDENT_ID = MARKS.STUDENT_ID
WHERE STUDENT.CLASS="DataScience"
GROUP BY STUDENT.STUDENT_ID
ORDER BY SUM(MARKS.MARKS) DESC
LIMIT 1;

Now convert the following English question into a SQL query:
"""
]



st.set_page_config(page_title="Retrieve Data")
st.header("🔍 Gemini App to Retrieve SQL Data")

question = st.text_input("Enter your question:")
submit = st.button("Ask Question")

if submit and question:
    sql_query = get_gemini_resopose(question, prompt)

    st.subheader("Generated SQL Query")
    st.code(sql_query, language="sql")

    try:
        results = read_sql_query(sql_query, "student.db")

        st.subheader("Results")
        if results:
            for row in results:
                st.write(row)
        else:
            st.info("No records found.")

    except Exception as e:
        st.error(f"SQL Error: {e}")
