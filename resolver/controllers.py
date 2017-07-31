import os

def resolve(path):
    """Resolve path for publisher. returns uid and pkgid
    :path: path to resolve <username>/<pkgname>
    """
    if not path:
        return dict()
    username, pkgname = path.split('/')[0], path.split('/')[1]
    return dict(userid=username, packageid=pkgname)
