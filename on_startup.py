import glob
import json
import logging
import requests
import subprocess
from requests.exceptions import RequestException

logger = logging.getLogger(__name__)


def populate_jupyter_data_directory(data_dir):
    """
    Download remote files specified by urls in the input.json file
    :param data_dir: <String> Path to directory to populate with data
    """
    with open("/tmp/input.json") as f:
        config_data = json.loads(f.read())

    for url in config_data["file_relationships"]:
        try:
            # Streaming GET for potentially large files
            response = requests.get(url, stream=True)
        except RequestException as e:
            raise RuntimeError(
                "Something went wrong while fetching file from {} : {}".format(
                    url,
                    e
                )
            )
        else:
            with open('{}{}'.format(data_dir, url.split("/")[-1]), 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    # filter out KEEP-ALIVE new chunks
                    if chunk:
                        f.write(chunk)
        finally:
            response.close()


# def swap_waiting_page():
#     subprocess.call(["mv", "/opt/conda/share/jupyter/hub/templates/page.html.bak",
#                      "/opt/conda/share/jupyter/hub/templates/page.html"])

if __name__ == '__main__':
    data_dir = "/home/jovyan/refinery-data/"

    populate_jupyter_data_directory(data_dir)

    # Don't switch page until data ingested
    # swap_waiting_page()
