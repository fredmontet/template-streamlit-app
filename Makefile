install:
	@echo "Installing all dependencies with Poetry"
	poetry install

dev:
	@echo "Starting the application for development"
	poetry shell && streamlit run src/main.py --server.runOnSave true

start:
	@echo "Starting application for production"
	streamlit run src/main.py --server.runOnSave true
