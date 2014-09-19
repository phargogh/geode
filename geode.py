import subprocess

if __name__ == '__main__':
    # set up virtualenv
    subprocess.call(['virtualenv --clear geode_env'], shell=True)
    print 'finished creating virtualenv:geode_env'

