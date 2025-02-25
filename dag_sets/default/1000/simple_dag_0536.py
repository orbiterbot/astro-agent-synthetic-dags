"""
Simple DAG with a configurable parse delay.
This DAG is automatically generated for performance testing.
"""
import time
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.empty import EmptyOperator

# Simulate parse delay
time.sleep(0.07668980983562408)

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "simple_dag_0536",
    default_args=default_args,
    description="A simple DAG with 0.07668980983562408 seconds parse delay",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["generated", "performance_test"],
) as dag:
    
    start = EmptyOperator(task_id="start")
    
    # Create a small chain of tasks
    previous_task = start
    for i in range(1, 6):
        task = EmptyOperator(task_id=f"task_{i}")
        previous_task >> task
        previous_task = task
    
    end = EmptyOperator(task_id="end")
    previous_task >> end 