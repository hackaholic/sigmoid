from logger import log
import zipfile
import shutil
import requests
import sys
import os
from package_check import *

logger = log()

def download_wordpress():
    print("Downloading Wordpress ...")
    logger.info("Downloading Worpress")
    try:
        url = "https://wordpress.org/latest.zip"
        r = requests.get(url, allow_redirects=True)
        f = open("/tmp/wordpress.zip", "wb")
        f.write(r.content)
        f.close()
        print("Ok: wordpress downloaded")
        logger.info("Wordpress Downloaded")
        
    except Exception as e:
       print(e)
       logger.error(e)
       sys.exit(1)

def wordpress_install():
    print("Installing Wordpress ...")
    logger.info("Installing Wordpress ...")
    try:
        zip_ref = zipfile.ZipFile("/tmp/wordpress.zip", 'r')
        zip_ref.extractall("/tmp")
        zip_ref.close()
        os.remove("/tmp/wordpress.zip")
        shutil.move("/tmp/wordpress", "/var/www/html/")
    except Exception as e:
        print(e)
        logger.error(e)

def update_config():
    db_name = "wordpress"
    db_user = "admin"
    db_pass = "hellowordpress"
    wp_dir = "/var/www//html/wordpress"
    print("Updating configuration for wordpress ...")
    logger.info("Updating configuration for wordpress ...")
    try:
        shutil.copy(os.path.join(wp_dir, 'wp-config-sample.php'), os.path.join(wp_dir, 'wp-config.php'))
        wp_config_content = open(os.path.join(wp_dir, 'wp-config.php')).read()
        wp_config_content = wp_config_content.replace('database_name_here', db_name)
        wp_config_content = wp_config_content.replace('username_here', db_user)
        wp_config_content = wp_config_content.replace('password_here', db_pass)
        f = open(os.path.join(wp_dir, 'wp-config.php'), 'w')
        f.write(wp_config_content)
        f.close()
    except Exception as e:
        print(e)
        logger.error(e)

def create_db():
    import pymysql
    print("Creating databse and user for wordpress")
    logger.info("Creating databse and user for wordpress")
    try:
        conn = pymysql.connect(host='localhost', user='root', password='helloroot')
        cur = conn.cursor()
        cur.execute("CREATE DATABASE wordpress")
        conn.commit()
        cur.execute("GRANT ALL PRIVILEGES ON wordpress.* TO 'admin'@'localhost' IDENTIFIED BY 'hellowordpress'")
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
        logger.error(e)


def main():
    
    #Update system
    update_system()
    
    # check for pip
    pip_check()

    #check for required python modules
    module_check()

    #check for apache installation
    check_apache()

    # check for php installation
    check_php()
    php_mysql()

    #check for mysql-server
    check_mysql()

    # Download wordpress
    download_wordpress()

    # wordpress installation
    wordpress_install()
    update_config()
    create_db()

if __name__ == '__main__':
    main()
