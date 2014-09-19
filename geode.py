import subprocess
import os

if __name__ == '__main__':
    # set up virtualenv

    envdir = 'geode_env'

    subprocess.call(['virtualenv --clear %s' % envdir], shell=True)
    print 'finished creating virtualenv:geode_env'

    pip_path = os.path.join(envdir, 'bin', 'pip')

    # Must refer to pip using explicit path
    subprocess.call('%s install wheel' % pip_path, shell=True)
