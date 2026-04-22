from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="news_pipeline",
    start_date=datetime(2024,1,1),
    schedule="@daily",
    catchup=False,
    tags=["news"]
) as dag:

    extract = BashOperator(
        task_id="extract",
        bash_command="python /opt/airflow/scripts/extract_news.py"
    )

    transform = BashOperator(
        task_id="transform",
        bash_command="python /opt/airflow/scripts/transform_news.py"
    )

    load = BashOperator(
        task_id="load",
        bash_command="python /opt/airflow/scripts/load_snowflake.py"
    )

    extract >> transform >> load