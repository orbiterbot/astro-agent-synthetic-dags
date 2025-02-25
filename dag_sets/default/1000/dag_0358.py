from datetime import datetime, timedelta

from airflow.models import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dag_0358",
    start_date=datetime(2021, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    task_000 = EmptyOperator(task_id="task_000")
    task_001 = EmptyOperator(task_id="task_001")
    task_002 = EmptyOperator(task_id="task_002")
    task_003 = EmptyOperator(task_id="task_003")
    task_004 = EmptyOperator(task_id="task_004")

    task_000 >> task_001    task_001 >> task_002    task_002 >> task_003    task_003 >> task_004
