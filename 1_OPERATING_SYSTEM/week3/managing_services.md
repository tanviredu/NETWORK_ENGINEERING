WORKING WITH SHUTDOWN REBOOT AND POWEROFF:
    FOR HALT IMMIDIATELY:
        1) sudo shutdown -h now
    FOR REBOOT IMMIDIATELY:
        2) sudo shutdown -r now 
    SHUTDOWN IN FUTURE:
        3) sudo shutdown -h +30 "The system will be shutdown within 30 min"
    CANCEL PENDING  SHUTDOWN :
        4) sudo shutdown -c
    
    




SETTING UP HOSTNAME:

    1) hostnamectl
    2) hostnamectl set-hostname "hostname"
    3) hostname
    4) cat /etc/hostname

SETTING UP TIME:
    
    1) timedatectl
    2) timedatectl set-time


