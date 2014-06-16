import os
from installimage import install_image

try:
    from cmd2 import Cmd
    import cmd2
except:
    print "Installing cmd2 module from EPEL."
    os.system('yum install python-cmd2 -y')
    import cmd2
    from cmd2 import Cmd


class EucaREPL(Cmd):
    """Simple command processor example."""
    prompt = 'euca-tutorial$ '

    def preloop(self):
        print """ _______                   _
(_______)                 | |             _
 _____   _   _  ____ _____| |_   _ ____ _| |_ _   _  ___
|  ___) | | | |/ ___|____ | | | | |  _ (_   _) | | |/___)
| |_____| |_| ( (___/ ___ | | |_| | |_| || |_| |_| |___ |
|_______)____/ \____)_____|\_)__  |  __/  \__)____/(___/
                            (____/|_|
"""

    def do_EOF(self, line):
        'Exit for the tutorial by pressing Ctrl+d'
        print ''
        return True

    def do_help(self, arg):
        if len(arg) == 0:
            print "Welcome to Eucalyptus Faststart tutorial"
            print "In these tutorials you will learn how to use your"
            print "newly installed Eucalyptus cloud."
            return self.commands('')
        return cmd2.Cmd.do_help(self, arg    )

    def do_installimage(self, arg):
        '''Installs default image for the tutorial.
        It downloads the image using curl and then goes through the required steps to install it.'''
        install_image(self)

    def commands(self, line):
        """
        Show all available commands
        """
        names = [name[3:] for name in list(set(dir(self)) - set(dir(Cmd))) if name.startswith('do_')]
        names.append('help')
        names.sort()
        print self.colorize('Available commands: \n', 'blue')
        for name in names:
            print self.colorize(name, 'green')
        print ''

    def default(self, line):
        print "No such command, please check the help menu."

if __name__ == '__main__':
    EucaREPL().cmdloop()