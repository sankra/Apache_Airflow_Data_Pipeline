from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

datasets = ['sales', 'marketing', 'finance']

def process_dataset(ds_name):
    print(f"Processing dataset: {ds_name}")

for ds in datasets:
    dag = DAG(
        dag_id=f'process_{ds}_dag',
        start_date=datetime(2023, 1, 1),
        schedule_interval='@daily',
        catchup=False
    )

    with dag:
        task = PythonOperator(
            task_id=f'process_{ds}',
            python_callable=process_dataset,
            op_args=[ds]
        )

    globals()[dag.dag_id] = dag
