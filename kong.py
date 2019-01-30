import os  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
import time
from google.cloud import storage
import logging

SCREENSHOT_FILE = 'attend.png'
KONG_USERNAME=os.environ['KONG_USERNAME']
KONG_PASSWORD=os.environ['KONG_PASSWORD']
GOOGLE_APPLICATION_CREDENTIALS=os.environ['GOOGLE_APPLICATION_CREDENTIALS']

logging.basicConfig(format='%(asctime)s %(message)s',level=logging.INFO,filename='lastlog')

def gen_attendance():
    logging.info('starting chrome...')
    chrome_options = Options()  
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument('window-size=1280,768')
    chrome_options.binary_location = '/usr/bin/google-chrome' 
    driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),   chrome_options=chrome_options)

    logging.info('signing in...')    
    driver.get("https://www.kong-tech.com/kong-check/signin")
    driver.find_element_by_class_name('signin-page__email').find_element_by_tag_name('input').send_keys(KONG_USERNAME)
    driver.find_element_by_class_name('signin-page__password').find_element_by_tag_name('input').send_keys(KONG_PASSWORD)
    driver.find_element_by_class_name('signin-page__login-button').click()
    time.sleep(3)

    logging.info('visiting dashboard..')
    driver.get('https://www.kong-tech.com/kong-check/dashboard/view/realtime')
    time.sleep(3)

    driver.save_screenshot(SCREENSHOT_FILE)


def upload_cloud_storage():
    logging.info('uploading on cloud strage...')
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('autokong')
    blob = bucket.blob(SCREENSHOT_FILE)
    blob.upload_from_filename(SCREENSHOT_FILE)
    blob.cache_control='private'
    blob.make_public()

if __name__ == '__main__':
    gen_attendance()
    upload_cloud_storage()
    logging.info('done.')