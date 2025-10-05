import time
import datetime
from airflow.sdk import DAG, task

with DAG(
    dag_id="example_dag",
    start_date=datetime.datetime(2021, 1, 1),
    schedule="@daily"
)as dag:
    @task
    def hello_world():
        time.sleep(5)
        print('Hello world, from Airflow!')
    
    @task
    def bye_world():
        time.sleep(5)
        print('Goodbye world, from Airflow!')
    
    hello_world() >> bye_world()