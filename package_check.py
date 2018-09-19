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

def pip_check():
    try:
        __import__('pip')
        print("Ok: pip is present")
        logger.info("Ok: pip is present")
    except ImportError:
        print("Installing pip ...")
        logger.info("Installing pip ..")
        cmd = ['sudo', 'apt-get', 'install', '-y', 'python3-pip']
        output, error = execute(cmd)
        if error:
            print(error)
            logger.error(rror)
        else:
            print("Ok: pip is installed.")
            logger.info("Ok: pip is installed")
    except Exception as e:
        print(e)
        logger.error(e)
        sys.exit(1)

def module_check():
    modules = ['pymysql']
    import pip
    for module in modules:
        try:
            __import__(module)
            print("Ok: {} is present".format(module))
            logger.info("Ok: {} is present".format(module))
        except ImportError:
            print("Installing module {}".format(module))
            logger.info("Installing module {}".format(module))
            pip.main(['install', module])
            print("Ok : {} is installed".format(module))
            logger.info("Ok : {} is installed".format(module))
        except Exception as e:
            print(e)
            logger.info(e)


#module_check()
#pip_check()           
#update_system()
