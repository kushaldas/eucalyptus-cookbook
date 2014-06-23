import os
import sys
import time
from utils import color, system, pbold


def launchinstances(self):
    print "\nIn this tutorial you will learn how to start a new instace from the"
    print " image we installed in the last tutorial."
    self.do_pause("Press Enter to continue.")
    out, err = system('euca-describe-images')
    lines = out.split('\n')
    for line in lines:
        if line.find('tutorial/fedora.raw.manifest.xml') != -1:
            words = line.split('\t')

    if not words:
        print "Unable to find the Fedora machine image. Use this command to install it:"
        print "  installimage\n"
        print "Exiting..."
        return

    else:
        imageid = words[1]
        print "The following command will start an instance with EMI %s" % imageid

        cmd = "euca-run-instances -k my-first-keypair %s" % imageid
        print pbold("+ " + cmd)

        out, err = system(cmd)
        lines = out.split('\n')
        line = lines[1]
        words = line.split()

        print out

        print "Capturing the instance ID and the public ip address"
        if words:
            instanceid = words[1]
            instanceip = words[3]
            status = words[5]

        # check for 30 seconds
        i =  0
        print "Waiting for your instance to start.\n"
        while status == 'pending':
            if i == 6:
                break
            i = i + 1
            time.sleep(5)
            out, err = system('euca-describe-instances ' + instanceid)
            lines = out.split('\n')
            line = lines[1]
            words = line.split()

            if words:
                instanceid = words[1]
                instanceip = words[3]
                status = words[5]

        if status == 'running':
            print "Use this command to log into your new instance\n."
            print " ssh -i ~/my-first-keypair.pem fedora@%s\n" % instanceip
            print "Next you should learn how to get the description of your instances using describeinstance tutorial command.\n"

        else:
            print "There is some error in creating instance."
