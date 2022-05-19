import sqlite3

import pymysql
def connection():
    connection = pymysql.connect(
        host = "localhost",
        user="root",
        password = "",
        db = "bd"   
    )
    return connection
    
   
    