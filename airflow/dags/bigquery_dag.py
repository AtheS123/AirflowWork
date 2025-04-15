import logging
import sys
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
def bigquery_attempt():
	@task(task_id="use_bigquery")
	def use_bigquery():
		client = bigquery.Client()
		query = """
		    SELECT corpus AS title, COUNT(word) AS unique_words
		    FROM `bigquery-public-data.samples.shakespeare`
		    GROUP BY title
		    ORDER BY unique_words
		    DESC LIMIT 10
		"""
		results = client.query(query)
		for row in results:
			title = row['title']
			unique_words = row['unique_words']
			print(f'{title:<20} | {unique_words}')
		return "finished!"
	
	use_bigquery()

bigquery_attempt()
