FROM python:3.10-slim
RUN apt-get clean && apt-get -y update
WORKDIR /app
COPY modules /app/modules
RUN pip install -r modules 
COPY ./app/ /app/
COPY sample.txt /tmp/
EXPOSE 5000
CMD [ "python", "/app/main.py" ]
