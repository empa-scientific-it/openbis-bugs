#!/bin/bash
docker inspect $(docker compose ps -q $1) -f "{{.State.Health.Status}}" | grep -q healthy