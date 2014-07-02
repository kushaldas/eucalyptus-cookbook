import os
import sys
import time
from utils import system, pbold, find_tutorial_image

def cloudinit(self):
    "Starts a new instance with cloud init."
    words = None
    print "In this tutorial you will learn to use cloud-init to do certain"
    print "tasks when you instance boots for the first time."

    print self.do_pause("Press Enter to continue.")

    #print "Now we will try to find out any running tutorial instance and"
    #print "terminate it so that we can start a new instance."

    raw_text = '''#cloud-config
users:
  - default
  - name: foobar
    gecos: Foo B. Bar
    selinux-user: staff_u
    lock-passwd: false
    passwd: e79b8ad22b34a54be999f4eadde2ee895c208d4b3d83f1954b61255d2556a8b73773c0dc0210aa044ffcca6834839460959cbc9f73d3079262fc8bc935d46262

packages:
  - pss
  - htop
  - sl'''
    print raw_text
    print "\n\n"

    print "The above is the cloud-init example we will be using, it follows yaml format."
    print "The first part is adding a new user called foobar with hashed password foobar."

    print "Using packages list we are installing three tools in the instance from Fedora repository.\n"
    print "The file is located at /root/cloud.yaml\n"

    with open('/root/cloud.yaml', 'w') as fobj:
        fobj.write(raw_text)

    self.do_pause("Press Enter to continue.")

    words =  find_tutorial_image()
    if not words:
        return
    else:
        imageid = words[1]
        print "The following command will start an instance with EMI %s" % imageid

        cmd = "euca-run-instances -k my-first-keypair -f /root/cloud.yaml %s" % imageid
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
            print "Remember installing packages will take time based on your network speed.\n"
            print "You can monitor /var/log/messages file to know when the installation is done."
            print "After that try sl command."
            print "To know more about cloud-init visit http://cloudinit.readthedocs.org/en/latest/"

        else:
            print "There is some error in creating instance."
