WORKING WITH SHUTDOWN REBOOT AND POWEROFF:
    FOR HALT IMMIDIATELY:
        1) sudo shutdown -h now
    FOR REBOOT IMMIDIATELY:
        2) sudo shutdown -r now 
    SHUTDOWN IN FUTURE:
        3) sudo shutdown -h +30 "The system will be shutdown within 30 min"
    CANCEL PENDING  SHUTDOWN :
        4) sudo shutdown -c

    POWEROFF COMMAND ALTERNATIVE
        1) sudo halt
        2) sudo poweroff
        3) sudo shutdown -h now
    FOR REBOOT
        1) sudo reboot

    CHECKING THE SERVER LOAD
        1) uptime


    HOW TO CHECK THE LOAD INCREASING??

    RUN THIS PYTHON SCRIPT:

    ---------------------------------------

    i = 1000
    mylist = []
    while True:
        value = 1000*i
        mylist.append(value)
        i = i+100
    -------------------------------------

    RUN THE CODE

    => python3 file.py &

    Then check with the command 

    => uptime




    IF YOU CREATE THE A FILE NAME nologin in /etc/directiony
    "/etc/nologin"
    then all the non root user cant login in the server
    only the root user can login and when you restart the 
    server it will delete the file automatically
    it is helpful when you do maintanace job in the linux server
    /etc/nologin
    file can be empty but if you want you can add content if you want


    After creating this file, any non-root user attempting to log in via SSH or any other means will receive the contents of the "nologin" file and will not be allowed to access the system. This can be useful for system administrators who want to temporarily prevent all regular users from logging in, for example, during maintenance or when performing critical system tasks.
    To allow non-root users to log in again, you can simply remove the "nologin" file from the /etc directory:



    
    

GRUB BOOTLOADER:
    GRUB STANDS FOR GRAND UNIFIED BOOTLOADER


    CONFIGURING GRUB
    
    1) sudo vim /etc/default/grub



WHAT HAPPEN IF YOU FORGOT YOUR ROOT PASSWORD
HOW TO BYPASS THE ROOT PASSWORD

    1) YOUR BOOTLOADER HAS TO BE EDITED SO THAT IT WILL SHOW THE MENU
       IN VAGRANT IT WONT SHOW THE MENU



    2) FIRST THING YOU HAVE TO HAVE PSHYCIAL ACCESS TO THE SERVER

    3) THEN WHEN WHEN THE BOOT SYSTEM LOAD YOU PRESS   e

    4)  IT WILL GIVE YOU TO THE EDIT PROCESS

    5)  GO WHERE THE WORD LINUX IS

    [LINUX /BOOT/VMLINUZ.5.4.**]

    ITS IN THE AREA WHERE THE KERNEL LOCATION IS SPECFIED. BUT YOU WILL SEE IT HAS SOME PARAMETER AFTER THE LOCATION. DELETE IT THEN ADD "rw init=/bin/bash"

    total command

    linux       /boot/vmlinuz-5.4.0-124-generic root=UUID=3ae-43-234234-234-23 rw init=/bin/bash

    HIT ENTER

    6) THE IT WILL DIRECTLY GET YOU A BASH SHELL

    7) passwd
    8) GIVE NEW PASWORD

    9) exec /sbin/init

    10) login again with new password


SETTING UP HOSTNAME:

    1) hostnamectl
    2) hostnamectl set-hostname "hostname"
    3) hostname
    4) cat /etc/hostname

SETTING UP TIME:
    
    1) timedatectl
    2) timedatectl set-time "yyyy-mm-dd HH:MM:SS"



MANAGING SYSTEMD AND SERVICE AND TARGETS:

SYSTEMD ECOSYSTEM

    -UNIFORMITY
    -ECO SYSTEM
    -SERVICES
    -TARGETS
    -LOGS
    -JOURNALCTL


