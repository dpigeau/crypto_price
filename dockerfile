FROM python:3.10-slim

# Tell pipenv to create venv in the current directory
ENV PIPENV_VENV_IN_PROJECT=1

COPY ./Pipfile ./Pipfile.lock ./.env ./

RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install

COPY ./app /app

EXPOSE 8501

ENTRYPOINT ["pipenv", "run", "streamlit", "run", "app/main.py"]
