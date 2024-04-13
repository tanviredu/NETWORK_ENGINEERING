#!/bin/bash

source /etc/os-release

INFO_HOSTNAME=$(hostname)
INFO_IP=$(hostname -i)
INFO_KERNEL=$(uname -r)
for i in {1..25} ; do
    echo -n =
done
echo
echo "HOSTNAME   : $INFO_HOSTNAME"
echo "IP ADDRESS : $INFO_IP"
echo "KERNEL     : $INFO_KERNEL"
echo "OS NAME    : $PRETTY_NAME"

for i in {1..25} ; do
    echo -n =
done
echo
