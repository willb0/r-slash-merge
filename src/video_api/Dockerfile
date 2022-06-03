FROM arm64v8/python:3.9-slim

WORKDIR /usr/src/api
RUN apt-get update && apt-get install ffmpeg -y && apt-get install python3-tk -y
COPY requirements.txt /usr/src/api/requirements.txt

ENV PYTHONUNBUFFERED=1
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

COPY ./ /usr/src/api/
RUN mkdir videos
ENV VIDEOPATH=/usr/src/api/videos/
ENV PYTHONUNBUFFERED=1

EXPOSE 81


CMD ["uvicorn","main:app","--host","0.0.0.0","--port","81"]
