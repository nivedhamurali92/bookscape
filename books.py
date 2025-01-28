import streamlit as st

import pymysql
import pandas as pd
db_config ={
    'host':'localhost',
     'user':'root',
      'password':'kasthuri67' ,
      'database':'books'
}
conn = pymysql.connect(**db_config)
cursor=conn.cursor()
print("connected")

   
st.title('BookScape Explorer :book:')
keyword = st.text_input("Search for books by keyword:")

# Question-specific queries
question = st.selectbox("Select a question:", [
    "1.Check Availability of eBooks vs Physical Books",  
    "2.Find the Publisher with the Most Books Published",   
    "3.Identify the Publisher with the Highest Average Rating",  
    "4.Get the Top 5 Most Expensive Books by Retail Price",  
    "5.Find Books Published After 2010 with at Least 500 Pages",  
    "6.List Books with Discounts Greater than 20%",  
    "7.Find the Average Page Count for eBooks vs Physical Books", 
    "8.Find the Top 3 Authors with the Most Books",  
    "9.List Publishers with More than 10 Books",
    "10.Find the Average Page Count for Each Category", 
    "11.Retrieve Books with More than 3 Authors",  
    "12.Books with Ratings Count Greater Than the Average",  
    "13.Books with the Same Author Published in the Same Year",  
    "14.Books with a Specific Keyword in the Title", 
    "15.Year with the Highest Average Book Price", 
    "16.Count Authors Who Published 3 Consecutive Years", 
    "17.Authors with books published in same year, different publishers", 
    "18.Average retail price of ebooks and physical books",
    "19.Identify Books that are outliers",
    "20.Publisher with the highest average rating (more than 10 books)"
])
if question:
    
    if question=="1.Check Availability of eBooks vs Physical Books":
        st.snow()
        cursor.execute("SELECT is_ebook, COUNT(*) AS book_count FROM book_tables1 GROUP BY is_ebook;")
        data=cursor.fetchall()
        df=pd.DataFrame(data,columns=['is_ebook','book_count'])
        st.dataframe(df)
    if question=="2.Find the Publisher with the Most Books Published":
        st.snow()
        cursor.execute("select publisher, count(*) as book_count from book_tables1 group by publisher order by book_count desc limit 2;")
        data=cursor.fetchall()
        df=pd.DataFrame(data,columns=['publisher','book_count'])
        df_cleaned = df[df['publisher'] != 'None']
        st.dataframe(df_cleaned)
    if question=="3.Identify the Publisher with the Highest Average Rating":
        st.snow()
        cursor.execute("select publisher ,max(average_rating) as avg_rating from book_tables1 group by publisher order by avg_rating desc limit 1;")
        data=cursor.fetchall()
        df=pd.DataFrame(data,columns=['publisher','avg_rating'])
        st.dataframe(df)
    if question=="4.Get the Top 5 Most Expensive Books by Retail Price":
        st.snow()
        cursor.execute("select title, max(retail_price) as highest_price from book_tables1 group by title order by highest_price desc limit 5;")
        data=cursor.fetchall()
        df=pd.DataFrame(data,columns=['title','highest_price'])
        st.dataframe(df)
    if question=="5.Find Books Published After 2010 with at Least 500 Pages":
        st.snow()
        cursor.execute("select title, published_year,page_count from book_tables1 where published_year>2010 and page_count>500;")
        data=cursor.fetchall()
        df=pd.DataFrame(data,columns=['title','published_year','page_count'])
        st.dataframe(df)
    if question=="6.List Books with Discounts Greater than 20%":
        st.snow()
        cursor.execute("SELECT  book_id,title,list_price,retail_price,ROUND(((list_price - retail_price) / list_price) * 100, 2) AS discount_percentage FROM book_tables WHERE list_price > 0 AND ((list_price - retail_price) / list_price) * 100 > 20  ORDER BY discount_percentage DESC;")
        data=cursor.fetchall()
        df=pd.DataFrame(data,columns=['book_id','title','list_price','retail_price','discount_precentage'])
        st.dataframe(df)
    if question=="7.Find the Average Page Count for eBooks vs Physical Books":
        st.snow()
        cursor.execute("select is_ebook,avg(page_count) as avg_page_count from book_tables1 group by is_ebook;")
        data=cursor.fetchall()
        df=pd.DataFrame(data,columns=['is_ebook','avg_page_count'])
        st.dataframe(df)
    if question=="8.Find the Top 3 Authors with the Most Books":
        st.snow()
        cursor.execute("select authors,count(*) as top3author from book_tables1 group by authors order by top3author desc limit 4;")
        data=cursor.fetchall()
        df=pd.DataFrame(data,columns=['authors','top3author'])
        df_cleaned = df[df['authors'] != '']
        st.dataframe(df_cleaned)
    if question=="9.List Publishers with More than 10 Books":
        st.snow()
        cursor.execute("select publisher,count(*) as book_count from book_tables1 group by publisher having book_count>10;")
        data=cursor.fetchall()
        df=pd.DataFrame(data,columns=['publisher','book_count'])
        st.dataframe(df) 
    if question=="10.Find the Average Page Count for Each Category":
        st.snow()
        cursor.execute("select categories ,avg(page_count) from book_tables1 group by categories;")
        data=cursor.fetchall()
        df=pd.DataFrame(data,columns=['categories','avg(page_count)'])
        df_cleaned = df[df['categories'] != '']
        st.dataframe(df_cleaned) 
    if question=="11.Retrieve Books with More than 3 Authors":
        st.snow()
        cursor.execute("select title, count(authors) as author_count from book_tables1 group by authors,title having count(authors)>3;")
        data=cursor.fetchall()
        df=pd.DataFrame(data,columns=['title','author_count'])
        st.dataframe(df)
    if question=="12.Books with Ratings Count Greater Than the Average":
        st.snow()
        cursor.execute("select title , ratings_count from book_tables1 where ratings_count >(select avg(ratings_count) from book_tables1);")
        data=cursor.fetchall()
        df=pd.DataFrame(data,columns=['title','ratings_count'])
        st.dataframe(df)
    if question=="13.Books with the Same Author Published in the Same Year":
        st.snow()
        cursor.execute("SELECT authors, published_year, GROUP_CONCAT(title) AS books FROM book_tables1 GROUP BY authors, published_year HAVING COUNT(*) > 1;")
        data=cursor.fetchall()
        df=pd.DataFrame(data,columns=['authors','published_year','books'])
        df_cleaned = df[df['authors'] != '']
        st.dataframe(df_cleaned) 
    if question=="14.Books with a Specific Keyword in the Title":
        st.snow()
        cursor.execute("select authors ,published_year,count(distinct publisher) from book_tables1 group by authors,published_year having count(distinct publisher)>1;")
        data=cursor.fetchall()
        df=pd.DataFrame(data,columns=['authors','published_year','count(distinct publisher)'])
        df_cleaned = df[df['authors'] != '']
        st.dataframe(df_cleaned) 
    if question=="15.Year with the Highest Average Book Price":
        st.snow()
        cursor.execute("select published_year , avg(retail_price) as avg_price from book_tables1 group by published_year order by avg_price desc limit 1;")
        data=cursor.fetchall()
        df=pd.DataFrame(data,columns=['published_year','avg_price'])
        st.dataframe(df)         
    if question=="16.Count Authors Who Published 3 Consecutive Years":
        st.snow()
        cursor.execute("select published_year,authors ,count(*)  as count_authors from book_tables1 group by published_year , authors having count_authors>=3;")
        data=cursor.fetchall()
        df=pd.DataFrame(data,columns=['published_year','authors','count_authors'])
        df_cleaned = df[df['authors'] != '']
        st.dataframe(df_cleaned) 
    if question=="17.Authors with books published in same year, different publishers":
        st.snow()
        cursor.execute("SELECT authors, published_year, COUNT(DISTINCT publisher) AS publisher_count FROM book_tables1 GROUP BY authors, published_year HAVING publisher_count > 1;")
        data=cursor.fetchall()
        df=pd.DataFrame(data,columns=['authors','published_year','publisher_count'])
        df_cleaned = df[df['authors'] != '']
        st.dataframe(df_cleaned) 
    if question=="18.Average retail price of ebooks and physical books":
        st.snow()
        cursor.execute("SELECT AVG(CASE WHEN is_ebook = 1 THEN retail_Price ELSE NULL END) AS avg_ebook_price,AVG(CASE WHEN is_ebook = 0 THEN retail_Price ELSE NULL END) AS avg_physical_price FROM book_tables1;")
        data=cursor.fetchall()
        df=pd.DataFrame(data,columns=['avg_ebook_price','avg_physical_price'])
        st.dataframe(df)
    if question=="19.Identify Books that are outliers":
        st.snow()
        cursor.execute("SELECT title, average_Rating, ratings_Count FROM book_tables1 WHERE average_Rating > (SELECT AVG(average_Rating) + 2 * STDDEV(average_Rating) FROM book_tables1);")
        data=cursor.fetchall()
        df=pd.DataFrame(data,columns=['title','average_Rating','ratings_Count'])
        st.dataframe(df)
    if question=="20.Publisher with the highest average rating (more than 10 books)":
        st.snow()
        cursor.execute("SELECT publisher, AVG(average_Rating) AS avg_rating FROM book_tables1 GROUP BY publisher HAVING COUNT(*) > 10 ORDER BY avg_rating DESC LIMIT 1;")
        data=cursor.fetchall()
        df=pd.DataFrame(data,columns=['publisher','avg_rating'])
        st.dataframe(df)     
           