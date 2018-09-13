FROM python:3-alpine
EXPOSE 8000
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY ./ /code/

RUN pip3 install -r requirements.txt

