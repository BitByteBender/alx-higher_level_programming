#!/usr/bin/python3
""" Script that filters all cities by state from hbtn_0e_4_usa database """
import MySQLdb
import sys


def display_states(usrname, password, db_name, st_name):
    conn = MySQLdb.connect(host="localhost", port=3306, user=usrname,
                           passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    slc = "SELECT cities.name"
    inner_join = "FROM cities INNER JOIN states ON cities.state_id=states.id"
    where = "WHERE states.name=%s"
    qry = slc + ' ' + inner_join + ' ' + where
    cur.execute(qry, (st_name,))
    query_rows = cur.fetchall()

    cities = [row[0] for row in query_rows]

    print(", ".join(cities))

    cur.close()
    conn.close()


if (__name__ == "__main__"):
    display_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
