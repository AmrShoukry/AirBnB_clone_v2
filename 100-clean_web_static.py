#!/usr/bin/python3
""" 4. Keep it clean! """
import os
from fabric.api import env, run

env.hosts = ['18.207.140.20', '18.204.13.232']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'

def clean_path(number, directory_path, files, state):
    """ Delete a specific path """
    sorted_files = sorted(files)

    length = len(sorted_files)
    safe_index = length - number
        
    for index, file_name in enumerate(sorted_files):
        if index < safe_index:
            if state == 'local':
                os.remove(os.path.join(directory_path, file_name))
            else:
                run(f'rm -r {directory_path}/{file_name}')



def do_clean(number=0):
    """ deletes out-of-date archives """
    current_directory = os.getcwd()
    local_path = os.path.join(current_directory, "versions")
    server_path = '/data/web_static/releases'

    number = int(number)
    if number == 0:
        number = 1

    local_files = os.listdir(local_path)
    local_files = [file for file in local_files if file.startswith("web_static")]
    server_files = run(f'ls {server_path}').split()
    server_files = [file for file in server_files if file.startswith("web_static")]

    clean_path(number, local_path, local_files, 'local')
    clean_path(number, server_path, server_files, 'server')
