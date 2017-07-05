FROM jupyter/base-notebook

COPY on_startup.py /home/jovyan/on_startup.py
# COPY page.html /home/jovyan/page.html
COPY input.json /home/jovyan/input.json
COPY start.sh /usr/local/bin/start.sh

# Disable all auth
RUN echo "c.NotebookApp.token = ''" >> /etc/jupyter/jupyter_notebook_config.py
# Disable csrf
RUN echo "c.NotebookApp.disable_check_xsrf = True" >> /etc/jupyter/jupyter_notebook_config.py

RUN mkdir /home/jovyan/refinery-data