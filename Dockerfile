FROM jupyter/base-notebook

# Disable all notebook auth, since refinery will be handling this
RUN echo "c.NotebookApp.token = ''" >> /etc/jupyter/jupyter_notebook_config.py

# Make directory for Refinery Data to live in
RUN mkdir /home/jovyan/refinery-data

# Copy our input, and startup script to ingest data
COPY input.json /tmp/input.json
COPY on_startup.py /tmp/on_startup.py

# Copy our custom start.sh
COPY start.sh /usr/local/bin/start.sh

# Copy our custom html page to display whilst waiting for data to be ingested
COPY page.html /tmp/page.html





