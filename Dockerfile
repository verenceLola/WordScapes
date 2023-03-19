FROM python

WORKDIR /app
RUN apt-get update && apt-get install -y python3-enchant pipenv

COPY . /app
RUN pipenv lock --requirements > requirements.txt

RUN cat requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD /usr/bin/pipenv run gunicorn --bind 0.0.0.0:8000 src.run:app
