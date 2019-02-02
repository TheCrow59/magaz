from setuptools import setup

setup(
    name='magaz',
    packages=['magaz'],
    include_package_data=True,
    install_requires=[
        'flask',
        'Flask-Cors',
        'Flask-Migrate',
        'Flask-SQLAlchemy',
        'itsdangerous',
        'Jinja2',
        'MarkupSafe',
        'psycopg2-binary',
        'SQLAlchemy',
        'Werkzeug',
        'flask-admin',
        'Flask-BasicAuth'
    ],
)