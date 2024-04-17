TASK1:
	GIVING COMPANY NAME:

		COMPANY NAME : OfficeSecuritySolution

TASK 2 :
	CREATING USERS:
		FOR EMPLOYEES
            => sudo mkdir -p /home/emp/johnEMP

			=> sudo useradd -m -d /home/emp/johnEMP johnEMP

			=> sudo passwd johnEMP
            
            => sudo mkdir -p /home/emp/emilyEMP
			
            => sudo useradd -m -d /home/emp/emilyEMP emilyEMP

			=> sudo passwd emilyEMP

		FOR INTERNS:
    		=> sudo useradd -m -d /home/intern/alexINT -e "$(date -d '+6 months')" alexINT

			=> sudo passwd alexINT

	        => sudo useradd -m -d /home/emp/lisaINT -e "$(date -d '+6 months')" lisaINT

			=> sudo passwd lisaINT

	CREATE GROUPS:
			=> sudo groupadd Employees
			=> sudo groupadd Interns


			ADDING EMPLOYEES AND INTERNS TO GROUP:
				=> sudo usermod -aG Employees johnEMP
				=> sudo usermod -aG Employees emilyEMP
			
			ADDING EMPLOYEES AND INTERNS TO GROUP:
				=> usermod -aG Interns alexINT
				=> usermod -aG Interns lisaINT


	CREATING DIRECTORIES:
			=> sudo mkdir -p /data/company_documents
			=> sudo mkdir -p /data/customer_information
			=> sudo mkdir -p /data/project_files

	CREATE SOME FILES INSIDE ALL THE DIRECTORIES
		   => sudo touch /data/company_documents/test1.txt
		   => sudo touch /data/company_documents/test2.txt
		   => sudo touch /data/project_files/test1.txt
		   => sudo touch /data/project_files/test2.txt
		   => sudo touch /data/customer_information/test1.txt
		   => sudo touch /data/customer_information/test2.txt


	AMONNG THREE FOLDER

		FULLTIME EMPLOYEE GROUP HAS FULL READ WRITE AND EXECUTE ACCESS TO THE
			1) customer_information
			2) project_files

		READ ACCESS TO
			1) company_documents

		INTERN GROUP HAVE  ACCESS TO 
		READ WRITE AND EXECUTE IN
			
			1) project_files

		AND READ AND EXECUTE ACCESS TO

			1) customer_information

		AND READ ACCESS TO
			1) company_documents


		AND SPECIAL PERMISSION (IMMUTABLE PERMISSION)
		TO
			1) company_documents



	ASSIGN OWNERSHIP AND GROUP FOR DIRECTORIES

		=> sudo chown :Employees /data/customer_information
		=> sudo chown :Employees /data/project_files
		=> sudo chown :Interns   /data/customer_information
		=> sudo chown :Interns   /data/project_files

	SETTING THE PERMISSION:

		READ WRITE AND EXECUTE FOR THE PERSON AND GROUP

		=> sudo chmod 770 /data/customer_information
		=> sudo chmod 770 /data/project_files

		READ AND EXECUTE PERMISSION FOR THE 
		company_documents

		=> sudo chmod 440 /data/company_documents


		SETTING Immutable permission for company_documents

		=> sudo chattr +i /data/company_documents



	 WE CREATE A NETWORK FILE SYSTEM FOR BACKUP
	 I ADDED A BACKUP SERVER
	 	IP      : 192.168.0.100
	 	SUBNET  : 255.255.255.0
	 	GATEWAY : 192.168.0.1

	 	IN THE SERVER INSTALL NFS

	 	=>	sudo apt update
	 	=>  sudo apt install nfs-kernel-server

	 ALLOW FIREWALL 
	 	=>  sudo ufw allow from 192.168.0.100/24 to any port nfs

	 START AND ENABLE THE SERVICE

	 	=> systemctl enable nfs-kernel-server
	 	=> systemctl start nfs-kernel-server

	 CREATE A DIRECTORY:
	 	=> mkdir /backup
	 	=> chmod 777 /backup

	 CHANGE THE CONFIGURATION
	 	=> vim /etc/exports

---------------------------------------------------
/backup		192.168.0.100/24(rw,sync,no_subtree_check)


---------------------------------------------------

	APPLY THE CHANGE

		=> exportfs -ra
		=> sudo systemctl restart nfs-kernel-server

	IN MACHINE

		=> sudo apt uppdate
		=> sudo apt install nfs-common

	MAKE A DIRECTORY
		=> sudo mkdir /localbackup
		=> sudo chmod 777 /localbackup	

	MOUNT NFS SERVER
		=> sudo mount 192.168.0.100:/backup /localbackup

	ADDING TO THE /etc/fstab file
---------------------------------------------------
192.168.0.100:/backup /localbackup nfs defaults 0 0
---------------------------------------------------

	CREATE THE BACKUP SCRIPT:
	=> touch /backup.sh
	=> chmod +x /backup.sh
---------------------------------------------------
#!/bin/bash

#CREATE ARCHIVE
=> tar -cf /tmp/backup.tar /data/company_documents data/customer_information /data/project_files
#COMPRESS IT
=> gzip /tmp/backup.tar
#COPY IT TO /localbackup
=> cp /tmp/backup.tar.gz /localbackup
#REMOVE THE TEMPORARY FILES
=> rm /tmp/backup.tar.gz

---------------------------------------------------


#CREATE A CORN JOB:
	=>crontab -e

-------------------------------------------

0 23 * * * /backup.sh

-------------------------------------------
