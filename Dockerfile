FROM python:3.13

LABEL Maintainer="Florian Thiévent"
LABEL traefik.enable="true"
LABEL traefik.http.middlewares.trbapi-https-redirect.redirectscheme.scheme="https"
LABEL traefik.http.routers.trbapi-secure.entrypoints="https"
LABEL traefik.http.routers.trbapi-secure.rule="Host(`trbapi.thievent.org`)"
LABEL traefik.http.routers.trbapi-secure.service="trbapi"
LABEL traefik.http.routers.trbapi-secure.tls="true"
LABEL traefik.http.routers.trbapi-secure.tls.certresolver="http"
LABEL traefik.http.routers.trbapi.entrypoints="http"
LABEL traefik.http.routers.trbapi.middlewares="trbapi-https-redirect"
LABEL traefik.http.routers.trbapi.rule="Host(`trbapi.thievent.org`)"
LABEL traefik.http.routers.trbapi.service="trbapi"
LABEL traefik.http.routers.trbapi.tls.certresolver="leresolver"
LABEL traefik.http.services.trbapi.loadbalancer.server.port="8000"

# Set variables for project name, and where to place files in container.
ENV PROJECT=trbapi
ENV CONTAINER_HOME=/opt
ENV CONTAINER_PROJECT=$CONTAINER_HOME/$PROJECT

# Image updates
# RUN apt-get update && apt-get upgrade

# Create application subdirectories
RUN mkdir $CONTAINER_PROJECT
WORKDIR $CONTAINER_PROJECT
RUN mkdir $CONTAINER_PROJECT/logs
RUN echo "" > $CONTAINER_PROJECT/logs/gunicorn.log
# Copy application source code to $CONTAINER_PROJECT
COPY . $CONTAINER_PROJECT

#Upgrade Pip and setuptools
RUN python -m pip install --upgrade pip setuptools

# Install Python dependencies
RUN pip install -r $CONTAINER_PROJECT/requirements.txt

# Copy and set entrypoint
WORKDIR $CONTAINER_PROJECT
COPY ./start.sh /
RUN ["chmod", "+x", "/opt/trbapi/start.sh"]

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]