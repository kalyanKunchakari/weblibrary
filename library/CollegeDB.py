import sqlite3
import os
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_librarian_table(conn, table_sql):
    sql_create_librarian_table = """ CREATE TABLE IF NOT EXISTS librarian (
                                        empid integer PRIMARY KEY,
                                        name text NOT NULL,
                                        email_id text,
                                        doj text NOT NULL
                                    );"""
    try:
        c  = conn.cursor()
        c.execute(sql_create_librarian_table)   
        sql = ''' INSERT INTO librarian(empid,name,email_id,doj)
              VALUES(?,?,?,?) '''
        c.execute(sql, table_sql)    
        conn.commit() 
        print("records inserted")        
    except Error as e:
        print(e)

def create_student_table(conn, table_sql):
    sql_create_student_table = """ CREATE TABLE IF NOT EXISTS student (
                                        stdid integer PRIMARY KEY,
                                        name text NOT NULL,
                                        email_id text,
                                        degree text NOT NULL,
                                        branch text NOT NULL,
                                        persuing_year text NOT NULL,
                                        doj text NOT NULL
                                    );"""
    try:
        c  = conn.cursor()
        c.execute(sql_create_student_table)   
        sql = ''' INSERT INTO student(stdid, name, email_id, degree, branch, persuing_year, doj)
              VALUES(?,?,?,?,?,?,?) '''
        c.execute(sql, table_sql)
        conn.commit()
        print("records inserted")        
    except Error as e:
        print(e)      

def main():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    database = os.path.join(BASE_DIR, 'db.sqlite3')                                    
    conn = create_connection(database)
    if conn :
        s1 = (101, "kalyan", "kalyan.kunchakari@jb.com", "Btech", "IT", "3 rd year", "2019")
        s2 = (102, "Anusha", "Anusha.puli@jb.com", "Btech", "Electronics Engineering", "4 th year", "2018")
        s3 = (103, "Akshaj", "Akshaj.kunchakari@jb.com", "Mtech", "Machine Learning", "1 st year", "2017")
        a1 = (201, "Navin", "navin.g@jb.com", "2010")
        create_student_table(conn, s1)
        create_student_table(conn, s2)
        create_student_table(conn, s3)
        create_librarian_table(conn, a1)
    else:
        print("Error creating the tables verify again and create it") 

if __name__ == '__main__':
    main()        