#!/usr/bin/python3

'''script that list states passed as arg from the database hbtn_0e_0_usa but
taking care of code injection'''

import MySQLdb
import sys

if __name__ == "__main__":
    try:
        user = sys.argv[1]
        passw = sys.argv[2]
        db = sys.argv[3]
        state_name = sys.argv[4]
        conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                               passwd=passw, db=db, charset="utf8")
        cur = conn.cursor()
        cur.execute("SELECT * FROM states \
                    WHERE name = '%s' ORDER BY id ASC", (state_name))
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()
    except Excpetion as error:
        print("Error with connection to DB")
