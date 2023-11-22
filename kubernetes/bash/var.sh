export NODE_PORT=$(kubectl get services/$1 -o go-template='{{(index .spec.ports 0).nodePort}}')
echo NODE_PORT=$NODE_PORT