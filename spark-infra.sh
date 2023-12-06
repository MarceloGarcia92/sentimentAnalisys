helm repo add spark-operator https://googlecloudplatform.github.io/spark-on-k8s-operator

helm install spark-release spark-operator/spark-operator --namespace spark-operator --create-namespace --set webhook.enable=true


helm status --namespace spark-operator spark-release

## Security
kubectl create namespace spark-apps
kubectl create serviceaccount spark --namespace=spark-apps
kubectl create clusterrolebinding spark-role --clusterrole=edit --serviceaccount=spark-apps:spark --namespace=spark-apps

helm install spark-release spark-operator/spark-operator --namespace spark-operator --create-namespace --set sparkJobNamespace=spark-apps
