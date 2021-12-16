#!/usr/bin/python3

'''
Display states in database by ascending id order
'''

if __name__ == '__main__':
    
    import sys
    import MySQLdb

    if len(sys.argv) > 3:
        with MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8") as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT * FROM states ORDER BY states.id ASC""")
                query_rows = cur.fetchall()
                for row in query_rows:
                    print(row)
