import os, glob
import sqlcheck
from sqlcheck.checker import identify_anti_patterns_v2
import sqlite3


# DB filepath
dbFilepath = 'benchmark_v1.db'

def get_antipatterns(query):
    if identify_anti_patterns_v2(query) !={}:
        ap = identify_anti_patterns_v2(query)
        print(ap)
        print("----------------")

def main():
	try:
		connection = sqlite3.connect(dbFilepath)
		cursor = connection.cursor()
		print("Connected to SQLite")
		sqlite_select_query = """SELECT QUERIES from SQLCheck_Benchmark_v1"""
		cursor.execute(sqlite_select_query)
		queries = [i[0] for i in cursor.fetchall()]

		for query in queries:
			try:
				get_antipatterns(query)
			except:
				pass

		print("Total queries are:  ", len(queries))

		cursor.close()
	except sqlite3.Error as error:
		print("Failed to read data from table", error)
	finally:
		if (connection):
			connection.close()
			print("The Sqlite connection is closed")

if __name__ == "__main__":
    main()
