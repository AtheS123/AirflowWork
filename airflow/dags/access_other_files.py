import logging
import pendulum
from airflow.decorators import dag, task
import os


log = logging.getLogger(__name__)

@dag(
	schedule=None,
	start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
	catchup=False,
	tags=["example", "dag_I_made"],
)
def andrew_access_files():
	@task(task_id="print_from_files")
	def access_and_print():
		print("hello world!")
		file_dir = os.path.dirname(__file__)
		with os.scandir(file_dir + "/other_python_shenanigans") as scannedfiles:
			for noticed_file in scannedfiles:
				print(noticed_file.name)
				readfile = open(file_dir + "/other_python_shenanigans/" + noticed_file.name)
				print(readfile.read())
		return "this gets returned"
	
	actually_run = access_and_print()
	
	actually_run


andrew_access_files()
