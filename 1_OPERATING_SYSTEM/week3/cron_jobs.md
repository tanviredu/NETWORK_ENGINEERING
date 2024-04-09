Task Scheduling 

	1) CROND (Jobs at regular intervals. MOST POPULAR)
	2) ATD   (One off for Irregular task. )
	3) TIMER UNITS (NO NEED FOR ADDITIONAL SERVICES)


UNDERSTANDING CRON JOBS USING CRONTAB:

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed


	1) FIRST CHECK IF THE CRON SERVICE IS RUNNING 	   AND ENABLED
		
		=>sudo systemctl status cron
	
	2) OPEN A CRONTAB FOR ADDING THE COMMAND
		=> crontab -e

	3) GOTO TO CRON GURU ONLINE FOR CREATING CRON 
	   TIME USING THE NUMBER
	   THEN GIVE THE COMMAND 

	4) YOU CAN MONITOR THE JOBS USING 
		=> sudo journalctl -f




	5) TO CHECK YOU HAVE ANY CRON JOB OR NOT 
	   THE COMMAND IS 

	   => CRONTAB -L


	6) EASY METHOD

	FOR EVERY HOUR COMMAND
	@hourly <command>

	FOR EVERY REBOOT THIS COMMAND
	@reboot <command>


	
	