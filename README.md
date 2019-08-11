# qisdatascraper

Simple Python script to check for new grades at the qis portal

## how to use:

* Add information to marked places in the sourcecode
* run:
``` 
docker build -t qisdatascraper:v0.1 .
```
* fix the path in the docker-compose.yml to where the code is
* run:
```
sudo docker-compose up -d
```

This uses a telegram bot to send you grades. Check out [this](https://www.codementor.io/garethdwyer/building-a-telegram-bot-using-python-part-1-goi5fncay).
