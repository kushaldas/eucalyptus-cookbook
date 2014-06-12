import cmd
import subprocess

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def install_image():
    print "\n"
    print "The default image installed by Faststart is small, and"
    print "not useful for much beyond demonstrating how images work."
    print ""
    print "In this tutorial, we will download a cloud image"
    print "from the internet and install it on your Faststart"
    print "cloud."
    print ""
    print "Hit Enter to continue."
    try:
        raw_input()
    except (KeyboardInterrupt, SystemExit):
        print color.BOLD + color.RED + "Stoping the tutorial as you pressed Ctrl+c" + color.END
        return
    print "Many Linux distributions now have preconfigured cloud images, so"
    print "you can download and install them to your cloud easily. For this"
    print "tutorial we will add a Fedora 20 cloud image to your cloud."
    print ""
    print "First, we will download and the image with curl. Eucalyptus"
    print "accepts raw images by default, so we will download a"
    print "compressed, raw image."
    print ""
    print "Hit Enter to download the image with curl. (Note: it may take a while.)"
    try:
        raw_input()
    except (KeyboardInterrupt, SystemExit):
        print color.BOLD + color.RED + "Stoping the tutorial as you pressed Ctrl+c" + color.END
        return

def system(cmd):
    """
    Runs the cmd and returns output and error (if any).
    """
    ret = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    out, err = ret.communicate()
    return out, err

class EucaREPL(cmd.Cmd):
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

    def do_greet(self, line):
        print "hello"

    def do_EOF(self, line):
        'Exit for the tutorial by pressing Ctrl+d'
        print ''
        return True

    def do_help(self, arg):
        print "Welcome to Eucalyptus Faststart tutorial"
        print "In these tutorials you will learn how to use your"
        print "newly installed Eucalyptus cloud."

        if len(arg) == 0:
            return cmd.Cmd.do_help(self, '')
        return cmd.Cmd.do_help(self, arg    )

    def do_installimage(self, arg):
        'Installs default image for the tutorial.'
        install_image()

if __name__ == '__main__':
    EucaREPL().cmdloop()