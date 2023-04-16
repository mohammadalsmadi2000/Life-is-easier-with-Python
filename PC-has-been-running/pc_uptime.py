import psutil
import time

# Get the system boot time
boot_time = psutil.boot_time()

# Calculate the number of seconds since boot time
uptime = int(time.time() - boot_time)

# Calculate the number of hours, minutes, and seconds
hours, remainder = divmod(uptime, 3600)
minutes, seconds = divmod(remainder, 60)

# Print the uptime
print(f"The system has been running for {hours} hours, {minutes} minutes, and {seconds} seconds.")
