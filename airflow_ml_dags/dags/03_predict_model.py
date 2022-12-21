from datetime import timedelta

# The DAG object
from airflow import DAG

# Operators
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from docker.types import Mount


default_args = {
    'owner': 'airflow',
    'email': ['airflow@example.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    '03_predict_model',
    default_args=default_args,
    description='Make a predict',
    schedule_interval="@daily",
    start_date=days_ago(2),
) as dag:

    predict = DockerOperator(
        image='airflow-predict',
        task_id='model-prediction',
        network_mode="bridge",
        do_xcom_push=False,
        mounts=[
            Mount(
                source="/home/ivan/'Рабочий стол'/Techno_2sem/MLOps/HW_MLOps/airflow_ml_dags/data",
                target='/data',
                type='bind',
                )],
        command='--input_path /data/splitted/{{ ds }}\
                 --pred_path /data/predictions/{{ ds }}\
                 --scaler_path /data/models/{{ ds }}\
                 --model_path /data/models/{{ ds }}',
    )

    predict
