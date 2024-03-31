import psutil
import os
import platform
import time
import subprocess
import socket
from prettytable import PrettyTable
from humanize import naturalsize as ns


while True:
    subprocess.call("clear")
    print("================= SERVER HEALTH ===================")
    print("OS TYPE          : {}".format(os.name))
    print("OPERATING SYSTEM : {}".format(platform.system()))
    print("OS VERSION       : {}".format(platform.release()))
    print("OS ARCHITECTURE  : {}".format(platform.architecture()))
    print("COMPUTER NAME    : {}".format(platform.node()))
    hostname = platform.node()
    IPAddress = socket.gethostbyname(hostname)
    print("IP ADDRESS       : {}".format(IPAddress))
    print("---------------------------------------------------")
    print("================= NETWORK STATUS ==================")
    table = PrettyTable(["NETWORK","STATUS","SPEED"])
    data = psutil.net_if_stats()
    for key in data.keys():
        name = key
        up = "UP" if data[key].isup else "DOWN"
        speed = data[key].speed
        table.add_row([name,up,speed])

    print(table)
    print("\n")
    print("-----------------------------------------------------")
    print("================== RAM INFORMATION ==================")
    raminfo = psutil.virtual_memory()
    memory_table  = PrettyTable(["TOTAL","USED","AVAILABLE","PERCENTAGE"])
    RAM_TOTAL     = ns(raminfo.total)
    RAM_USED      = ns(raminfo.used)
    RAM_AVAILABLE = ns(raminfo.available)  
    RAM_PERCENT   = "{}%".format(raminfo.percent)
    memory_table.add_row([RAM_TOTAL,RAM_USED,RAM_AVAILABLE,RAM_PERCENT])
    print(memory_table)

    print("------------------------------------------------------")
    print("=================== TOP 10 PROCESSES =================")
    all_processed = psutil.process_iter(attrs=["pid","name","cpu_percent"])
    processes = sorted(all_processed,key=lambda x:x.info['cpu_percent'],reverse=True)[:10]
    table = PrettyTable(["PID","NAME","CPU %"])

    for p in processes:
        table.add_row([p.info['pid'],p.info['name'],p.info['cpu_percent']])
    print(table)

    time.sleep(1)
