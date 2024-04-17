WHAT IS FILESYSTEM?

	FILESYSTEM IS A METHOD THAT IS USED BY AN OS TO STORE, RETIEVE ORGANIZE AND MANAGE FILES AND DIRECTORIES ON MASS STORAGE DEVICE.

	STORAGE DEVICE > FILE SYSTEM

	FILESYSTEM HOLDS
		1) INFORMATION, DATEOF CREATION AND MODIFICATION
		   OF INDIVIDUAL FILES, FILE SIZAE, FILE TYPE, FILE PERMISSION

		2) PROVIDE STRUCTURED FROM FOR DATA STORAGE

	FILE SYSTEM LABELS ASSIGNED FOR EASY IDENTIFICATION. LABEL MAY BE UP TO 16 CHARACTER LONG AND CAN BE DISPLAYED OR CHANGED USING 

	=>e2label 
	
	OR
	
	=>tune2fs -L

	COMMAND



	FILE SYSTEM EXT4 THE NEWEST FILE SYSTEM FOR LINUX DISTRINUTION BACKWARDS COMPATABLE FOR EXT3 AND EXT2
	EXT4 SUPPORTS JOUIRNALING. SUPPORT VOLUME UP TO 1 EXABYTE AND FILES UP TO 16 TIB, EXT4 IS THE DEFAULT FILE SYSTEM FOR CENTOS/RTEDHAT7 AND UBUNTU

	SWAP IS NOT A TRUE FILE SYSTEM. BUT RATHER A PORTION OF THE HARD DISK THAT IS USED IN SITUATION WHEN LINUX IS OUR OF RAM SPACE AND NEEDS MORE OF IT. LINUX THEN PUSHES SOME UNUSED FILES TO SWAP SPACE TO FREE MEMORY
	THIS TYPE OF OPERATION IS SLOWER.


	PARTITIONS

		A PARTITION IS A SECTION OF THE HARD DISK THAT IS LOGICALLY ACTS AS S SEPARATE DISK. PARTITION CONVERT A LARGE HARD DISK TO SMALLER ,MANAGABLE CHUNKS, LEADING TO BETTER ORGANIZATION OF INFORMATION. a PARTITION MUST BE FORMATTED AND ASSIGNED A FILESYSTEM BEFORE DATA CAN BE STORED.
		PARTITION ARE IDENTIFIED USING PARTITION TABLE, WHICH IS STORED IN THE BOOT RECORD.
		PARTITION CAN HAVE FOUR PROIMARY POARTITION

	HARD DISK SECFICATION


	/      MINIMUM 1 GB
	
	/BOOT  100MD
	
	SWAP   DOUBLE OF THE RAM SIZE
	
	/VAR   MINIMUM 250MB. DEPENDING ON THE AMOUNT OF THE 		SOFTWARE YOU WANT TO INSTALL

	/HOME VARIES BASED ON THE NUMBER OF USER


	PARITTION TYPE

	PRIMARY      FOUR PRIMARY PARTITION IS ALLOWED. ONE 			 PARTITION CAN CONTAIN ONE FILE SYSTEM 				 AND IT IS CALLED AS VOLUMES



	EXTENDED 	 AN EXTENDED PARTITION CAN CONTAIN 					 SEVERAL FILESYSTEM. WHICH ARE REFER TO 			 AS LOGICAL FILE SYSTEM. THERE CAN BE ONE 			   EXTENDED PARTITION WHICH IS FURTHER      SUBDIVIDED.  THIS IS A CONTAINER OF 				 			  LOGICAL PARTITION SO IT DOES NOT DIRECTLY 				HOLD ANY DATA. 


	LOGICAL      LOGICAL PARTITION IS CREATED WITHIN AN EXTENDED PARTITION. THERE IS NO RESTRICTION ON THE NUMBER OF LOGICAL PARTITION. BUT IS IS ADVISABLE TO LIMIT TO 12 LOGICAL PARTITION PER DISK DRIVE

EVERYTHING IN LINUX IS A FILE


	MOUNT POINTS:
		A MOUNT POINT IS AN ACCESS POINT TO INFORMATION STORED ON A LOCAL OR REMOTE STORAGE DEVICES. THE MOUNT POINT IS TYPICALLY AN EMPTY DIRECTORY ON WHICH A FILESYSTEM IS LOADED, OR MOUNTED. IF THE DIRECTIORY ALREADY HAS CONTENT. THE CONTENT BECOME INVISIBLE TO USERS UNTILL TRHE MOUNTED FILESYSTEM IS UNMOUNTED.

	YOU CAN USE /ETC/FSTAB FILE TO MOUNT FILESYSTEM ON BOOT TIME



	JOURNALING FILE SYSTEM:
		WHAT IS JOURNALING FILE SYSTEM?
		IT IS A METHOD USED BY AN OPERATING SYSTEM TO QUICKLY RECOVER AFTER AN UNEXPECTED INTERRUPTION SUCH AS SYSTEM CRASH. JOURNALING CAN REMOVE THE NEED FOR A FILE SYSTEM CHECK WHEN SYSTEM BOOTS. IN THE JOURNALING FILE SYSTEMS,
		THE SYSTEM DOES NOT WRITE MODIFIED FILES DIRECTLY ON THE DISK, INSTEAD A JOURNAL IS MAINTAINED

		IT WORKED LIKE:

		1) THE JOURNAL DESCRIBES ALL THE CHANGES THAT MUST BE MADE TO THE DISK

		2) A BACKGROUND PROCESS MAKE THA CHANGE OF ACCORDING TO THE JOURNAL INSTRUCTION

		3) IF THE SYSTEM SHUTS DOWS, PENDING CHANGES ARE PERFORMED WHEN IS REBOOTED

		4) INCOMPLETED ENTRIES IN THE JOURNAL ARE DISCARDED




		JOURNAL FILE SYSTEM WORKS WITH SMALL FILES AND SMALL DRIVES. THE POOR PERFORMANCE REASON

		1) FILESYSTEM RECOVERY TIME AFTER POWER FAILURE OR IMPROPER SHUTDOWN
		2) BITMAP METHOD OF TRACKING THE FILE SYSTEM
		3) WASTED SPACE AND FRAGMENTATION

	HOW TO CHECK THE FILE SYSTEM AND REPAIR IT
	TO CHECK THE FILE SYSTEM AND REPAIR USE THIS COMMAND

	=>sudo fsck -t <file_system_type> <block_device>

	EXAMPLE:

	=> sudo fsck -t ext4 /dev/sdc1


	HOW TO REPAIR

	=>sudo fsck -r  <block_device>

	EXAMPLE:

	=> sudo fsck -r  /dev/sdc


	ANOTHER COMMAND TO ADD JOURNALING TO THE FILE SYSTEM IS

		=> tune2fs


	CHANGE LABEL WITH
	=>e2label
	COMMAND

	PRIMARY PARTITION 4
	EXTENDED PARTITION 1
	UNDER EXTENDED THERE ARE LOGICAL PARTITION

	/FSTAB CAN ONLY EDITED BY ROOT AND ITS WORK IS TO MOUNT ON BOOT


	SWAP ON AND OFF USING THIS COMMMAND

	=>swapon
	=>swapoff




WHAT IS BLOCK DEVICE
LIST ALL THE BLOCK DEVICE

=> lsblk
=> lsblk -f



LOGGING:
	SYSTEM LOGS

	SYSTEM LOGS ARE RECORDS OF SYSTEM ACTIVITIES THAT ARE TRACKED AND MAINTAIN BY THE SYSLOGD SERVICE/DAEMON. SYSTEM LOGS ARE USUALLY STARTED AT BOOT TIME.
	IT INCLUDES
		1) DATE
		2) PROCESS THAT DELIVERED THE MESSAGE
		3) THE ACTUAL MESSAGE

	LOG MESSAGE ARE STORED IN THE /VAT/LOG DIRECTORY.
	THE MAIN LOG FILE IS /VAT/LOG/MESSAGE.

	SOME SERVICE CAN CREATE THEIR OWN LOG FILE


AUTOMETIC ROTATION
	
	AUTOMATIC ROTATION IS A SYSTEM OF REGULAR ROTATION OF LOGS TO MAINTAIN A MINIMUM LOG FILE SIZE. THE 
	=> logrotate 
	UTILITY USED TO PERFORM AUTOMETIC ROTATION. WHEN EXECUTED
	=> logrotate ADDS .1 TO THE END OF THE NAME OF THE CURRENT VERSION OF THE LOG FILE.pREVIOUSLY ROTATED FILES ARE SUFFIXED WITH .2 .3 AND SO ON . OLDER LOGS HAVE LARGER NUMBER ON THEIR FILE NAMES. LOG FILE CAN BE ROTATED ON A DAILY WEEKLY OR MONTHLY BASIS. AUTOMATIC ROTATION SAVE DISK SPACE BECAUSE OLDER LOGS ARE PUSHED OUT WHEN SIZE LIMIT IS REACHED. OTHERWISE COMPUTER RUNS OUT OF SPACE ON THE HARD DRIVE AND WILL CRASH




CREATE A CENTRAL LOGGIN SERVER:
	WE CAN MAKE A COMPUTER IN A NETWORK AS A CENTRAL LOGGING SERVER. REMEMBER LOGGIN SERVER ACCEPT UDP CONNECTION JUST LIKE THE DNS SERVER. 

	IN THE SERVER SIDE FIRST WE INSTALLL. IF NOT ALREADY INSTALLED YOU HAVE TO INSTALL THE PACKAGE
		=> sudo apt install rsyslog


	NOW WE EDIT THE CONFIGURRATION FILE

	=> sudo vim /etc/rsyslog.conf

	NOW UNCOMMENT THE LINE IN THE FILE

	$ModLoad imudp
	$UDPServerRun 514

	RESTART THE SERVICE

	=> sudo systemctl restart rsyslog


	YOU MIGHT NEED TO ALLOW THE 514 PORT

	=> sudo ufw allow 514/udp
	=> sudo ufw reload

NOW IN THE CLIENT MACHINE
	1) INSTASLL THE rsyslog PACKAGE IN THE JUST LIKE THE SERVER

	2) IF YOU WANT TO SEND ALL THE LOG IN THE SERVER IN THE NETWORK

	=> *.* @<SERVER_ip>:514

	EXAMPLE:

	=> *.* @192.168.0.100:514