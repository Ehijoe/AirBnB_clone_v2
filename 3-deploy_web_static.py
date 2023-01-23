#!/usr/bin/python3
"""Deploy the hbnb static site."""
import datetime
import os.path
from fabric.api import *

env.hosts = ["18.234.107.94", "3.85.196.195"]


def do_pack():
    """Pack the contents of web_static in an archive."""
    time = datetime.datetime.now()
    time = time.strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{time}.tgz"
    if not os.path.exists("versions/"):
        local("mkdir versions")
    res = local(f"tar -cvzf versions/{archive_name} web_static")
    if res.failed:
        return None
    return f"versions/{archive_name}"


def do_deploy(archive_path):
    """Deploy archive on servers."""
    archive = archive_path[9:]
    if not os.path.exists(archive_path):
        return False
    put(archive_path, "/tmp/")
    run(f"tar -xvzf /tmp/{archive}")
    run("mkdir -p /data/web_static/releases")
    run(f"mv -f web_static /data/web_static/releases/{archive[:-4]}")
    run("rm /data/web_static/current")
    run(f"ln -s /data/web_static/releases/{archive[:-4]}/ "
        "/data/web_static/current")
    return True


def deploy():
    """Deploy the current repo as a new version."""
    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive)
