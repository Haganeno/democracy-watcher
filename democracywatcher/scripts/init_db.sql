CREATE DATABASE democracywatcher;
CREATE USER dmw WITH ENCRYPTED PASSWORD 'pass1234';
ALTER ROLE dmw SET client_encoding TO 'utf8';
ALTER ROLE dmw SET default_transaction_isolation TO 'read committed';
ALTER ROLE dmw SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE democracywatcher TO dmw;