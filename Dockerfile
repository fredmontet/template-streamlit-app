FROM python:3.9

COPY . /app
WORKDIR /app

RUN pip install poetry
RUN poetry install

EXPOSE 8501

CMD poetry run streamlit run src/main.py