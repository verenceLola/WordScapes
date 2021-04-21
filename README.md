# WordScapes

Genrate US English Words from a given number of letters.

## Running The Application Locally

To run the application locally; run the command

```bash
pipenv install # to install application dependencies
gunicorn src.run:app # to run the application server
```

Configure your .env file as shown in the sample below

```bash
FLASK_APP=src.run
FLASK_ENV=development
```
