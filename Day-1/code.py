# Check Disk Usage
import shutil
import os
import subprocess

print("\n")
path = "/Users/tripurakant/Documents/"
stat = shutil.disk_usage(path)
print("Total disk usage is:", stat.total)
print("\n")
# Monitor Running Services
print("Runnning services are:")
try:
    services = subprocess.check_output("ps aux | head -n 6", shell=True).decode("utf-8")
    print(services)
except Exception as e:
    print("Error fetching services:", e)
# Assess Memory Usage
# Evaluate CPU Usage
# Send a Comprehensive Report via Email Every Four Hours
