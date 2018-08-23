Open Postgres with psql and then: __

CREATE DATABASE multiple_schema;
CREATE USER ivan;
GRANT ALL on DATABASE multiple_schema to ivan;
ALTER USER ivan with  password 'ivan123!'
\c multiple_schema
CREATE SCHEMA app1;
CREATE SCHEMA app2;
\q

####Activate  virtual env  with
source bin/activate
cd multipleSchema
python manage.py migrate
##Enjoy :)

