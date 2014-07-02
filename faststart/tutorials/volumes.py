import os
import sys
import time
from utils import system, pbold, find_tutorial_image

def get_volume_details(cmd):
    out, err = system(cmd)
    volid = None
    status = None
    for line in out.split('\n'):
        tokens = line.split('\t')
        if len(tokens) >= 6:
            volid = tokens[1]
            status = tokens[5]
    return out, volid, status

def attachvolume(self):
    words = None
    print "\nIn this tutorial you will learn about volumes."
    print "How to create, attach and describe volumes."
    print "You need a running instance for this tutorial."
    self.do_pause('Press Enter to continue.')

    words = find_tutorial_image()
    if not words:
        return
    else:
        imageid = words[1]
        out, err = system('euca-describe-instances')
        lines = out.split('\n')
        for line in lines:
            tokens = line.split()
            if tokens[2] == imageid and tokens[5] == 'running': # We have our instance
                iid = tokens[1]
                ip = tokens[3]

                print "The following command will create a volume of 1GB size."
                cmd = 'euca-create-volume -z default --size 1'
                print pbold('+ ' + cmd)

                out, volid, status = get_volume_details(cmd)
                print out


                print "\nNow let's review some of the key output of that command:\n"

                print pbold(volid) + ' is the id of the volume we are creating.'
                print pbold('1') + ' is the size of the volume.'
                print pbold('default') + ' is the availability zone it is getting created.'
                print pbold(status) + ' is the status of the volume.'

                self.do_pause('\nPress Enter to continue.')

                print "Now wait till the volume gets created properly."

                for i in range(5):
                    time.sleep(15)
                    cmd = 'euca-describe-volumes %s' % volid
                    out, volid, status = get_volume_details(cmd)

                    if status == 'available':
                        break

                if status != 'available':
                    print "There are some issues in creating the volume"
                    return
                print "\nYour volume is created properly.\n"
                cmd = 'euca-attach-volume %s -i %s -d /dev/sdf' % (volid, iid)

                print "The following command will attach the volume to the running instance."

                print pbold("+ " + cmd)

                self.do_pause('Press Enter to continue.')

                out, err = system(cmd)

                print out
                print "\nThe volume will be attached to the running instance. Login to the"
                print "instance, become root and then you can access the volume as /dev/vdb"

                print "# mkfs.ext4 -p /dev/vdb"
                print "# mount /dev/vdb /mnt\n"



















