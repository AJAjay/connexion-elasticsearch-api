#!/usr/bin/env python3
import connexion
import datetime
import logging

from connexion import NoContent
from elasticsearch import Elasticsearch

# our memory-only pet storage
PETS = {}


def get_data(query):
    es = Elasticsearch()
    value = es.search(index=query['index'],body=query['body'])
    return value

def test_query(query):
    es = Elasticsearch()
    print(query)
    value = es.search(index=query['index'],body=query['body'])
    return value


logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__)
app.add_api('swagger.yaml')
# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app
application = app.app

if __name__ == '__main__':
    # run our standalone gevent server
    app.run(port=8080, server='gevent')
