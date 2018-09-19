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
    logger.info(output)
    if error:
        print(e)
        logger.error(e)
        sys.exit(1)
    else:
        logger.info(output)
        print("System updated")
        logger.info("System Updated")

def pip_check():
    try:
        __import__('pip')
        print("Ok: pip is present")
        logger.info("Ok: pip is present")
    except ImportError:
        print("Installing pip ...")
        logger.info("Installing pip ...")
        cmd = ['sudo', 'apt-get', 'install', '-y', 'python3-pip']
        output, error = execute(cmd)
        logger.info(output)
        if error:
            print(error)
            logger.error(error)
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
            print("Installing module {} ...".format(module))
            logger.info("Installing module {} ...".format(module))
            pip.main(['install', module])
            print("Ok : {} is installed".format(module))
            logger.info("Ok : {} is installed".format(module))
        except Exception as e:
            print(e)
            logger.info(e)
            sys.exit(1)

def check_apache():
    cmd = ['sudo', 'service', 'apache2', 'status']
    output, error = execute(cmd)
    logger.info(output)
    if output:
       if "not-found" in str(output):
           print("Installing apache2 ...")
           logger.info("Installing apache2 ...")
           cmd = ['sudo', 'apt-get', 'install', 'apache2']
           output1, error1 = execute(cmd)
           logger.info(output1)
           if error1:
              print(error)
              logger.error(error)
           else:
              print("Ok: apache2 is installed")
              logger.info("Ok: apache2 is installed")
       else:
           print("Ok: apache2 is present")
           logger.info("Ok apache2 is present")

    if error:
        print(error)
        logger.info(error)

check_apache()
#module_check()
#pip_check()           
#update_system()
