import textwrap
from datetime import datetime, timedelta
from airflow.modules.dag import DAG
from airflow.operators.bash import BashOperator

with DAG(
	"tutorial",
	default_args={
		"depends_on_past": False,
		"email": ["airflow@example.com"],
		"email_on_failure": False,
		"email_on_retry": False,
		"retries": 1,
		"retry_delay": timedelta(minutes=5),
	},
	description="My Testing DAG",
	schedule=timedelta(days=1),
	start_date=datetime(2025, 1, 21),
	catchup=False,
	tags=["example"],
) as dag:

	t1 = BashOperator(
		task_id="print_date",
		bash_command="date",
	)
