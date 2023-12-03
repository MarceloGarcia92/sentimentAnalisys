#!bin/sh

minikube service $1

kubectl port-forward svc/airflow-webserver 8080:8080 