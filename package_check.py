import sys
import subprocess
from logger import log

logger = log()

def execute(cmd):
    child = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return child.communicate()

def update_system():
    logger.info("Updating the system ...")
    cmd = ['sudo', 'apt-get', 'update']
    output, error = execute(cmd)
    if error:
        print(e)
        logger.error(e)
        sys.exit(1)
    else:
        print("System updated")
        logger.info("System Updated")

#update_system()
