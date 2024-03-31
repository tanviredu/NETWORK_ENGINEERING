## you have to install it with pip
import psutil
from humanize import naturalsize as nt
from humanize import naturaltime as ntime
## cpu_times
#print(psutil.cpu_times())

cpu_times = psutil.cpu_times().user

human_cpu_time = ntime(cpu_times)
print("CPU TIMES  : {}".format(human_cpu_time))

## disk usage
du = psutil.disk_usage("/")
#print(psutil.disk_usage("/home/tanvir/drive1/NETWORK_ENGINEERING"))

total = nt(du.total)
used  = nt(du.used)
free  = nt(du.free)

print("TOTAL SIZE : {}".format(total))
print("USED       : {}".format(used))
print("FREE       : {}".format(free))
print("USED in %  : {}%".format(du.percent))
