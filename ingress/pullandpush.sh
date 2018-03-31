docker pull quay.io/kubernetes-ingress-controller/nginx-ingress-controller:0.12.0
docker tag quay.io/kubernetes-ingress-controller/nginx-ingress-controller:0.12.0 harbor.pks.pcfdemo.com/demo/defaultbackend:1.4
docker push harbor.pks.pcfdemo.com/demo/nginx-ingress-controller:0.12.0


docker pull gcr.io/google_containers/defaultbackend:1.4
docker push harbor.pks.pcfdemo.com/demo/defaultbackend:1.4
docker tag gcr.io/google_containers/defaultbackend:1.4 harbor.pks.pcfdemo.com/demo/nginx-ingress-controller:0.12.0


kubectl apply -f namespace.yaml
kubectl apply -f default-backend.yaml
kubectl apply -f configmap.yaml
kubectl apply -f tcp-services-configmap.yaml
kubectl apply -f udp-services-configmap.yaml
kubectl apply -f rbac.yaml
kubectl apply -f with-rbac.yaml
