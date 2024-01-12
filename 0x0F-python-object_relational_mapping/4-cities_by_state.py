#!/usr/bin/python3
"""
This script connects to a MySQL server,
retrieves all cities from a specific database,
and prints the results ordered by state ID.
"""

import MySQLdb
from sys import argv


def main():
    """Main function to execute the script."""
    db = MySQLdb.connect(host="localhost",
                         port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")
    cities = cursor.fetchall()
    for city in cities:
        print(city)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
