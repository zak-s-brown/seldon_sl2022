# Seldon local development
Setting up Seldon local development on kind

## Prerequisites
- Install [docker](https://docs.docker.com/engine/install/)
- Install [kubectl v1.23.6](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl)
- Install [istioctl v1.14.1](https://istio.io/latest/docs/setup/getting-started/#download)
- Install helm v3 `brew install helm`
- Install kind `brew install kind`

## Get started
- `make init`
- `make iris`
- `make test`

## See it to believe it
[![asciicast](https://asciinema.org/a/J5Ies2TySyE2uWmB8uqW8Q2hZ.svg)](https://asciinema.org/a/J5Ies2TySyE2uWmB8uqW8Q2hZ)
