FROM continuumio/miniconda:latest

ENV IN_DOCKER=1
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

COPY environment.yml /environment.yml
RUN conda env update -f environment.yml -n base

COPY app.py /app.py

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
