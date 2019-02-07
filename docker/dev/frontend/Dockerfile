FROM node:lts-alpine as frontend

ADD package.json package.json
RUN yarn
ADD . ./
RUN yarn run build:dev

FROM nginx:alpine
ADD nginx.conf.nginx /etc/nginx/conf.d/default.conf
COPY --from=frontend /build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
