#!/usr/bin/python3

"""
Display states in database by ascending id order that match request
   and protects against SQL injections
   Script should take 4 arguments:
   mysql username, mysql-password, database-name, state-name
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    with MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    ) as conn:
        with conn.cursor() as cur:
            query = """SELECT * FROM states WHERE name = %s
            ORDER BY states.id ASC"""
            cur.execute(query, (sys.argv[4],))
            query_rows = cur.fetchall()
            for row in query_rows:
                print(row)
