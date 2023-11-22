#!bin/bash

cp airflow/dags/$1.py /Users/marcelogarciacastillo/airflow/dags
cp -r src /Users/marcelogarciacastillo/airflow/dags
echo $1 has been moved

#airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin
