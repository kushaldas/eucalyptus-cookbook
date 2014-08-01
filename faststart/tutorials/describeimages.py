import os
import sys
from utils import color, system, pbold


def describe_images(self):
    words = None
    print pbold("Listing Images$")
    self.do_pause("Hit Enter to continue.")
    print "The fundamental building block of Eucalyptus is the image."
    print "We use a program called euca2ools to interact with those images."
    print ""
    print "In this tutorial, we're going to show you how to list"
    print "the images available to your Eucalyptus users."
    print ""
    self.do_pause("Hit Enter to continue.")

    print "Remember: when using Eucalyptus, you must \"log in\"."
    print "When using euca2ools, the way to \"log in\" is to source"
    print "the euca2ools credentials file. By default, Faststart"
    print "installs your credentials file in the root directory."
    print ""
    print pbold("source /root/eucarc")
    self.do_pause("\nHit Enter to run the command:")

    print pbold("+ source /root/eucarc")

    print "\nThe euca2ools command for listing images is " + pbold("euca-describe-images") + '.'
    print "If you have ever worked with Amazon Web Services, you will"
    print "notice that the command, and the output from the command, is"
    print "nearly identical to the comparable AWS command; this is by design."
    self.do_pause("Press Enter to run " + pbold("euca-describe-images") + " now.")

    print pbold("+ euca-describe-images")

    os.system("euca-describe-images")

    print "\nNow let's review some of the key output of that command:\n"

    out, err = system('euca-describe-images')
    lines = out.split('\n')
    for line in lines:
        if line.find('tutorial/fedora.raw.manifest.xml') != -1:
            words = line.split('\t')

    if words:
        imageid = words[1]
        imagepath = words[2]
        public = words[5]

        print pbold(imageid) + " is the " + pbold("image ID") +", which is used"
        print "to refer to the image by most other commands.\n"

        print pbold(imagepath) + " is the image path.\n"

        print pbold(public) +  " is the permission for this image. Images that"
        print "  are accessible to all users of this cloud are marked public; images that can"
        print "  only be run by the owner of the image are marked private.\n"

        print "To learn more about the euca-describe-images command, check out the documentaion:"
        print "  https://www.eucalyptus.com/docs/eucalyptus/3.4/index.html#euca2ools-guide/euca-describe-images.html"


def terminate_instances(self):
    'Tutorial for instance termination.'
    words = None
    data = None
    running_instances = []
    print ""
    print "In this tutorial, we're going to show you how to terminate"
    print "a running instance."
    print ""
    self.do_pause("Hit Enter to continue.")
    print "But before that we should learn how to find out more about the instances."
    print "The following command will give the us the information required."
    print pbold("\n+ euca-describe-instances\n")
    out, err = system("euca-describe-instances")
    print out

    self.do_pause('Press Enter to continue.')
    print "Let us learn a bit more about the output.\n"

    for line in out.split('\n'):
        if line.startswith('INSTANCE'):
            words = line.split('\t')
            if words[5] == 'running':
                running_instances.append(words)

    instances = {}
    for words in running_instances:
        instanceid = words[1]
        imageid = words[2]
        publicip = words[3]
        privateip = words[4]
        status = words[5]
        keypair = words[6]
        itype = words[9]

        print pbold(instanceid) + ' is running with public IP as ' + pbold(publicip) + ' and private IP as ' + pbold(privateip) \
            + " with a keypair called " + pbold(keypair) + ' and the instance type is ' + pbold(itype) + '.'
        instances[instanceid] = True
    print ""
    print "Now we can use " + pbold('euca-terminate-instances') + ' command to terminate any given instances.'


    while True:
        data = raw_input('Type in the instance id you want to terminate. Leave it blank to exit: ')
        data = data.strip()
        if not data:
            return
        if data not in instances:
            print "You have a typo in the instance id. Please try again."
            continue
        break

    print ""
    print "The following command will be used to terminate %s.\n" % data
    print pbold('+ euca-terminate-instances %s\n' % data)

    os.system('euca-terminate-instances %s' % data)

    self.do_pause('Press Enter to continue.')

    print '\nNow after some time use the euca-describe-instacnes command to see the instacne in terminated state.\n'
    print "To learn more about the euca-terminate-instances command, check out the documentaion:"
    print "  https://www.eucalyptus.com/docs/eucalyptus/3.4/index.html#euca2ools-guide/euca-terminate-instances.html\n"




