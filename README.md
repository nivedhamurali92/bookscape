BookScape-Explorer

The BookScape Explorer project aims to facilitate users in discovering and analyzing book data through a web application. The application will extract data from online book APIs, store this information in a SQL database, and enable data analysis using SQL queries.

Project Overview

The Books Explorer project is a web-based application built using Streamlit and MySQL. It allows users to:

Search for books using the Google Books API.

View detailed analytics on books stored in the database.

Answer frequently asked questions about books based on SQL queries.

Features

Search for books using keywords and store in SQL database.

View analytics, such as top authors, publishers, and categories.

#Project Objectives
Data Integration: Combine external API data with database analytics.

Data Storage: Create a SQL database with well-designed schema using appropriate data types and primary keys.

Interactive Visualization: Present results in an engaging and user-friendly format.

Scalability: Create a framework that supports additional queries and features.

Setup Instructions
Prerequisites
Python 3.7+

MySQL Server

Google Books API Key

Required Python Libraries:
streamlit

pymysql

pandas

requests

Installation Steps
Clone the Repository
git clone https://github.com/your-repo/books-explorer.git cd books-explorer

Install Dependencies
pip install -r requirements.txt

Set Up MySQL Database
Create a database named database2.

Import the schema and data from database2.sql.

Add Google Books API Key

Replace the api_key variable in the script with your API key.

Run the Application

streamlit run app.py

Access the Application

Open http://localhost:8501 in your browser.

Challenges Faced
Data Cleaning:
Managing inconsistent data between API and database.

Handling missing or null values in certain fields.

API Rate Limits:
Google Books API limits the number of requests, requiring optimization of API calls.

Database Optimization:
Ensuring SQL queries run efficiently with indexed columns.Insights and Learnings

Insights and Learnings
Successfully integrated Google Books API, enabling real-time data retrieval.

Gained insights into book trends, such as popular authors, languages, and publishers.

Leveraged expanders and tabs for an intuitive user experience in Streamlit.
