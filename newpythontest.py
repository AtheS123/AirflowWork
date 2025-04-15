import os
from google.cloud import bigquery

currentdir = os.path.dirname(__file__)
client = bigquery.Client()

with os.scandir(os.path.join(currentdir, "querytest")) as scannedfiles:
	for foundfile in scannedfiles:
		query = open(foundfile.path)
		results = client.query(query.read())
		print(foundfile.name)
		if results.result().total_rows > 0:
			print("Returned rows")
		print()
		query.close()
