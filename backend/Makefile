.PHONY: help sync run migrate gen_migration

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

sync: ## Sync the project dependencies using uv
	uv sync

run: ## Run the FastAPI server
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

migrate: ## Run alembic migrations
	alembic upgrade head

gen_migration: ## Generate a new alembic migration with a message
	@read -p "Enter migration message: " msg; \
	alembic revision --autogenerate --message "$$msg"
