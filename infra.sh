helm repo add spark-operator https://googlecloudplatform.github.io/spark-on-k8s-operator

helm install spark-release spark-operator/spark-operator --namespace spark-operator --create-namespace --set webhook.enable=true


helm status --namespace spark-operator spark-release