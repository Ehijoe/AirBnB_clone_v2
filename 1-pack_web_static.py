#!/usr/bin/python3
"""Deploy the hbnb static site."""
import datetime


def do_pack():
    """Pack the contents of web_static in an archive."""
    time = datetime.datetime.now()
    time = time.strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{time}.tgz"
    print(archive_name)
