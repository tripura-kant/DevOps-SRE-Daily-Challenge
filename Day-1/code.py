# Check Disk Usage
import shutil
import os
import subprocess
import psutil

print("\n")
path = "/Users/tripurakant/Documents/"
stat = shutil.disk_usage(path)
print("Disk usage is:", stat.total)
print("\n")
# Monitor Running Services
print("Runnning services are:")
try:
    services = subprocess.check_output("ps aux | head -n 6", shell=True).decode("utf-8")
    print(services)
except Exception as e:
    print("Error fetching services:", e)
# Assess Memory Usage
result = psutil.virtual_memory().percent
print("Ram is:", result)

# Evaluate CPU Usage
cpu_us = psutil.cpu_percent()
print("Cpu is:", cpu_us)

# Send a Comprehensive Report via Email Every Four Hours
