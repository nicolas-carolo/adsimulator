#!/bin/bash
adsimulator_PATH="$HOME/.adsimulator"

if ! [ $(uname) == "Darwin" ] ; then
    echo "ERROR: This installation script is only for systems running macOS"
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