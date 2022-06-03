# r slash merge

```
git clone https://github.com/willb0/r-slash-merge
cd r-slash-merge
docker-compose build
docker-compose up
```

and go hit localhost:82/docs
port 81 is video api
port 80 is links api

when u kill it
`docker-compose down --volumes`

doesnt delete videos from shared storage or local storage after download, doing that next