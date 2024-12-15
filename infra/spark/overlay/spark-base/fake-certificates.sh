#!/bin/bash

mkdir fake-certificates

openssl req -newkey rsa:2048 -keyout fake-certificates/domain.key -out fake-certificates/domain.csr

openssl x509 -signkey fake-certificates/domain.key -in fake-certificates/domain.csr -req -days 365 -out fake-certificates/domain.crt