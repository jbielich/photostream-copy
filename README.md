# Prerequisites

You need to install gntp <https://github.com/kfdm/gntp/>


# Usage

Run the script with the target directory. In my case, I use Dropbox (for auto-backup until I can get to processing them):

    ./photostreamcopy.py ~/Dropbox/Photos/inbox

A hidden file will be created in your target directory in this format: `.YYYYMMDD.HHMMSS`  

This will be the date of the modification date of the latest image in the photostream sub-directories. Each successive run, it will auto-update the filename to the latest modification date. This way, you only copy the latest files over, even if you move the copied images out of your target directory. No cruft for you!

This will let you also manually set the date from which to copy, if you have to:

    touch .20100923.000000


# Automatic Running

You can set it to auto-run via cron, or launchd. Just be sure to specify the target directory. Personally, I set it up via a Hazel rule, so I can get it as soon as my Mac receives it from Photostream:

Add the Hazel rule to your Photostream directory:

    /Users/YOUR_USERNAME/Library/Application Support/iLifeAssetManagement/assets/sub

![](http://farm9.staticflickr.com/8282/7708254120_d3bdcdc1f0.jpg)


![](http://farm8.staticflickr.com/7251/7708205478_5f33d46e16.jpg)


