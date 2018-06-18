FROM praekeltfoundation/python-base:3.6-stretch

RUN apt-get update && apt-get install -y netcat git

WORKDIR /app/

COPY requirements.txt /app/requirements/

RUN pip3 install --no-cache-dir -r /app/requirements/requirements.txt --src /usr/local/src

COPY . /app/

EXPOSE 8080

CMD ["uwsgi", "uwsgi.ini"]
