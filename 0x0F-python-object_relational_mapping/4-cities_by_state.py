#!/usr/bin/python3
""" Script that filters all cities from hbtn_0e_4_usa database """
import MySQLdb
import sys


def display_states(usrname, password, db_name):
    conn = MySQLdb.connect(host="localhost", port=3306, user=usrname,
                           passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    slc = "SELECT cities.id, cities.name, states.name"
    from_join = "FROM cities JOIN states ON cities.state_id = states.id"
    order = "ORDER BY cities.id ASC"
    cur.execute(slc + ' ' + from_join + ' ' + order)
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()


if (__name__ == "__main__"):
    display_states(sys.argv[1], sys.argv[2], sys.argv[3])
