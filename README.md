# service SMT V2

## Instalasi

Clone repo

```bash
  git clone https://github.com/muhamadijlal/service-smt-at4-.git
```

## Jalankan service

local

```
  SCHEDULE_INTERVAL=5 DB_HOST="localhost" DB_USERNAME="root" DB_PORT="3306" DB_PASSWORD="" DB_DATABASE="dtabaseName" python main.py
```

docker

```
  docker run --restart=always -v /etc/localtime:/etc/localtime --name service-smt-v2 -e SCHEDULE_INTERVAL=5 -e DB_HOST="localhost" -e DB_USERNAME="root" -e DB_PORT="3306" -e DB_PASSWORD="" -e DB_DATABASE="dtabaseName" -dit yourimagesdokcer:version
```

## Features

- Service AT4 SMT
- Koneksi ke (MySQL, Postgresql)
- scheduler service

## Libs

- mysql-connector-python
- apscheduler
- python-dotenv
- logging
- colorama
- requests

## Versi

- Python 3.10.6
