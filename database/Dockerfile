FROM postgres:9.3
ENV POSTGRES_USER docker
ENV POSTGRES_PASSWORD docker
ENV POSTGRES_DB docker

WORKDIR /database

ADD create_db.sql /docker-entrypoint-initdb.d/

EXPOSE 5432