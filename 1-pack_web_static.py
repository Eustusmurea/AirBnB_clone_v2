#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import local
from os.path import exists, join


def do_pack():
    """Generates a tgz archive."""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        output_dir = "versions"
        if not exists(output_dir):
            local("mkdir -p {}".format(output_dir))
        file_name = "web_static_{}.tgz".format(date)
        file_path = join(output_dir, file_name)
        local("tar -cvzf {} web_static".format(file_path))
        return file_path
    except Exception as e:
        print(f"Error: {e}")
        return None

do_pack()

