import os
import sys
import subprocess

class color(object):
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


def pbold(text):
    """
    Adds BOLD chars before and after the given text.
    :param text: Text to be printed
    :return: Text wirth bold chars.
    """
    return color.BOLD + text + color.END


def system(cmd):
    """
    Runs the cmd and returns output and error (if any).
    """
    ret = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    out, err = ret.communicate()
    return out, err