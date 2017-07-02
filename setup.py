from setuptools import setup

setup(
    name='taas',
    packages=['taas'],
    include_package_data=True,
    install_requires=[
        'flask==0.12.2',
        'sqlalchemy==1.1.11',
        'Flask-SQLAlchemy==1.0',
        'psycopg2==2.7.1'
    ],
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest',
    ],
)