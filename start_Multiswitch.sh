#!/bin/bash

BASEDIR=`dirname $0`

echo $BASEDIR

#PYTHONPATH=$BASEDIR $BASEDIR/bin/ryu-manager --verbose --observe-links $BASEDIR/ryu/app/ForwardingMultiSwitch.py
PYTHONPATH=$BASEDIR $BASEDIR/bin/ryu-manager --observe-links $BASEDIR/ryu/app/ForwardingMultiSwitch.py

