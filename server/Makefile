# Format code
.PHONY: format
format:
	poetry run black .
	poetry run isort .

# Lint code
.PHONY: lint
lint:
	poetry run flake8 .

# Check code format and style 
.PHONY: check
check:
	poetry run black --check .
	poetry run isort --check-only .
	poetry run flake8 .
