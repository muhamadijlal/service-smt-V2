# service SMT V2

## Instalasi

Clone repo

```bash
  git clone https://github.com/muhamadijlal/service-smt-at4-.git
```

copy .env.example rename menjadi .env

sesuaikan konfigurasi credentials

```
  SCHEDULE_INTERVAL=1 # Interval dalam menit
  DB_CONNECTION=mysql
  DB_HOST=127.0.0.1
  DB_PORT=3306
  DB_DATABASE=laravel
  DB_USERNAME=root
  DB_PASSWORD=
```

## Jalankan service

```
  python main.py
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
