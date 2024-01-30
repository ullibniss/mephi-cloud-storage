#!/bin/bash

docker build -t cloud-storage:latest .
docker-compose up -d
