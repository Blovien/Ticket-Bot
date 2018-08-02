import os
import subprocess
import sys


def main():
    print('Starting...')

    if not os.path.isdir('.git'):
        raise EnvironmentError("This isn't a Git repository.")

    try:
        subprocess.check_call('git --version', shell=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        raise EnvironmentError("Couldn't use Git on the CLI. You will need to run 'git pull' yourself.")

    print("Passed Git checks...")

    print("Done!")


if __name__ == '__main__':
    main()
