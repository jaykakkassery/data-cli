import sys
import mysql.connector
import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-d','--db', help='Provide database name', default='testdb')
    parser.add_argument('-t','--table', help='Provide table name', default='employee')
    args = parser.parse_args()
    dbname = args.db
    mydb = mysql.connector.connect(host="localhost", user="root", database=dbname)
    mycrusor = mydb.cursor()
    querystring = f'select * from {args.table}'
    print(querystring)
    mycrusor.execute(querystring)
    myresult = mycrusor.fetchall()
    for row in myresult:
        print(row)
    
if __name__ == '__main__':
    main()