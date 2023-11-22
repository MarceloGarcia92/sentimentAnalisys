#DOCKER
docker build -t mgarcia92/mlflow:v1 /Users/marcelogarciacastillo/Documents/Projects/Bills/Bills/kubernetes/mlflow
docker push mgarcia92/mlflow:v1 
docker run --name mlflow-serv mgarcia92/mlflow:v1

#KUBERNETES
alias k=kubectl
export do='--dry-run=client -o yaml'
k create -f /Users/marcelogarciacastillo/Documents/Projects/Bills/Bills/kubernetes/mlflow/mlflow-pod.yaml
k expose pod mlflow --port=5000 --target-port=5000 --name=mlflow-svc