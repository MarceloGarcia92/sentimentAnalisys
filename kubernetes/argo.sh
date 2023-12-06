export ARGO_WORKFLOWS_VERSION=v3.5.2

kubectl create namespace argo

kubectl apply -n argo -f https://github.com/argoproj/argo-workflows/releases/download/$ARGO_WORKFLOWS_VERSION/install.yaml

kubectl patch deployment \
  argo-server \
  --namespace argo \
  --type='json' \
  -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/args", "value": [
  "server",
  "--auth-mode=server"
]}]'