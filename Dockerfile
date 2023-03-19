FROM python

WORKDIR /src
RUN apt-get update && apt-get install -y python3-enchant pipenv

COPY . /src
RUN pipenv lock --requirements > requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD /usr/bin/pipenv run gunicorn --bind 0.0.0.0:$PORT src.run:app
