FROM python:3.8-slim-buster

ENV AIRFLOW_HOME /usr/local/airflow

RUN pip install apache-airflow 
#&& pip install apache-airflow-providers-apache-spark

ENTRYPOINT ["airflow"]

CMD ["webserver"]

#CMD ["airflow","airflow", "webserver", "--port", "8080"]

##########
#FROM python:3.8-slim-buster

#ENV AIRFLOW_HOME /opt/airflow/
#ENV AIRFLOW__CORE__DAGS_FOLDER=/opt/airflow/dags
#ENV AIRFLOW__CORE__EXECUTOR = KubernetesExecutor
#ENV AIRFLOW__CORE__LOAD_EXAMPLES = False


#RUN pip install apache-airflow && \
# pip install apache-airflow-providers-apache-spark && \
# pip install apache-airflow-providers-cncf-kubernetes

#EXPOSE 8080

#CMD ["airflow","airflow", "webserver", "--port", "8080"]