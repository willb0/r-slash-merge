FROM arm64v8/python:3.9-slim


WORKDIR /usr/src/api
RUN apt-get update
COPY requirements.txt /usr/src/api/requirements.txt

ENV PYTHONUNBUFFERED=1
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

COPY ./ /usr/src/api/

EXPOSE 80


CMD ["uvicorn","main:app","--host","0.0.0.0","--port","82"]