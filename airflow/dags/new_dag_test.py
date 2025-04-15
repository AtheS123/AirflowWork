import logging
import os

import pendulum
from airflow.decorators import dag, task

log = logging.getLogger(__name__)

@dag(
	schedule=None,
	start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
	catchup=False,
	tags=["example", "dag_I_made"],
)
def andrew_test_python():
	@task(task_id="print_something")
	def print_a_thing():
		print("hello world!")
		return "run directory: " + os.getcwd()
	
	actually_run = print_a_thing()
	
	actually_run


andrew_test_python()
