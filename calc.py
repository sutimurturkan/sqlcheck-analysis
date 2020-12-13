import os, glob
import sqlcheck
from sqlcheck.checker import identify_anti_patterns
import sqlite3

# DB filepath
dbFilepath = 'benchmark_v1.db'


def get_calculations(results, predicted):
	tp = 0
	fp = 0
	tn = 0
	fn = 0
	for (res, pred) in zip(results, predicted):
		if (res == pred and res == 'YES'):
			tp+=1
		elif (res == pred and res == 'NO'):
			tn+=1
		elif (res == 'YES' and pred == 'NO'):
			fp+=1
		else:
			fn+=1
	recall = tp / (tp + fn)
	precision = tp / (tp + fp)
	accuracy = (tp + tn) / (tp + tn + fp + fn)
	calc = [recall, precision, accuracy]
	return calc

def main():
	try:
		connection = sqlite3.connect(dbFilepath)
		cursor = connection.cursor()
		print("Connected to SQLite")
		sqlite_select_detect = """SELECT DETECTED_BY_V1 from SQLCheck_Benchmark_v1"""
		cursor.execute(sqlite_select_detect)
		v1_results = [i[0] for i in cursor.fetchall()]
		sqlite_select_detect = """SELECT DETECTED_BY_V2 from SQLCheck_Benchmark_v1"""
		cursor.execute(sqlite_select_detect)
		v2_results = [i[0] for i in cursor.fetchall()]
		sqlite_select_detect = """SELECT EXPECTED_RESULT from SQLCheck_Benchmark_v1"""
		cursor.execute(sqlite_select_detect)
		predicted = [i[0] for i in cursor.fetchall()]
		cursor.close()
		v1_calc = get_calculations(v1_results, predicted)
		v2_calc = get_calculations(v2_results, predicted)
		print(v1_calc, v2_calc)


	except sqlite3.Error as error:
		print("Failed to read data from table", error)
	finally:
		if (connection):
			connection.close()
			print("The Sqlite connection is closed")

if __name__ == "__main__":
    main()
