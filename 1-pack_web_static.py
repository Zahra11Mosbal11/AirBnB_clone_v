#!/usr/bin/python3
"""Compress before sending"""
from datetime import datetime
from fabric import *
from fabric.operations import local


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    
    now = datetime.now()
    archive = 'web_static_' + now.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
