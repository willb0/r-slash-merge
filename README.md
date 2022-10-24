# r slash merge

```
git clone https://github.com/willb0/r-slash-merge
cd r-slash-merge
docker-compose build
docker-compose up
```
dashboard : [localhost:8501/](https://localhost:8501/)
links-api : [localhost:80/](https://localhost:80/docs)
video-api : [localhost:81/](https://localhost:81/docs)
pipeline : [localhost:82/](https://localhost:82/docs)

when u kill it
`docker-compose down --volumes`

## Dashboard
The dashboard provides a Streamlit UI to test the app and view the video response
it will look like this:
<img src="images/screenshot.jpg" alt="drawing" width="200"/>