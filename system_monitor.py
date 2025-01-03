import psutil

def monitor_resources():
    # CPU Usage
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
    
    # Memory Usage
    memory_usage = psutil.virtual_memory().percent
    print(f"Memory Usage: {memory_usage}%")
    
    # Disk Usage (Make sure you specify a directory like '/')
    disk_usage = psutil.disk_usage('/')
    print(f"Disk Usage: {disk_usage.percent}%")

if __name__ == "__main__":
    monitor_resources()

