#coding=utf-8
import MySQLdb

connection = MySQLdb.connect(user='root', passwd='920816', db='demosite')
cursor = connection.cursor()
cursor.execute("SELECT title FROM demosite_links ")

for row in cursor.fetchall():
    print  row[0]

connection.close()