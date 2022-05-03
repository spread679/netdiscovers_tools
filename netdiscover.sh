#!/bin/bash
#
# discover other hosts in your network
#
if [ -z $1 ]
then
    echo [-] You need to add the part of your network.
    echo [+] For example run: ./netdiscover.sh 10.0.1
else
    for i in `seq 1 1 254`
    do
        result=`ping -c 1 $1.$i | grep '64 bytes' | cut -d ' ' -f 4 | sed 's/://'`
        if [ $result ]
        then
            echo [+] $result
        fi
    done
fi 
