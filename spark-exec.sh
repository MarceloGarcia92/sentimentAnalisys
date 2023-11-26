spark-submit \
    --master k8s://https://<k8s-master-url> \
    --deploy-mode cluster \
    --name spark-example \
    --class org.example.YourMainClass \
    --conf spark.executor.instances=2 \
    --conf spark.kubernetes.container.image=<your-spark-image> \
    --conf spark.kubernetes.namespace=default \
    --conf spark.kubernetes.authenticate.driver.serviceAccountName=spark \
    local:///path/to/your-app.jar