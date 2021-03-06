import os
import sys
import subprocess
from logger import log

logger = log()

def execute(cmd):
    child = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return child.communicate()

def update_system():
    print("Updating the system ...")
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
    modules = ['pymysql', 'psutil']
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
           cmd = ['sudo', 'apt-get', 'install', '-y', 'apache2']
           output1, error1 = execute(cmd)
           logger.info(output1)
           if error1:
              print(error1)
              logger.error(error1)
              sys.exit(1)
           else:
              print("Ok: apache2 is installed")
              logger.info("Ok: apache2 is installed")
       else:
           print("Ok: apache2 is present")
           logger.info("Ok apache2 is present")

    if error:
        print(error)
        logger.error(error)
        sys.exit(1)

def check_php():
    cmd = ['which', 'php']
    output, error = execute(cmd)
    logger.info(output)
    if output:
        print("Ok: php is present")
        logger.info("Ok: php is present")
    else:
        print("Installing php ...")
        logger.info("Installing php ...")
        cmd = ['sudo', 'apt-get', 'install', '-y', 'php']
        output1, error1 = execute(cmd)
        logger.info(output1)
        if error1:
            print(error1)
            logger.error(error1)
            sys.exit(1)
        print("Ok: php is installed")
        logger.info("Ok php is installed")

def php_mysql():
    print("Installing php-mysql ...")
    logger.info("Installing php-mysql ...")
    cmd = ['sudo', 'apt-get', 'install', '-y', 'php-mysql']
    output1, error1 = execute(cmd)
    logger.info(output1)
    if error1:
        print(error1)
        logger.error(error1)
        sys.exit(1)
    print("Ok: php-mysql is installed")
    logger.info("Ok php-mysql is installed")


def check_mysql():
    cmd = ['sudo', 'service', 'mysql', 'status']
    output, error = execute(cmd)
    logger.info(output)
    if output or "mysql.service could not be found" in str(error):
       if "not-found" or "mysql.service could not be found" in str(output):
           print("Installing mysql-server ...")
           logger.info("Installing mysql-server ...")
           os.system('./set_root_pass.sh')
           cmd = ['sudo', 'apt-get', 'install', '-y', 'mysql-server-5.7']
           output1, error1 = execute(cmd)
           logger.info(output1)
           if error1:
              print(error1)
              logger.error(error1)
              sys.exit(1)
           else:
              print("Ok: mysql-server is installed")
              logger.info("Ok: mysql-server is installed")
       else:
           print("Ok: mysql-server is present")
           logger.info("Ok mysql-server is present")

    else:
        print(error)
        logger.error(error)
        sys.exit(1)
