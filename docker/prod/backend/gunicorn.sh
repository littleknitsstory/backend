 #!/bin/bash
 NAME="Little knits story"
 DIR=/home/lks_user/lks/
 USER= "lks"
 GROUP= "lks"
 WORKERS=3
 BIND=unix:/home/lks_user/lks/run/gunicorn.sock
 DJANGO_SETTINGS_MODULE=backend.settings
 DJANGO_WSGI_MODULE=backend.wsgi
 LOG_LEVEL=error
 ENV=/home/lks_user/.local/share/virtualenvs/<pipenv_generate_name>/bin/activate
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