 #!/bin/bash
 NAME="<project>"
 DIR=/home/<username>/<project>/
 USER= "<username>"
 GROUP= "<groupname>"
 WORKERS=3
 BIND=unix:/home/<username>/<project>/run/gunicorn.sock
 DJANGO_SETTINGS_MODULE=backend.settings
 DJANGO_WSGI_MODULE=backend.wsgi
 LOG_LEVEL=error
 ENV=/home/<username>/.local/share/virtualenvs/<pipenv_generate_name>/bin/activate
 cd ${DIR}
 source ${ENV}
 export DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE}
 export PYTHONPATH=${DIR}:${PYTHONPATH}

 exec $(which gunicorn) ${DJANGO_WSGI_MODULE}:application \
 --name ${NAME} \
 --workers ${WORKERS} \
 --user=${USER} \
 --group=${GROUP} \
 --bind=${BIND} \
 --log-level=${LOG_LEVEL} \
 --log-file=-