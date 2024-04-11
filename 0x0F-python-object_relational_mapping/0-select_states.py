#!/usr/bin/python3
""" Script to display all states from hbtn_0e_0_usa databse """
import MySQLdb
import sys


def display_states(usrname, password, db_name):
    conn = MySQLdb.connect(host="localhost", port=3306, user=usrname,
                           passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()


if (__name__ == "__main__"):
    display_states(sys.argv[1], sys.argv[2], sys.argv[3])
