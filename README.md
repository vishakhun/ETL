# Mars Weather Data Aggregation Pipeline

## Project Overview
This project demonstrates an ETL pipeline that utilizes NASA's InSight lander API to fetch Mars weather data, processes the data using Apache Spark, and schedules the workflow with Apache Airflow. It serves as a practical example of how to integrate various data engineering tools and techniques.

## Objectives
- To fetch Mars weather data from NASA's InSight API.
- To process and aggregate the data using Apache Spark for meaningful insights.
- To schedule and automate the ETL tasks using Apache Airflow.

## Technology Stack
- **Python**: The core programming language used for scripting.
- **Requests**: A Python library used for HTTP requests to fetch data from the NASA API.
- **Apache Spark**: A powerful analytics engine for big data processing.
- **Apache Airflow**: A platform to programmatically author, schedule, and monitor workflows.

## Project Structure
- `data_fetching/fetch_data.py`: Contains the script to fetch data from the NASA API.
- `data_processing/process_data.py`: Contains the Spark job for data processing and aggregation.
- `airflow_dags/mars_weather_dag.py`: Contains the Airflow DAG for scheduling and automating the ETL pipeline.
- `requirements.txt`: Lists all the necessary Python dependencies.
