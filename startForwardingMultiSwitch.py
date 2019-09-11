#!/bin/bash

BASEDIR=`dirname $0`

echo $BASEDIR

#PYTHONPATH=$BASEDIR $BASEDIR/bin/ryu-manager --verbose --observe-links $BASEDIR/ForwardingMultiSwitch.py
PYTHONPATH=$BASEDIR $BASEDIR/bin/ryu-manager --observe-links --user-flags $BASEDIR/flagsForwardingMultiSwitch.py $BASEDIR/ForwardingMultiSwitch.py
#PYTHONPATH=$BASEDIR $BASEDIR/bin/ryu-manager --observe-links --user-flags $BASEDIR/flagsForwardingMultiSwitch.py --broadcast-to-localport $BASEDIR/ForwardingMultiSwitch.py
