#!/bin/bash
PWD_OK="false"
SALT="Thisissecretsalt" 
while [ "$PWD_OK"!="true" ] ; do
    # Number of the argument can be count 
    # by $#
    #read -sp 'Enter a new Password:'
    if [[ $# -ne 1 ]] ; then
        echo "Enter a new password"
	read -s
	
    else
	REPLY="$1"
    fi
    echo
    PWD_LEN=$(echo -n "$REPLY" | wc -m)
    PASSWORD=$(openssl passwd -6 --salt "$SALT" "$REPLY")
    if [ "$PWD_LEN" -gt 6 ] ; then
        PWD_OK="true"
	echo "$PASSWORD"
	exit 1
    else
        echo "password to short"
	echo
        exit 1
    fi
done
