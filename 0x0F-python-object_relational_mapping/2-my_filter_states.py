#!/usr/bin/python3
""" Script that filters all states from hbtn_0e_0_usa database """
import MySQLdb
import sys


def display_states(usrname, password, db_name, st_name):
    conn = MySQLdb.connect(host="localhost", port=3306, user=usrname,
                           passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    qry = "SELECT * FROM states WHERE name LIKE BINARY '{}'"
    cur.execute(qry.format(st_name))
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()


if (__name__ == "__main__"):
    display_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
