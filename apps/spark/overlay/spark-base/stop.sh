#!/bin/bash
set -euo pipefail

kustomize build | kubectl delete -f -