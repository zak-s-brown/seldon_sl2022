#!/bin/bash

svc=$1
echo "Building Service" $svc 
cd ./services/$svc/
docker build -t $svc:latest .

echo "Tagging and Deploying"
cd ../../
docker tag $svc:latest localhost:5001/$svc:latest && \
docker push localhost:5001/$svc:latest && \
kubectl apply -f k8s/$svc-deploy.yml