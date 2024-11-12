#!/bin/bash
# USAGE: sh ./unseal-vault.sh POD-NAME

kubectl exec $1 -- vault operator init -key-shares=1 -key-threshold=1 -format=json > cluster-keys.json 

VAULT_UNSEAL_KEY=$(jq -r ".unseal_keys_b64[]" cluster-keys.json)

kubectl exec $1 -- vault operator unseal $VAULT_UNSEAL_KEY