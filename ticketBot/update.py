import os
import subprocess
import sys


def y_n(q):
    while True:
        ri = input('{} (y/n): '.format(q))
        if ri.lower() in ['yes', 'y']:
            return True
        elif ri.lower() in ['no', 'n']:
            return False


def main():
    print('Starting...')

    if not os.path.isdir('.git'):
        raise EnvironmentError("This isn't a Git repository.")

    try:
        subprocess.check_call('git --version', shell=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        raise EnvironmentError("Couldn't use Git on the CLI. You will need to run 'git pull' yourself.")

    print("Passed Git checks...")

    # Check that the current working directory is clean
    sp = subprocess.check_output('git status --porcelain', shell=True, universal_newlines=True)
    if sp:
        oshit = y_n('You have modified files that are tracked by Git (e.g the bot\'s source files).\n'
                    'We can try to reset your folder to a clean version for you. Continue?')
        if oshit:
            try:
                subprocess.check_call('git reset --hard', shell=True)
            except subprocess.CalledProcessError:
                raise OSError("Could not reset the directory to a clean state.")
        else:
            print('Okay. Cancelling update process for now.')
            return

    print("Attempting to update the bot using Git...")

    try:
        subprocess.check_call('git pull', shell=True)
    except subprocess.CalledProcessError:
        raise OSError("Could not update the bot. You will need to run 'git pull' yourself.")

    print("Attempting to update dependencies...")

    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-U', '-r', 'requirements.txt'], shell=True)
        print("type exit()")
    except subprocess.CalledProcessError:
        raise OSError(
            "Could not update dependencies. You will need to run '{0} -m pip install -U -r requirements.txt' yourself.".format(
                sys.executable))

    print("Done!")


if __name__ == '__main__':
    main()
