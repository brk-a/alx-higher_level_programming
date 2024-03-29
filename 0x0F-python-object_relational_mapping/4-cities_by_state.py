#!/usr/bin/python3

"""
Lists all cities from the database
   and protects against SQL injections
   Script should take 3 arguments:
   mysql username, mysql-password, database-name
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
            query = """SELECT cities.id, cities.name, states.name FROM cities
            INNER JOIN states ON cities.state_id = states.id
            ORDER BY id ASC;"""
            cur.execute(query)
            query_rows = cur.fetchall()
            for row in query_rows:
                print(row)
