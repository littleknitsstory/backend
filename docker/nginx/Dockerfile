FROM nginx:1.12-alpine

COPY nginx.conf.nginx /etc/nginx/sites-enabled/default

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]