import logging
import sys
import os
import pendulum
from google.cloud import bigquery
from airflow.decorators import dag, task

log = logging.getLogger(__name__)

@dag(
	schedule=None,
	start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
	catchup=False,
	tags=["dag_I_made"]
)
def run_external_queries():
	@task(task_id="use_bigquery")
	def use_bigquery():
		client = bigquery.Client()
		currentdir = os.path.dirname(__file__)
		with os.scandir(currentdir + "/queries") as scannedfiles:
			for foundfile in scannedfiles:
				query = open(currentdir + "/queries/" + foundfile.name)
				results = client.query(query.read())
				for row in results:
					print(row['result'])
				query.close()
		return "finished!"
	
	use_bigquery()

run_external_queries()
