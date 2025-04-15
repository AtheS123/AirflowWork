import os
import logging
import pendulum
import sys

from datetime import timedelta
from google.cloud import bigquery
from airflow.decorators import dag, task

# Set the log
log = logging.getLogger(__name__)

# Dag info
@dag(
	schedule=None,
	start_date=pendulum.datetime(2025,1,1,tz="UTC"),
	catchup=False,
	tags=["dag_I_made"],
) # Actual DAG
def check_queries():
	# Establish which directory to grab the query from
	currentdir = os.path.dirname(__file__)
	querylist = os.scandir(os.path.join(currentdir, "queries"))
	client = bigquery.Client()
	
	# The base task function (used for query in the folder)
	@task
	def individual_query_check(queryfile):
		openedfile = open(queryfile.path)
		results = client.query(openedfile.read())
		# Raise exception (fail the task) if the query returns rows
		if results.result().total_rows > 0:
			raise Exception("Query returned rows")
		return "success"
	
	# Make a task for each query in the query folder
	for foundfile in querylist:
		ran_query = individual_query_check.override(task_id=f"{foundfile.name}")(foundfile)
		ran_query
	
check_queries()
