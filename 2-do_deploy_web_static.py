#!/usr/bin/python3
""" 2. Deploy archive! """
import os
from fabric.api import env, run, put

env.hosts = ['18.207.140.20', '18.204.13.232']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """ Deploying a new archive into web servers """

    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = os.path.basename(archive_path)
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run(f'mkdir -p {path}{archive_name}/')
        run(f'tar -xzf /tmp/{archive_name} -C {path}{archive_name}')
        run(f'rm /tmp/{archive_name}')
        run(f'mv {path}{archive_name}/web_static/* {path}{archive_name}/')
        run(f'rm -rf /{path}{archive_name}/web_static')
        run(f'rm -rf /data/web_static/current')
        run(f'ln -s {path}{archive_name}/ /data/web_static/current')
        return True
    except Exception as E:
        return False
