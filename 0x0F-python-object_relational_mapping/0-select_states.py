#!/usr/bin/python3

'''script that lists all states from the database hbtn_0e_0_usa'''

import MySQLdb
import sys

if __name__ == "__main__":
    try:
        user = sys.argv[1]
        passw = sys.argv[2]
        db = sys.argv[3]
        conn = MySQLdb.connect(host="localhost", port=3306, user=f"{user}",
                               passwd=f"{passw}", db=f"{db}", charset="utf8")
        cur = conn.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()
    except Excepctions:
        print("Error with connection to DB")
