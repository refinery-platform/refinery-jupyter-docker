FROM jupyter/base-notebook

COPY on_startup.py /home/jovyan/on_startup.py
COPY input.json /home/jovyan/input.json
COPY start.sh /usr/local/bin/start.sh

# # Display our waiting page until jupyter downloads all necessary files
# COPY index.html 

# Disable all auth
RUN echo "c.NotebookApp.token = ''" >> /etc/jupyter/jupyter_notebook_config.py

RUN mkdir /home/jovyan/refinery-data