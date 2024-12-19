import psutil
import subprocess
import time
from datetime import datetime

CPU_THRESHOLD = 85
MEMORY_THRESHOLD = 85
DISK_THRESHOLD = 85
CHECK_INTERVAL = 60
PING_HOST = "8.8.8.8"

def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > CPU_THRESHOLD:
        print(f"ALERT: High CPU usage detected: {cpu_percent}% (Threshold: {CPU_THRESHOLD}%)")

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    if memory_percent > MEMORY_THRESHOLD:
        print(f"ALERT: High memory usage detected: {memory_percent}% (Threshold: {MEMORY_THRESHOLD}%)")

def check_disk_usage():
    disk = psutil.disk_usage('/')
    disk_percent = disk.percent
    if disk_percent > DISK_THRESHOLD:
        print(f"ALERT: High disk usage detected: {disk_percent}% (Threshold: {DISK_THRESHOLD}%)")

def check_network_status():
    try:
        cmd = ['ping', '-c', '4', PING_HOST]

        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        output = result.stdout
        if "100% packet loss" in output:
            print(f"ALERT: No response from {PING_HOST}. Network unreachable.")

    except Exception as e:
        print(f"ERROR: {e}")
        
def log_system_status():
    print(f"\n--- System Status Report --- {datetime.now()}")
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_network_status()

def monitor_system():
    print("Starting system resource monitoring...")
    while True:
        log_system_status()
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_system()