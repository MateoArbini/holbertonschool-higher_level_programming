#!/usr/bin/python3

'''script that lists all cities from a state the database hbtn_0e_4_usa'''

import MySQLdb
import sys

if __name__ == "__main__":
    try:
        user = sys.argv[1]
        passw = sys.argv[2]
        db = sys.argv[3]
        state = sys.argv[4]
        text = ""
        cont = 0
        conn = MySQLdb.connect(host="localhost", port=3306, user=f"{user}",
                               passwd=f"{passw}", db=f"{db}", charset="utf8")
        cur = conn.cursor()
        cur.execute("SELECT cities.name FROM cities WHERE state_id = (SELECT \
                    states.id FROM states WHERE states.name = '%s' \
                    ORDER BY cities.id ASC)" % (state))
        query_rows = cur.fetchall()
        for row in query_rows:
            cont += 1
            if cont < len(query_rows):
                text += row[0]+', '
            else:
                text += row[0]
        print(text)
        cur.close()
        conn.close()
    except (Excepction) as error:
        print("Error with connection to DB")
