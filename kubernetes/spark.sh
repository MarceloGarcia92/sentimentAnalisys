alias k=kuebctl

export SPARK_NAMESPACE="spark-app"
export SPARK_WORKER_NAME="spark-worker"
export SPARK_MASTER_NAME="spark-master"

export SPARK_MASTER_POD_NAME=$(k get pods \
    --namespace "$SPARK_NAMESPACE" \
    --selector="app=$SPARK_MASTER_NAME" \
    --output jsonpath='{.items[0].metadata.name}')

export SPARK_WORKER_POD_NAME=$(k get pods \
    --namespace "$SPARK_NAMESPACE" \
    --selector="name=$SPARK_WORKER_NAME" \
    --output jsonpath='{.items[0].metadata.name}')