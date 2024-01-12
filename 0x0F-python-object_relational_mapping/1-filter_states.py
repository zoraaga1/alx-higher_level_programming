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
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
