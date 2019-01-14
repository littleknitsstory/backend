FROM node:alpine

RUN mkdir /frontend
WORKDIR frontend

ADD ./frontend/package.json /frontend/package.json

RUN yarn

ADD ./frontend /frontend/

RUN yarn run server
