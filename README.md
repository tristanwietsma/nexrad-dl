nexrad-dl
=========

From [Wikipedia](http://en.wikipedia.org/wiki/NEXRAD

> NEXRAD or Nexrad (Next-Generation Radar) is a network of 159 high-resolution S-band Doppler weather radars operated by the National Weather Service, an agency of the National Oceanic and Atmospheric Administration (NOAA) within the United States Department of Commerce. Its technical name is WSR-88D, which stands for Weather Surveillance Radar, 1988, Doppler. NEXRAD detects precipitation and atmospheric movement or wind. It returns data which when processed can be displayed in a mosaic map which shows patterns of precipitation and its movement. The radar system operates in two basic modes, selectable by the operator – a slow-scanning clear-air mode for analyzing air movements when there is little or no activity in the area, and a precipitation mode, with a faster scan for tracking active weather. NEXRAD has an increased emphasis on automation, including the use of algorithms and automated volume scans.

nexrad-dl is a download agent that syncs a local copy of the daily precipitation files with NEXRAD's FTP site. File formats include shape and netCDF.

Requirements
------------

nexrad-dl was developed and tested using the following configuration:

* Python 2.7.3rc2

* BeautifulSoup 3.2.1

Installation
------------

Installation on Linux is pretty easy and customizable.

Clone the repository:

    cd <wherever you like to store git repos>
    git clone git@github.com:tristanwietsma/nexrad-dl.git

Create a cache (directory) to store the precipitation files. This can be anywhere on the file system that is accessible from the account that will execute nexrad-dl. After the cache has been created, you need to set an environment variable so that nexrad-dl can find it.

    cd <wherever you want to store the cache>
    mkdir nexrad-cache
    cd nexrad-cache
    echo "export NEXRAD_CACHE=`pwd`" >> ~/.bashrc

Now, you can run nexrad-dl.py and it will synchronize your cache with the FTP site. Set it up on cron and you can keep the cache up to date automatically.

    python nexrad-dl.py

Enjoy! If you see any opportunities for improvement, please send me a pull request.
