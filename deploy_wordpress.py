from logger import log
import zipfile
import shutil
import requests
import sys
import os

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


wordpress_install()
#download_wordpress()
