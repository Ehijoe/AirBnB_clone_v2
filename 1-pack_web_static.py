#!/usr/bin/python3
"""Deploy the hbnb static site."""
import datetime
import os.path
from fabric.operations import local


def do_pack():
    """Pack the contents of web_static in an archive."""
    time = datetime.datetime.now()
    time = time.strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{time}.tgz"
    if not os.path.exists("versions"):
        local("mkdir versions")
    res = local(f"tar -cvzf versions/{archive_name} web_static")
    if res.failed:
        return None
    return f"versions/{archive_name}"
