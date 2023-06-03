#!/usr/bin/python3
"""
A fabric script that distributes an archive on the web servers using do_deploy:
"""
from fabric.api import local, env, put, run
import datetime
import os

env.user = 'ubuntu'
env.hosts = ['35.174.211.234', '100.25.141.83']


def do_pack():
    """
    The prototype to produce a .tgz file
    """
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    local('sudo mkdir -p ./versions')
    path = './versions/web_static_{}'.format(now)
    local('sudo tar -czvf {}.tgz web_static'.format(path))
    name = '{}.tgz'.format(path)
    if name:
        return name
    else:
        return None


def do_deploy(archive_path):
    """
    A script that distributes an archive to web servers
    """
    if os.path.exists(archive_path):
        archive = archive_path.split('/')[-1]
        path = '/data/web_static/releases/{}/'.format(archive.split('.')[0])
        current = '/data/web_static/current'
        path_a = '/tmp/{}'.format(archive)
        put(archive_path, path_a)
        run('sudo mkdir -p {}/'.format(path))
        run('sudo tar -xzf {} -C {}'.format(path_a, path))
        run('sudo rm {}'.format(path_a))
        run('sudo mv {}/web_static/* {}'.format(path, path))
        run('sudo rm -rf {}/web_static'.format(path))
        run('sudo rm -rf {}'.format(current))
        run('sudo ln -s {} {}'.format(path, current))
        print('New version deployed!')
        return True
    return False
