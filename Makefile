.PHONY: install run dev test clean help

# Default target
help:
	@echo "Available commands:"
	@echo "  install    Install dependencies"
	@echo "  run        Run the application"
	@echo "  dev        Run the application in development mode with auto-reload"
	@echo "  test       Test the API endpoints"
	@echo "  clean      Clean cache files"
	@echo "  help       Show this help message"

# Install dependencies
install:
	pip install -r requirements.txt

# Run the application
run:
	uvicorn main:app --host 0.0.0.0 --port 8000

# Run in development mode with auto-reload
dev:
	uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# Test the API endpoints
test:
	@echo "Testing the API..."
	@echo "Testing root endpoint:"
	curl -s http://localhost:8000/ | python -m json.tool
	@echo "\nTesting weather endpoint for New York:"
	curl -s http://localhost:8000/weather/New%20York | python -m json.tool
	@echo "\nTesting weather endpoint for Tokyo:"
	curl -s http://localhost:8000/weather/Tokyo | python -m json.tool
	@echo "\nTesting health check:"
	curl -s http://localhost:8000/health | python -m json.tool

# Clean cache files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete 