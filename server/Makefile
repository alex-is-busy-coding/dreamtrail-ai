# Format code
.PHONY: format
format:
	poetry run black .

# Sort imports
.PHONY: sort
sort:
	poetry run isort .

# Lint code
.PHONY: lint
lint:
	poetry run flake8 .

# Check types
.PHONY: type-check
type-check:
	poetry run mypy .

# Check code format and style 
.PHONY: check
check:
	poetry run black --check .
	poetry run isort --check-only .
	poetry run flake8 .
	poetry run mypy .
