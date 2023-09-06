#!/usr/bin/python3
""" 1. Compress before sending """

from fabric.api import task, local
import os
from datetime import datetime


@task
def do_pack():
    current_directory = os.getcwd()

    parent_directory = 'versions/'
    full_parent_directory = os.path.join(current_directory, parent_directory)

    if not os.path.exists(full_parent_directory):
        os.makedirs(full_parent_directory)

    current_date = datetime.now()
    year = current_date.year
    month = current_date.strftime('%m')
    day = current_date.strftime('%d')
    hour = current_date.strftime('%H')
    minute = current_date.strftime('%M')
    second = current_date.strftime('%S')

    archive_name = f'web_static_{year}{month}{day}{hour}{minute}{second}.tgz'
    archive_path = os.path.join(full_parent_directory, archive_name)

    try:
        print(f"Packing web_static to versions/{archive_name}")
        local(f'tar -cvzf versions/{archive_name} web_static')
        size = os.path.getsize(archive_path)
        print(f"web_static packed: versions/{archive_name} -> {size}Bytes")
        return archive_path
    except Exception as e:
        return None
