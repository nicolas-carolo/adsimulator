#!/bin/bash
ADSIMULATOR_PATH="$HOME/.adsimulator"

if ! [ $(uname) == "Darwin" ] ; then
    echo "ERROR: This installation script is only for systems running macOS"
    exit 1
fi

if ! [ -d "$ADSIMULATOR_PATH" ] ; then
    mkdir $ADSIMULATOR_PATH
fi

if ! [ -d "$ADSIMULATOR_PATH/adsimulator" ] ; then
    git clone https://github.com/nicolas-carolo/adsimulator $ADSIMULATOR_PATH/adsimulator
    cp -r $ADSIMULATOR_PATH/adsimulator/data $ADSIMULATOR_PATH
fi

cd $ADSIMULATOR_PATH/adsimulator
git_output=$(git pull)
if [ "$git_output" == "Already up to date." ]  ; then
    echo "adsimulator already up-to-date"
else
    touch $ADSIMULATOR_PATH/adsimulator_sw.lock
    echo "Latest version of adsimulator downloaded"
    echo "Run the following commands (be sure to use the Python 3 interpreter)"
    echo -e "\t$ pip install -r $ADSIMULATOR_PATH/adsimulator/requirements.txt"
    echo -e "\t$ cd $ADSIMULATOR_PATH/adsimulator"
    echo -e "\t$ python3 setup.py install"
    echo -e "\t$ rm $ADSIMULATOR_PATH/adsimulator_sw.lock"
    echo -e "\t$ adsimulator"
    if [ -d "$ADSIMULATOR_PATH/data" ] ; then
        rm -fr $ADSIMULATOR_PATH/data
    fi
    cp -r $ADSIMULATOR_PATH/adsimulator/data $ADSIMULATOR_PATH
fi
