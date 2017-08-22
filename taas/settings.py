# -*- coding: utf-8 -*-
"""Application configuration."""
import os


def get_db_uri():
    db_uri = os.environ.get('DATABASE_URI', 'localhost')
    db_user = os.environ.get('DATABASE_USER', 'postgres')
    db_pass = os.environ.get('DATABASE_PASS', 'mysecretpassword')
    return 'postgresql://{}:{}@{}/taas'.format(db_user, db_pass, db_uri)

def get_api_url():
    api_url = os.environ.get('API_CALLBACK_URL', 'http://localhost:5000')
    return api_url


class Config(object):
    """Base configuration."""

    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = 'amqp://guest@localhost//'
    CELERY_BACKEND = 'amqp://guest@localhost//'
    API_CALLBACK_URL = get_api_url()


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = get_db_uri()


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = get_db_uri()
