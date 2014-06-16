import os
import sys
from utils import color, system, pbold

def install_image(self):
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
    print color.BOLD + "curl http://mirror.fdcservers.net/fedora/updates/20/Images/x86_64/Fedora-x86_64-20-20140407-sda.raw.xz > fedora.raw.xz" + color.END
    ret = os.system("curl http://mirror.fdcservers.net/fedora/updates/20/Images/x86_64/Fedora-x86_64-20-20140407-sda.raw.xz > fedora.raw.xz")

    if ret != 0:
        print "======"
        print "[OOPS] Curl failed!"
        print ""
        print "It appears that curl failed to fetch the image. Please check"
        print "your network connection and try the tutorial again."
        print ""
        print "Exiting..."
        os.system('curl --silent "https://www.eucalyptus.com/faststart_errors.html?/msg=TT_DOWNLOAD_IMAGE_FAILED&uuid=$uuid" >> /dev/null')
        sys.exit(1)

    print "\nOK, now let's unzip the image. This image is zipped in the xz"
    print "format, so to unzip the image, we will use the ${bold}xz${normal} command."
    print ""
    print "Hit Enter to unzip the image. (This may also take a bit.)"

    raw_input()

    print "+ " + color.BOLD + "xz -d fedora.raw.xz" + color.END
    os.system("xz -d fedora.raw.xz")


    print "\nOK, now you are ready to install the image into your cloud."
    print "To install the image, we will run the following command:"
    print ""
    print color.BOLD + "euca-install-image -n Fedora20 -b tutorial -i fedora.raw -r x86_64 --virtualization-type hvmcolor.END\n"
    print color.BOLD+ "-n Fedora20"+ color.END + " specifies the name we're giving the image."
    print color.BOLD+"-b tutorial" + color.END + " specifies the bucket we're putting the image into."
    print color.BOLD+"-i fedora.raw" + color.END + " specifies the filename of the input image."
    print color.BOLD+"-r x86_64" + color.END + " specifies the architecture of the image."
    print color.BOLD + "--virtualization-type hvm" + color.END + " means that we're using a native hvm image.\n"
    print "Hit Enter to install the image."

    raw_input()

    print "+ " + pbold("euca-install-image -n Fedora20 -b tutorial -i fedora.raw -r x86_64 --virtualization-type hvm")
    ret = os.system("euca-install-image -n Fedora20 -b tutorial -i fedora.raw -r x86_64 --virtualization-type hvm")
    if ret != 0:
        print "======"
        print "[OOPS] euca-install-image failed!"
        print ""
        print "It appears that Eucalyptus failed to install the image. You may want to"
        print "check to see if you have enough disk space to install this image."
        print ""
        print "Exiting..."
        os.system('curl --silent "https://www.eucalyptus.com/faststart_errors.html?/msg=TT_INSTALL_IMAGE_FAILED&uuid=$uuid" >> /dev/null')
        sys.exit(1)

    print "\nBy default, your machine images are visible only to you. You may"
    print "easily make images available to other cloud users. Let's make"
    print "your new image available to all users of this cloud."
    print ""


    out, err = system('euca-describe-images')
    lines = out.split('\n')
    emid = None
    for line in lines:
        if line.find('tutorial/fedora.raw.manifest.xml') != -1:
            emid = line.split('\t')[1]
    if not emid:
        print "Can not find installed tutorial image."
        return
    command = "euca-modify-image-attribute -l -a all %s" % emid
    print "+ " + pbold(command)

    self.do_pause("Hit Enter to modify the image attribute.")
    os.system(command)

    print "\nYour new Fedora machine image is installed and available to all"
    print "users on your cloud! Let's confirm that by running euca-describe-images"
    print "one more time."
    self.do_pause("Hit Enter to show the list of images.")

    os.system("euca-describe-images")