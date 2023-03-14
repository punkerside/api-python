FROM alpine:3.17.2

RUN apk update && apk upgrade && apk add python3 python3-dev py3-pip

RUN pip install flask
RUN pip install flask_restful
RUN pip install redis


COPY app/app.py app.py
CMD [ "python", "app.py" ]