import subprocess
import platform
import os

link_chromedriver = {
    '80': {
        'linux': 'https://chromedriver.storage.googleapis.com/80.0.3987.16/chromedriver_linux64.zip',
        'mac': 'https://chromedriver.storage.googleapis.com/80.0.3987.16/chromedriver_mac64.zip',
        'win': 'https://chromedriver.storage.googleapis.com/80.0.3987.16/chromedriver_win32.zip'
    },
    '79': {
        'linux': 'https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_linux64.zip',
        'mac': 'https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_mac64.zip',
        'win': 'https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_win32.zip'
    },
    '78': {
        'linux': 'https://chromedriver.storage.googleapis.com/78.0.3904.105/chromedriver_linux64.zip',
        'mac': 'https://chromedriver.storage.googleapis.com/78.0.3904.105/chromedriver_mac64.zip',
        'win': 'https://chromedriver.storage.googleapis.com/78.0.3904.105/chromedriver_win32.zip'
    },
    '77': {
        'linux': 'https://chromedriver.storage.googleapis.com/77.0.3865.40/chromedriver_linux64.zip',
        'mac': 'https://chromedriver.storage.googleapis.com/77.0.3865.40/chromedriver_mac64.zip',
        'win': 'https://chromedriver.storage.googleapis.com/77.0.3865.40/chromedriver_win32.zip'
    },
    '76': {
        'linux': 'https://chromedriver.storage.googleapis.com/76.0.3809.126/chromedriver_linux64.zip',
        'mac': 'https://chromedriver.storage.googleapis.com/76.0.3809.126/chromedriver_mac64.zip',
        'win': 'https://chromedriver.storage.googleapis.com/76.0.3809.126/chromedriver_win32.zip'
    },
    '75': {
        'linux': 'https://chromedriver.storage.googleapis.com/75.0.3770.8/chromedriver_linux64.zip',
        'mac': 'https://chromedriver.storage.googleapis.com/75.0.3770.8/chromedriver_mac64.zip',
        'win': 'https://chromedriver.storage.googleapis.com/75.0.3770.8/chromedriver_win32.zip'
    },
    '74': {
        'linux': 'https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_linux64.zip',
        'mac': 'https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_mac64.zip',
        'win': 'https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_win32.zip'
    },
    '73': {
        'linux': 'https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_linux64.zip',
        'mac': 'https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_mac64.zip',
        'win': 'https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_win32.zip'
    }
}


def download_chrome_driver():
    operation_system = platform.system().lower()
    try:
        result = subprocess.check_output('google-chrome --version', shell=True)
    except:
        print('Maybe google-chrome not be installed in your computer')
        print('please install google-chrome first')
        print('Following by: ')
        print('\twget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')
        print('\tsudo apt install ./google-chrome*.deb')

    chrome_version = result.decode("utf-8").strip().split(' ')[-1].split('.')[0]
    os.system("wget -q {} -O tmp_file_chromedriver.zip".format(link_chromedriver[chrome_version][operation_system]))
    os.system("unzip -o tmp_file_chromedriver.zip")
    os.system("rm -f tmp_file_chromedriver.zip")


def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
