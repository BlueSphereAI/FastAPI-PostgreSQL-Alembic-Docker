.PHONY: runBuildDocker runDocker

SHELL := /bin/bash

runBuildLocalDocker:
	docker compose -f docker-compose.local.yml up -d --build

stopBuildLocalDocker:
	docker compose -f docker-compose.local.yml down

runLocalDocker:
	docker compose -f docker-compose.local.yml up -d

runBuildDevDocker:
	docker compose -f docker-compose.dev.yml up -d --build

stopBuildDevDocker:
	docker compose -f docker-compose.dev.yml down

runDevDocker:
	docker compose -f docker-compose.dev.yml up -d
