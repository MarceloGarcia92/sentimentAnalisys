#git clone -b main  https://github.com/airflow-helm/charts.git

#k create ns airflow

## set the release-name & namespace
export AIRFLOW_NAME="airflow-cluster"
export AIRFLOW_NAMESPACE="airflow"

## create the namespace
kubectl create ns "$AIRFLOW_NAMESPACE"

## install using helm 3
helm install \
  "$AIRFLOW_NAME" \
  airflow-stable/airflow \
  --namespace "$AIRFLOW_NAMESPACE" \
  --version "8.X.X" \
  --values ./docker/charts/charts/airflow/values.yaml
  
## wait until the above command returns and resources become ready 
## (may take a while)
#kubectl wait --for=condition=ready pod \
#  --namespace "$AIRFLOW_NAMESPACE" \
#  --selector="app.kubernetes.io/name=airflow,app.kubernetes.io/instance=$AIRFLOW_NAME" \
#  --timeout=360s

## get the airflow webserver pod name 
export AIRFLOW_POD_NAME=$(kubectl get pods \
  --namespace "$AIRFLOW_NAMESPACE" \
 --selector="app.kubernetes.io/name=airflow,app.kubernetes.io/instance=$AIRFLOW_NAME" \
 --output jsonpath='{.items[0].metadata.name}')

## port-forward the airflow webserver pod to localhost
#kubectl port-forward \
#  --namespace "$AIRFLOW_NAMESPACE" \
#  "$AIRFLOW_POD_NAME" \
#  8080:8080

## open the airflow UI in your browser
#open http://localhost:8080

