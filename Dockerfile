FROM python

WORKDIR /app
RUN apt-get update && apt-get install -y libenchant-dev pipenv

COPY . /app
RUN pipenv install

EXPOSE 8000

ENTRYPOINT ["/usr/bin/pipenv", "run" ,"gunicorn -b 0.0.0.0:8000 src.run:app"]
