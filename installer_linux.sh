#!/bin/bash
adsimulator_PATH="$HOME/.adsimulator"

if ! [ -f "$adsimulator_PATH/enable_root.cfg" ] && [ $(id -u) = 0 ] ; then
	echo "ERROR: This script must NOT be run as 'root'"
	exit 1
fi

if ! [ $(uname) == "Linux" ] ; then
    echo "ERROR: This installation script is only for systems running a Linux distribution"
    exit 1
fi

if ! [ -d "$adsimulator_PATH" ] ; then
    mkdir $adsimulator_PATH
fi

if [ -d "$adsimulator/data" ] ; then
    rm -fr $adsimulator/data
fi

cp -r data $adsimulator_PATH

echo "File copied successfully!"
echo "Run:"
echo -e "\$ python setup.py install"