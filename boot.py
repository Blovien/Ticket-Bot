import os
import subprocess
import sys
from ticketBot.update import main


def pyexec(pycom, *args, pycom2=None):
    pycom2 = pycom2 or pycom
    os.execlp(pycom, pycom2, *args)


def check_python():
    print("Checking for Python 3.5+")

    if sys.version_info < (3, 5):
        print("Python 3.5+ is required. This version is %s", sys.version.split()[0])

        pycom = None

        if sys.platform.startswith('win'):
            print('Trying "py -3.5"')
            try:
                subprocess.check_output('py -3.5 -c "exit()"', shell=True)
                pycom = 'py -3.5'
            except:
                print('Trying "python3"')
                try:
                    subprocess.check_output('python3 -c "exit()"', shell=True)
                    pycom = 'python3'
                except:
                    pass

            if pycom:
                pyexec(pycom, 'boot.py')

                # I hope ^ works
                os.system('start cmd /k %s boot.py' % pycom)
                sys.exit(0)

        else:
            print('Trying "python3.5"')
            try:
                pycom = subprocess.check_output('python3.5 -c "exit()"'.split()).strip().decode()
            except:
                pass

            if pycom:
                print("\nPython 3 found.  Re-launching bot using: %s boot.py\n", pycom)
                pyexec(pycom, 'boot.py')

                print("Could not find Python 3.5 or higher.  Please run the bot using Python 3.5")


def boot():
    check_python()


if __name__ == '__main__':
    boot()
    main()
