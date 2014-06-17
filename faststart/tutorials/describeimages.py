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
    print "Hit Enter to continue."

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