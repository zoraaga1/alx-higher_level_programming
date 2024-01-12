#!/usr/bin/python3
"""
This script connects to a MySQL server,
retrieves all states from a specific database,
only states strats with N,
and prints the results ordered by state IDs.
"""

import MySQLdb
from sys import argv


def main():
    """Main function to execute the script."""
    db = MySQLdb.connect(host="localhost",
                         port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in cur.fetchall() if state[1][0] == "N"]

if __name__ == "__main__":
    main()
