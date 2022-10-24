FROM arm64v8/python:3.9-slim


WORKDIR /usr/src/api
RUN apt-get update
COPY requirements.txt /usr/src/api/requirements.txt

ENV PYTHONUNBUFFERED=1
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

COPY ./ /usr/src/api/

EXPOSE 8501


CMD ["python3","-m","streamlit","run","main.py"]