import subprocess
import os

if __name__ == '__main__':
    # set up virtualenv

    local_package_dir = os.path.expanduser('~/.geode/packages/')
    if not os.path.exists(local_package_dir):
        os.makedirs(local_package_dir)

    envdir = 'geode_env'

    subprocess.call(['virtualenv --clear %s' % envdir], shell=True)
    print 'finished creating virtualenv:geode_env'

    pip_path = os.path.join(envdir, 'bin', 'pip')

    # Must refer to pip using explicit path
    kwargs = {
        'pip': pip_path,
        'download_dir': local_package_dir,
    }
    subprocess.call('%(pip)s install wheel --download-cache %(download_dir)s' % kwargs, shell=True)
