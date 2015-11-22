FROM python:3

RUN apt-get update && apt-get install -y \
                build-essential \
                gcc \
                libffi-dev \
                libfreetype6-dev libjpeg-dev \
                libssl-dev \
                mysql-client libmysqlclient-dev \
                postgresql-client libpq-dev \
                python3-dev python3-pip \
                zlib1g-dev \
        --no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

ENTRYPOINT ["./entrypoint.sh"]
