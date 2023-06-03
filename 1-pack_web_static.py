#!/usr/bin/python3
"""A script that generates a .tgz archive from the
contents of web_static using the do_pack
"""
from fabric.api import local, env
import datetime


def do_pack():
    """Creates a tar gzipped archive for the
    directory web_static """
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    local('sudo mkdir -p ./versions')
    path = './versions/web_static_{}'.format(now)
    local('sudo tar -czvf {}.tgz web_static'.format(path))
    name = '{}.tgz'.format(path)
    if name:
        return name
    else:
        return None
