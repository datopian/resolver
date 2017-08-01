import os
import json
import requests

config = {}
for key, value in os.environ.items():
    config[key.upper()] = value


def resolve(path):
    """Resolve path for publisher. returns uid and pkgid
    :path: path to resolve <username>/<pkgname>
    """
    if not path:
        return dict()
    username, pkgname = path.split('/')[0], path.split('/')[1]
    response = requests.get('{auth_server}/auth/resolve?username={username}'
        .format(auth_server=config['AUTH_SERVER'], username=username))
    ret = response.json()
    ret['packageid'] = pkgname
    return ret
