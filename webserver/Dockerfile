FROM continuumio/miniconda:latest

ENV IN_DOCKER=1
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    python-dev

COPY environment.yml /environment.yml
RUN conda env update -f environment.yml -n base

COPY /webserver/app.py /app.py

EXPOSE 5000

CMD ["python", "-u", "app.py"]
