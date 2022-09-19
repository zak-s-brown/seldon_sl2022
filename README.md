# Seldon local development
Setting up Seldon local development on kind

## Prerequisites
- Install [docker](https://docs.docker.com/engine/install/)
- Install [kubectl v1.23.6](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl)
- Install [helm v3](https://helm.sh/): `brew install helm`
- Install [kind](https://kind.sigs.k8s.io/): `brew install kind`
- Install [k9s](https://k9scli.io/): `brew install derailed/k9s/k9s`
- Install python 3.x + `requests` library (for testing endpoint)

## Get started
- `make init` (setup kind cluster, install istio, install seldon)
- `make build-all` (build & deploy ner, sentiment, punct, and complex execution graph)
- `make f` (establish port forward, `make kf` to terminate this background process)
- `python test_request.py all` (test requests to all of the services, including complex execution graph) 
