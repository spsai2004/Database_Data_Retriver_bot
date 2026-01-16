# 📊 Gemini SQL Data Retriever Bot

## 📌 Project Overview

The **Gemini SQL Data Retriever Bot** is an AI-powered web application that allows users to ask questions in natural English and automatically retrieves answers from a SQLite database by generating SQL queries using Google Gemini.

This project demonstrates seamless integration of:
- AI (Google Gemini)
- Relational Databases (SQLite)
- Web Applications (Streamlit)
- Prompt Engineering

---

## 🚀 Features

- Converts English questions into SQL queries  
- Uses **Google Gemini 2.5 Flash**  
- Executes queries on a SQLite database  
- Supports JOIN, GROUP BY, ORDER BY, and aggregation  
- Displays results in an interactive Streamlit UI  
- Secure API key handling using python-dotenv  
- Prevents destructive SQL queries (DELETE, DROP, UPDATE)  

---

## 🧱 Database Schema

### STUDENT Table

| Column      | Description               |
|-------------|---------------------------|
| STUDENT_ID  | Unique student identifier |
| NAME        | Student name              |
| CLASS       | CSE / DataScience         |
| SECTION     | Section (A, E)            |

### MARKS Table

| Column      | Description                  |
|-------------|------------------------------|
| STUDENT_ID  | Foreign key to STUDENT table |
| SUBJECT     | Maths / AI / DBMS            |
| MARKS       | Marks scored                 |

### Table Relationship

The MARKS table references the STUDENT table using STUDENT_ID, forming a one-to-many relationship where one student can have multiple subject marks: STUDENT.STUDENT_ID → MARKS.STUDENT_ID

---

## 🧠 Sample Questions Supported

- Who is topper in DataScience class?
- Show marks of Krish
- Students who scored more than 85 in AI
- Average marks of each student
- Marks of students from section A

---

## 🛠️ Tech Stack

Python, Streamlit, SQLite, Google Gemini API, python-dotenv

---

## 🔐 Environment Setup

Create a `.env` file in the project root directory and add the following line exactly as shown: GOOGLE_API_KEY=your_google_gemini_api_key

---

## 📦 Install Dependencies

Install all required libraries listed in `requirements.txt` using the following command: pip install -r requirements.txt

---

## 🗄️ Database Setup

Run the following command once to create tables and insert sample data: python sqlite.py

---

## ▶️ Run the Application

Start the Streamlit application using the following command: streamlit run sql.py

---

## 🌐 Open in Browser

Access the application in your browser at the following address: http://localhost:8501
