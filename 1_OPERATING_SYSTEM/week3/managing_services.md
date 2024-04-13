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


HOW A COMPUTER BOOT

    1) IN PHYSICAL DEVICE

    2) BIOS LOOK FOR BOOTABLE DISK

    3) IT RUN THE GRUB

    4) GRUB LOAD THE KERNAL

    5) KERNAL LOAD THE RAMFS  THE MINIMUM LIBRARY TO READ THROUGH THE FILE SYSTEM TO LOAD 
       ALL THE LIBRARIES

    6) THEN THE WHOLE SYSTEM LIGHT UP




TO SEE ALLT HE PROCESS WHICH IS BASE WHICH IS IN THE BRANCH USE COMMAND
    1) pstree

    IT IS SUSTEMD WHICH IS PID 1
    PID FOR PROCESS ID 1

    IT MAY SHOW INIT BUT IT IS JUST A LINK OF SYSTEMD


    1) systemd-analyze HOW MOW MUCH TIME IT WILL TAKE TO STARTUP



USING SYSTEMCTL TO MANAGE SERVICES
    
    EXAMPLE
    1) systemcrl status cron

    START AND ENABLE
    2) systemctl enable -now cron

    STOP AND DISABLE
    3) systemctl disable -now cron

    EDIT THE TARGET FILE

    4) systemctl edit cron --full

    SEE THE TARGET FILE
    5) systemctl cat cron




WHAT IS RUNLEVEL
    1) GRAPHICAL RUNLEVEL IS 5
    2) SERVER MULTIUSER BUT NO GRAPHICAL RUNLEVEL

    0 - Halt: The system is to be shut down.

    1 - Single User Mode: The system operates in a single-user mode without networking.

    2 - Multi-User Mode: The system is operational with multiple users, but without networking.

    3 - Multi-User Mode with Networking: The system is operational with networking support and multiple users.
    
    4 - Not used/User-definable: Historically, this runlevel was available for user customization.
    
    5 - Start GUI: The system starts the GUI (Graphical User Interface), typically the default runlevel for a desktop system.

    6 - Reboot: The system is to be rebooted.



    WHICH RUNLEVEL IS CURRENTLY USED
    
    1) runlevel

    GET THE DEFAULT RUNLEVEL

    2) systemctl get-default

    LIST ALL THE TARGET. REMEMBER ONE TARGET/UNIT CAN LOAD ANOTHER TARGET

    3) systemctl list-units --type target

    CHANGE MULTIUSER TARGET (RUNLEVEL 3)

    4) sudo systemctl isolate multi-user
    7) sudo systemctl set-default multi-user
    8) sudo systemctl get-default



LOGGING
    
    WE DONT NEED TO SEARCH DIFFERENT DIFFERENT LOG FILE .
    WE COULD JUST USE THE JOURNALCTL
    

    1) sudo jurnalctl

    LOG FOR SSH

    2) sudo journalctl --unit ssh

 
    WITH TIME

    3) sudo journalctl --unit ssh --since today


    IF WE WANT TO PERSIST THE LOGS

    4) sudo vim /etc/systemd/journald.conf
    5) storage=persistent
    6)systemctl restart systemd-journald

    PROCESS MONITORING
        FIND THE CPU LOAD

        1) uptime
        
        MONITORY UPTIME

        2) watch uptime
        
        PROCESS SORTED BY DIFFERENT PARAMETER

        3) top

        FIND THE PID OF ANY RUNNING PROCESS

        4) pgrep <service name>

        KILL PROCESS
        
        5) kill <PID>

        KILL WITH NAMES

        6) pkill <service name>

        FORCE KILLING PROCESS

        7) kill -9 <PID>


SEE THE TARGETS
    => ls /lib/systemd/system/*.target
SEE THE RUNLEVEL:
    =>runlevel

CHANGE IN RUNLEVEL:
    => telinit <number_od_run_level>
    
    IT WILL GOTO RESCUE MODE
    => telinit 1

MANAGING JOB STARTING,STOPPING,MONITORING,KILLING,BACKGROUND AND FOREGROUND

    =>sleep 300 &
    =>sleep 250 &
    =>sleep 200 &

VIEW PROCESS:
    => jobs
OR
    => ps 
TO KILL A PROCESS NUMBER 3 process:
    => kill &3

TAKE THE BACKGROUND JOB INTO FOREGROUND:
    FORGROUNDING THE 2ND JOB
    => fg &2  

SEE ALL THE PROCESS IN EVERY USER
    => ps -e

KILL PROCESS:
    FIRST FINDT THE PID using ps command
    THEN
    => KILL <process_id>

MANAGING TIMING OF THE JOBS:

INCREASE THE PRIORITY OF A JOB TO FINISH IN TIME

INFORMATION ABOUT PROCESS:
    => ps xl | less
    OR
    => top

LOOK FOR HIGHEST NICE VALUE

    IN THE PROCESS NICE VALUE THE LOWER THE MORE PRIORITY
    THE MORE NICE VALUE IS LESS PRIORITY

    FIRST CHECK THE NICE VALUE
    => top

    MAKE PROCESS:
    =>sleep 300 &

    SUPPOSE THE PID is x

    THEN
    => sudo top

    NOW RENICE IT

    HIT R

    THEN GIVE THE PID OF THE JOB YOU WANT TO RENICE
    THEN GIVE VALUE BETWEEN -20 - 19

    LESS NUMBER MORE PRIORITY MORE NUMBER LESS PRIORITY





    SENARIO :  YOUR MANAGER GIVE YOU A LIST OF JOB THAT IS CPU INTENSIVE AND TOLD YOU THAT THIS PROCESS SHOULD BE RUN AFTER THE WORKING HOUR . SO YOU NEED TO RUN SOME JOB WHICH IS NOT ATTACHED WITH A SHELL
    BECAUSE THE JOB HAS TO BE RUN AFTER YOU LOGOUT(AFTER OFFICE HOUR). THE PROCESS HAS TO RUN THE BACKGROUND

    => nohup <command>

    FOR EXAMPLE

    => nohup tar -cvf backup.tar /etc/

    NOHUP MEANS NO HANGUP
    IT WILL CONTINUE TO RUN PROCESSES EVEN AFTER YOU LOGGED OUT FROM THE SERVER. AND IT WILL STORE THE OUTPUT IN A FILE CALLED nohup.out



    SERVICES -> APPLICATION RUN IN THE BACKGROUND
    DAEMON -> APPLICATION RUN IN THE BACKGROUND AND DOES NTO ALLOW USER INTERFERE

    DAEMON AND SERVICES ARE FUNDAMENTALLY SAME.
    WINDOWS USERS CALL IT SERVICES AND LINUX USER
    CALL IR DAEMON

    LINE PRINTER DAEMON LPD

    INIT IS THE FIRST PROCESS

    RUNLEVEL IS A GROUP OF PROCESS IN LINUX COMMAND

    SWITCH RUNLAVEL WITH TELINIT COMMAND

    COMPUTER SEARCH FOR BOOTLOADER
    WHEN BOORITN

    GRUB IS THE LINUX BOOTLOADER WHICH LOAD THE KERNEL

    SHUTODWN -t <SECOND>

    HOW MANY SECOND AFTER THE OS SHUTDOWN


    RUNING PROGRAM IS PROCESS

    PROCESS HAS PID

    THERE IS FOREGROUND AND BACKGROUND PROCESS

    RUNNING MORETHAN 1 PROCESS IS MULTITASKING

    THERE CAN BE 1 FOREGROUND PROCESS


    LOOK USERS SPECFIC PROCESS

    WITH jobs COMMAND

    STATE OF JOBS

    RUNNING    ACTIVE
    STOPPED    SUSPENDED
    TERMINATED KILLED
    DONE       COMPLETED

    IF YOU RUN bg COMMAND THE SUSPENDED JOBS CAN RESUME
    THE fg COMMAND TO COME TO FOREGROUND

    TERMINATED JOBS CANT BE RESUME

    CHILD PPROCESS

    A PROCESS CAN GENERATE ANOTHER PROCESS IS CALL CHILD
    PROCESS

    TO VISUALIZE IT YOU CAN USE THE pstree
    COMMAND

    KILL PROCESS KILL PSKILL

    TOP COMMAND 
    NICE ,RENICE -20 HIGHST 19 LOWEST


    CRON JOB TO SCHEDULE JOBS
    AT COMMAND TO SET A COMMAND A SPECFIC TIME

    CLOCKDRIFT SYSTEM CLOCK SHOWS DIFFERENT THAN HARDWARE CLOCK

    NTP NETWORK TIME PROTOCOL FOR SERVING TIME INFORMATION
    







