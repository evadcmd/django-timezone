FROM python:3.8-slim as server
ENV APPDIR /opt/app/
WORKDIR ${APPDIR}
COPY project/ ${APPDIR}project
COPY Pipfile* ${APPDIR}
COPY wait-for-it.sh ${APPDIR}
RUN chmod +x wait-for-it.sh
RUN pip install pipenv
RUN pipenv install --system --deploy