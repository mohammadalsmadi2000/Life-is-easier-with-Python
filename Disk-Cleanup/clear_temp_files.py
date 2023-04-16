import os
import subprocess

# run the Disk Cleanup utility
subprocess.run('cleanmgr.exe /sagerun:1', shell=True)

# delete remaining temporary files
temp_folder = os.environ.get('TEMP')
subprocess.run(f'rd /s /q "{temp_folder}"', shell=True)
subprocess.run(f'mkdir "{temp_folder}"', shell=True)

print('Temporary files have been cleared.')
