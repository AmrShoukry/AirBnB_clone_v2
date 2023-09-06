#!/usr/bin/python3
""" 3. Full deployment """
from fabric.api import env, task, runs_once
packing = __import__('1-pack_web_static')
deploying = __import__('2-do_deploy_web_static')

archive_path = packing.do_pack()

@task
def deploy():
    """ Combine packing and deploying together """
    if archive_path is None:
        return False
    return deploying.do_deploy(archive_path)
