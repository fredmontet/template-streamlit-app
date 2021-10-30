install:
	@echo "Installing all dependencies with Pipenv"
	pipenv install && pipenv shell

start:
	@echo "Starting application with Streamlit"
	streamlit run src/main.py --server.runOnSave true
