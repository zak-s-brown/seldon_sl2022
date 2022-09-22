CERT_VERSION=v1.8.0
ISTIO_VERSION=1.14.1
SELDON_VERSION=1.14.0
service:=$(s)
reg_name='kind-registry'
reg_port='5001'



.PHONY: init
init: helm_add_repo init_kind install_metrics install_cert_manager install_istio install_seldon install_gateway

.PHONY: helm_add_repo
helm_add_repo:
	helm repo add jetstack https://charts.jetstack.io
	helm repo add seldonio https://storage.googleapis.com/seldon-charts
	helm repo update

.PHONY: init_kind
init_kind:
	#kind create cluster --config ./k8s/cluster-config.yml
	bash init_kind.sh

.PHONY: tag 
tag: 
	docker tag $(service):latest localhost:5001/$(service):latest && \
	docker push localhost:5001/$(service):latest

.PHONY:  install_metrics
install_metrics:
	kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

.PHONY: install_cert_manager
install_cert_manager:
	kubectl create namespace cert-manager && \
	helm upgrade --install \
	cert-manager jetstack/cert-manager \
	--namespace cert-manager \
	--version $(CERT_VERSION) \
	--set installCRDs=true

.PHONY: install_istio
install_istio:
	curl -L https://istio.io/downloadIstio | ISTIO_VERSION=$(ISTIO_VERSION) TARGET_ARCH=$(uname -a|awk '{print $15}') sh -
	cd istio-$(ISTIO_VERSION) &&\
	./bin/istioctl install --set profile=demo --set values.gateways.istio-ingressgateway.type=NodePort -y &&\
	kubectl label namespace default istio-injection=enabled

.PHONY: install_gateway
install_gateway: 
	kubectl apply -f k8s/istio-gateway.yml
	

.PHONY: install_istio_via_helm
install_istio_via_helm:
	kubectl create namespace istio-system
	helm install istio-base istio/base --version $(ISTIO_VERSION) -n istio-system
	helm install istiod istio/istiod --version $(ISTIO_VERSION) -n istio-system
	helm install gateway istio/gateway --version $(ISTIO_VERSION) -n istio-system

.PHONY: install_seldon
install_seldon:
	kubectl create namespace seldon-system
	helm upgrade --install seldon-core seldon-core-operator \
	--repo https://storage.googleapis.com/seldon-charts \
	--set ambassador.enabled=false \
	--set usageMetrics.enabled=true \
	--set certManager.enabled=true \
	--set istio.enabled=true \
	--version $(SELDON_VERSION) \
	--namespace seldon-system

.PHONY: iris
iris:
	kubectl create namespace seldon
	kubectl apply -f k8s/iris-deploy.yml

.PHONY: f
f:
	#nohup kubectl port-forward svc/seldon-d0934233541ef6b732c88680f8a0e94f 9000:9000 -n seldon >/dev/null 2>&1 & 
	nohup kubectl port-forward -n istio-system svc/istio-ingressgateway 8080:80 >/dev/null 2>&1 & 

.PHONY: kf
kf:
	pkill kubectl

.PHONY: build-service
build-service: 
	echo "Building Service:" $(service) && \
	bash build_service.sh $(service)

	
.PHONY: build-all
build-all: 
	echo "Building Service:" ner && \
	bash build_service.sh ner && \
	echo "Building Service:" sentiment && \
	bash build_service.sh sentiment && \
	echo "Building Service:" rpunct && \
	bash build_service.sh rpunct && \
	echo "Building Service:" combiner && \
	bash build_service.sh combiner && \
	kubectl apply -f k8s/serial-rpunct-ner.yml && \
	kubectl apply -f k8s/complex-rpunct-ner-sentiment.yml

.PHONY: test
test:
	python test_request.py $(service)

.PHONY: clean
clean:
	kind delete cluster --name seldon
	rm -rf istio-$(ISTIO_VERSION)
