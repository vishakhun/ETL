from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'mars_weather_etl',
    default_args=default_args,
    description='ETL pipeline for Mars weather data',
    schedule_interval='@daily',
)

def fetch_data():
    """
    Airflow task to fetch Mars weather data.
    """
    # Assuming the script is in the same directory as the DAG file
    exec(open("data_fetching/fetch_data.py").read())

def process_data():
    """
    Airflow task to process the fetched Mars weather data.
    """
    # Assuming the script is in the same directory as the DAG file
    exec(open("data_processing/process_data.py").read())

fetch_task = PythonOperator(
    task_id='fetch_mars_weather',
    python_callable=fetch_data,
    dag=dag,
)

process_task = PythonOperator(
    task_id='process_mars_weather',
    python_callable=process_data,
    dag=dag,
)

fetch_task >> process_task
