FROM alpine

RUN apk add --update nginx
RUN apk add --update bash && rm -rf /var/cache/apk/*

RUN mkdir -p /run
RUN mkdir -p /storage

#COPY ./media/ /srorage/media
#COPY nginx.conf /etc/nginx/nginx.conf
#COPY nginx.conf /etc/nginx/conf.d/default.conf
#COPY media /media

CMD ["nginx", "-g", "daemon off;"]
