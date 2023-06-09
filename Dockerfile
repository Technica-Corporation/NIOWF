FROM nikolaik/python-nodejs:python3.9-nodejs10
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY ./ozone-framework-python-server /code/ozone-framework-python-server
COPY ./ozone-framework-client /code/ozone-framework-client
COPY ./ozone-example-widgets /code/ozone-example-widgets
COPY ./start.sh /code
RUN chmod +x /code/*.sh
RUN npm install --prefix /code/ozone-framework-client
RUN npm run bootstrap --prefix /code/ozone-framework-client
RUN pip install -r /code/ozone-framework-python-server/requirements_prod.txt
