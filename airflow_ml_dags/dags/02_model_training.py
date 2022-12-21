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
    '02_model_training',
    default_args=default_args,
    description='Download/preproccessing/splitting data. Train/save model.',
    schedule_interval="@weekly",
    start_date=days_ago(2),
) as dag:

    files = DockerOperator(
        image='airflow-preprocess-files',
        task_id='data-downloading',
        network_mode='bridge',
        do_xcom_push=False,
        mounts=[
            Mount(
                source="/home/ivan/'Рабочий стол'/Techno_2sem/MLOps/HW_MLOps/airflow_ml_dags/data",
                target='/data',
                type='bind',
                )],
        command='--in_path /data/raw/{{ ds }} --tmp_path /data/tmp/{{ ds }}',
    )

    preprocessing = DockerOperator(
        image='airflow-preprocess',
        task_id='preprocessing',
        network_mode='bridge',
        do_xcom_push=False,
        mounts=[
            Mount(
                source="/home/ivan/'Рабочий стол'/Techno_2sem/MLOps/HW_MLOps/airflow_ml_dags/data",
                target='/data',
                type='bind',
                )],
        command='--scaler_path /data/models/{{ ds }}\
                 --tmp_path /data/tmp/{{ ds }}\
                 --preprocess_path /data/preprocessed/{{ ds }}',
    )

    split = DockerOperator(
        image='airflow-split',
        task_id='data-splitting',
        network_mode="bridge",
        do_xcom_push=False,
        mounts=[
            Mount(
                source="/home/ivan/'Рабочий стол'/Techno_2sem/MLOps/HW_MLOps/airflow_ml_dags/data",
                target='/data',
                type='bind',
                )],
        command='--preprocessed_path /data/preprocessed/{{ ds }}\
                 --splitted_path /data/splitted/{{ ds }}\
                 --test_size 0.15\
                 --random_state 42',
    )

    train = DockerOperator(
        image='airflow-train',
        task_id='model-training',
        network_mode="bridge",
        do_xcom_push=False,
        mounts=[
            Mount(
                source="/home/ivan/'Рабочий стол'/Techno_2sem/MLOps/HW_MLOps/airflow_ml_dags/data",
                target='/data',
                type='bind',
                )],
        command='--load_data_path /data/splitted/{{ ds }}\
                 --save_model_path /data/models/{{ ds }}',
    )

    validation = DockerOperator(
        image='airflow-validation',
        task_id='model-validation',
        network_mode='bridge',
        do_xcom_push=False,
        mounts=[
            Mount(
                source="/home/ivan/'Рабочий стол'/Techno_2sem/MLOps/HW_MLOps/airflow_ml_dags/data",
                target='/data',
                type='bind',
                )],
        command='--validation_path /data/splitted/{{ ds }}\
                 --metrics_path /data/models/{{ ds }}\
                 --model_path /data/models/{{ ds }}',
    )

    files >> preprocessing >> split >> train >> validation
