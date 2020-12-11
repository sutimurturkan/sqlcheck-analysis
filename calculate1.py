import os, glob
import sqlcheck
from sqlcheck.checker import identify_anti_patterns
import sqlite3

# DB filepath
dbFilepath = 'benchmark_v1.db'

def main():
	try:
		true_positives = 0
		false_positives = 0
		true_negatives = 0
		false_negatives = 0

		connection = sqlite3.connect(dbFilepath)
		cursor = connection.cursor()
		print("Connected to SQLite")
		sqlite_select_detect = """SELECT DETECTED_BY_SQLCHECK from SQLCheck_Benchmark_v1"""
		cursor.execute(sqlite_select_detect)
		elements = [i[0] for i in cursor.fetchall()]
		for element in elements:
                    if (element == "True Positive"):
                    	true_positives+= 1
                    elif (element == "False Positive"):
                    	false_positives+= 1
                    elif (element == "True Negative"):
                    	true_negatives+= 1
                    else:
                    	false_negatives+= 1
		print("Total queries are:  ", len(elements))
		print("True Positives: ", true_positives)
		print("False Positives: ", false_positives)
		print("True Negatives: ", true_negatives)
		print("False Negatives: ", false_negatives)
		recall = true_positives / (true_positives + false_negatives)
		precision = true_positives / (true_positives + false_positives)
		accuracy = (true_positives + true_negatives) / (true_positives + true_negatives + false_positives + false_negatives)
		print("Precision: ", precision, "Recall: ", recall, "Accuracy: ", accuracy)
		cursor.close()
	except sqlite3.Error as error:
		print("Failed to read data from table", error)
	finally:
		if (connection):
			connection.close()
			print("The Sqlite connection is closed")

if __name__ == "__main__":
    main()
