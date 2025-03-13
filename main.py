# main.py
from urllib.parse import urljoin
from constants import BASE_DIR, MAIN_DOC_URL

def whats_new():
    # Вместо константы WHATS_NEW_URL, используйте переменную whats_new_url.
    whats_new_url = urljoin(MAIN_DOC_URL, 'whatsnew/')
    ...

def latest_versions():
    ...

def download():
    # Вместо константы DOWNLOADS_URL, используйте переменную downloads_url.
    downloads_url = urljoin(MAIN_DOC_URL, 'download.html')
    ...
