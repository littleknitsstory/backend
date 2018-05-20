FROM nginx:latest

# Set the file maintainer (your name - the file's author)
MAINTAINER Ray Alez

ENV HOMEDIR=/home
ENV PROJECTDIR=/home/blog
ENV FRONTENDDIR=/frontend


# Turn off daemon mode
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf

# Copy frontend files
WORKDIR $FRONTENDDIR
COPY . .

# Copy nginx config
RUN rm /etc/nginx/sites-enabled/default
COPY frontend_nginx.conf /etc/nginx/sites-enabled


# Define default command.
CMD ["nginx"]

# Expose ports.
EXPOSE 8080
