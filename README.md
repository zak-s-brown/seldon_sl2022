# Seldon local development
Setting up Seldon local development on kind

## Prerequisites
- Install [docker](https://docs.docker.com/engine/install/)
- Install [kubectl v1.23.6](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl)
- Install [helm v3](https://helm.sh/): `brew install helm`
- Install [kind](https://kind.sigs.k8s.io/): `brew install kind`
- Install [k9s](https://k9scli.io/): `brew install derailed/k9s/k9s`

## Get started
- `make init`
- `make build-service s=ner`
- `make build-service s=sentiment`
- `make build-service s=rpunct`
- `python test_request.py`

## See it to believe it
[![asciicast](https://asciinema.org/a/J5Ies2TySyE2uWmB8uqW8Q2hZ.svg)](https://asciinema.org/a/J5Ies2TySyE2uWmB8uqW8Q2hZ)


## Prerequesites [DEPRECATED, installed via init]
- Install [istioctl v1.14.1](https://istio.io/latest/docs/setup/getting-started/#download)