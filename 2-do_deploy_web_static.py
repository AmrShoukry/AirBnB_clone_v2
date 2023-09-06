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
        put(archive_path, '/tmp/')
        archive_name = os.path.basename(archive_path)
        run(f'mkdir -p /data/web_static/releases/{archive_name}/')
        run(f'tar -xzf /tmp/{archive_name} -C\
            /data/web_static/releases/{archive_name}')
        run(f'rm /tmp/{archive_name}')
        run(f'mv /data/web_static/releases/{archive_name}/web_static/*\
             /data/web_static/releases/{archive_name}/')
        run(f'rm -rf /data/web_static/releases/{archive_name}/web_static')
        run(f'rm -rf /data/web_static/current')
        run(f'ln -s /data/web_static/releases/{archive_name}/\
             /data/web_static/current')
        print("New version deployed!")
        return True
    except Exception as E:
        return False
