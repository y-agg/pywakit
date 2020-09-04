from termcolor import colored
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
from win32com.client import Dispatch
from win32com.client import Dispatch
import platform, requests, zipfile, os, sys, urllib
from clint.textui import progress

sys.setrecursionlimit(10**6)

class CountryCodeException(Exception):
    pass

class IllegalArgumentError(Exception):
    pass

class MaximumTimeAttemptException(Exception):
    pass

class InternetConnectionException(Exception):
    pass

class WhatsApp():
    def __init__(self):
        self.very_short_time_break = 0.5
        self.short_time_break = 2
        self.long_time_break = 7
        self.medium_time_break = 5
        self.retry= 10
        self.log_file = self.open_file("log.txt")
        self.message_log_file = self.open_file("pywakit_db.txt")
        self.webpage_url = "https://web.whatsapp.com/"
        self.webpage_xpath = '//div[@class = "_3FRCZ copyable-text selectable-text" and @dir="ltr" and @data-tab="3"]'
        self.canvas_qr_xpath = '//canvas[@aria-label="Scan me!" and @role="img"]'
        self.send_button_xpath = '//span[@data-testid="send" and @data-icon="send"]'
        self.invalid_number_modal_xpath= '//div[@class="_2HE5l" and @data-animate-modal-body="true:"]'
        self.default_chromedriver_path =  './pywakit/chromedriver'
    
    def setup_driver(self, chromedriver=None):
        if chromedriver==None and (os.path.isfile(self.default_chromedriver_path+".exe") or os.path.isfile(self.default_chromedriver_path)):
            self.log_data("// Status: Chromedriver found on this system", 'yellow')
            self.setup_driver(self.default_chromedriver_path)
            return
        if chromedriver==None:
            self.log_data("// Status: Downloading chromedriver", 'yellow')
            self.download_chrome_driver()
            self.setup_driver(self.chromedriver_path)
            return
        if isinstance(chromedriver, str) != True:
            self.log_data("// Warning: The path must be of string type", 'red')
            raise IllegalArgumentError("The path must be of string type") 
        if  chromedriver.strip() == '':
            self.log_data("// Warning: chromedriver path can't be empty or null. Proivde Valid Path to Function", 'red')
            raise IllegalArgumentError("chromedriver path can't be empty or null") 
        if not(os.path.isfile(chromedriver+".exe") or os.path.isfile(chromedriver)):
            self.log_data("// Error: chromedriver.exe or chromedriver not found at provided path", 'red')
            raise IllegalArgumentError("chromedriver.exe or chromedriver not found at provided path") 
        self.check_internet_connection()
        self.driver = webdriver.Chrome(chromedriver)
        return     

    def check_valid_phone_number(self, number):
        if isinstance(number, str):
            if "+" not in number:
                self.log_data("// Warning: Country code missing from phone_no", 'red')
                raise CountryCodeException("Country code missing from phone_no")
            return
        self.log_data("// Warning: Invalid Number Entered", 'red')
        IllegalArgumentError("Invalid Number Entered")

    def call_sleep_function(self, time):
        self.only_log_data(f"// Process: Sleep Cycle Excuted for {time} seconds")
        sleep(time)
    
    def get_retry_val(self):
        return self.retry
    
    def very_short_break(self):
        self.call_sleep_function(self.very_short_time_break)

    def medium_short_break(self):
        self.call_sleep_function(self.medium_time_break)

    def short_break(self):
        self.call_sleep_function(self.short_time_break)

    def long_break(self):
        self.call_sleep_function(self.long_time_break)

    def check_message_sent(self):
        data = self.driver.find_elements_by_xpath('//span[@data-testid="msg-time" and @data-icon="msg-time"]')
        if len(data) > 0:
            self.log_data("// Waiting: Message Is Not Yet Sent ..", 'yellow')
            self.short_break()
            self.check_message_sent()

    def open_file(self, filenname):
        if os.path.isfile(filenname):
            pointer = open(filenname, 'a')
            pointer.write(f"[{datetime.now()}] // Process: {filenname} is opened. \n")
            return pointer
        pointer = open(filenname, 'w')
        pointer.write(f"File Created: {filenname} created at {datetime.now()} \n")
        pointer.write(f"pywakit {filenname} file\n")
        pointer.write("________________________________________________________\n")
        return pointer

    def check_internet_connection(self):
        self.only_log_data("Status: Checking Internet Connection Status")
        try:
            urlopen('https://www.google.com', timeout=1)
        except urllib.error.URLError:
            self.log_data("You are not connected to internet", 'red')
            raise InternetConnectionException("You are not connected to internet")

    def destroy(self):
        self.log_data("// Closing: Closing All pointers...", 'yellow')
        self.log_data("// Status: All pointers Closed...", 'green')
        self.only_log_data("\n++++++++++\n----------\n++++++++++")
        self.driver.close()
        self.log_file.close()
        self.message_log_file.close()

    def log_data(self, message, color, file_log=None):
        if file_log == 'log_message_file':
            self.message_log_file.write(f"[{datetime.now()}]  {message} \n")
        print(colored(message, color))
        self.log_file.write(f"[{datetime.now()}]  {message} \n")

    def only_log_data(self, message):
        self.log_file.write(f"[{datetime.now()}]  {message} \n")

    def get_google_chrome_version(self):
        self.only_log_data("// Process: get_google_chrome_version() is called...")
        paths = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]
        version = list(filter(None,  [self.get_version_via_com(p) for p in paths]))[0]
        return version

    def get_version_via_com(self,filename):
        self.only_log_data("// Process: get_version_via_com() is called...")
        parser = Dispatch("Scripting.FileSystemObject")
        try:
            version = parser.GetFileVersion(filename)
        except Exception:
            return None
        return version

    def download(self,url):
        file_name= url.split('/')[-1]
        self.only_log_data("// Process: download() is called...")
        r = requests.get(url, stream=True)
        if r.status_code ==200:
            self.log_data(f"Status: Downloading chromedriver.zip file",'yellow')
            with open(f"./pywakit/{file_name}", "wb") as chrome_exe:
                total_length = int(r.headers.get('content-length'))
                for ch in progress.bar(r.iter_content(chunk_size = 2391975), expected_size=(total_length/1024) + 1):
                    if ch:
                        chrome_exe.write(ch)
            self.log_data(f"Status: Download successful",'green')
            self.log_data(f"Status: Unziping {file_name}",'yellow')
            with zipfile.ZipFile(f"./pywakit/{file_name}", 'r') as zip_ref:
                zip_ref.extractall("./pywakit/")
            self.log_data(f"Status: Unziping of {file_name} successfull",'yellow')
            os.remove(f"./pywakit/{file_name}")
            self.log_data(f"Status: Removing {file_name} successfull",'green')
            self.chromedriver_path =  './pywakit/chromedriver'
        else: 
            self.log_data(f'''// Error:{url} generated is invalid somehow. Please download the chromedriver Manually from https://sites.google.com/a/chromium.org/chromedriver/ and after downloading copy the path of extracted chromedriver.exe file and pass it to setup_driver function as arugument like Object_name.setup_driver('PATH_OF_CROME_DRIVER')\n''', 'yellow')
            sys.exit()

    def download_chrome_driver(self):
        chromedriver_version= self.get_google_chrome_version()
        self.log_data(f"Info: Chrome {chromedriver_version} on your System.",'yellow')
        architecture_version= platform.architecture()[1].lower()
        if architecture_version.startswith('darwin'):
                os_ = 'mac'
                architecture = 64 if float(chromedriver_version) >= 2.23 else 32
        elif architecture_version.startswith('linux'):
                os_ = 'linux'
                architecture = platform.architecture()[0][:-3]
        elif architecture_version.startswith('win'):
                os_ = 'win'
                architecture = 32
        else:
            raise Exception('Unsupported platform: {0}'.format(architecture_version))
        self.log_data(f"Info: Chomedriver based on your system config is {os_}{architecture}.",'yellow')
        link= f"https://chromedriver.storage.googleapis.com/{chromedriver_version}/chromedriver_{os_}{architecture}.zip"
        self.log_data(f"Chrome Driver link generated {link}",'yellow')
        self.download(link)

    def scan_code(self):
        self.log_data(
            f"Process: Opening {self.webpage_url} in Web Broswer.", 'yellow')
        self.driver.get(self.webpage_url)
        self.check_qr_code_is_avaiable(self.canvas_qr_xpath, self.get_retry_val())
        self.check_qr_code_scanned(self.canvas_qr_xpath, self.get_retry_val())

    def check_qr_code_is_avaiable(self, xpath, retry):
        self.only_log_data("Process: check_qr_code_is_avaiable() is called")
        if retry == 0:
            self.check_internet_connection()
            self.log_data("//Warning: Some Element Are Working Right.", 'red')
            raise MaximumTimeAttemptException("Exiting Program, Limit reached")
        if len(self.driver.find_elements_by_xpath(xpath)) == 0:
            self.log_data("//Checking : Looking for QR code", 'yellow')
            if not(self.quick_check_webpage(self.webpage_xpath)):
                self.long_break()
                self.check_qr_code_is_avaiable(xpath, retry-1)
            return
        self.log_data("// Status: QR code is avaiable to scan...", 'green')
        return

    def check_qr_code_scanned(self, xpath, retry):
        self.only_log_data("Process: check_qr_code_scanned() is called")
        if retry == 0:
            self.log_data("//Warning: Some Element Are Working Right.", 'red')
            raise MaximumTimeAttemptException("Exiting Program, Limit reached")
        if len(self.driver.find_elements_by_xpath(xpath)) != 0:
            self.log_data("// Status: Scan QR code...", 'yellow')
            self.long_break()
            self.check_qr_code_scanned(xpath, retry-1)
            return
        self.log_data("// Status: QR Code is Scanned...", 'green')
        return

    def quick_check_webpage(self, xpath):
        return True if len(self.driver.find_elements_by_xpath(xpath)) > 0 else False

    def check_webpage_loaded(self, xpath, retry=20):
        self.only_log_data("Process: check_webpage_loaded() is Called.")
        if retry == 0:
            self.log_data("//Warning: Some Element Are Working Right.", 'red')
            raise MaximumTimeAttemptException("Program Terminated.")
        if retry == 2:
            self.check_internet_connection()
        if retry == 5:
            self.log_data("// Warning: Your Internet Connection Is Not Stable.Check Your Internet Speed...", 'yellow')
        if not(len(self.driver.find_elements_by_xpath(xpath)) > 0):
            self.long_break()
            self.check_webpage_loaded(xpath, retry-1)

    def is_given_number_avaiable(self, number):
        self.only_log_data("// Process: Checking is given number avaiable on whatsapp .")
        if len(self.driver.find_elements_by_xpath(self.send_button_xpath)) == 0:
            self.log_data(f"// Warning: {number} is Invalid, Does'nt exists in whatsapp database.", 'red')
            return False
        return True

    def is_send_button_avaiable(self, number):
        self.only_log_data("Process: Validating Number and Button.")
        if len(self.driver.find_elements_by_xpath(self.send_button_xpath)) == 0:
            return self.is_given_number_avaiable(number)
        return True

    def send_message(self, number, message):
        self.only_log_data("// Process: send_message() is called.")
        self.check_valid_phone_number(number)
        self.driver.get(f'{self.webpage_url}send?phone='+number+'&text='+message)
        self.check_webpage_loaded(self.webpage_xpath)
        self.short_break()
        if not(self.quick_check_webpage(self.webpage_xpath)):
            self.check_webpage_loaded(self.webpage_xpath)
        if self.is_send_button_avaiable(number):
            self.driver.find_element_by_xpath(self.send_button_xpath).click()
            self.check_message_sent()
            self.log_data(f"// Status: Message is successfully sent to {number}", 'green', 'log_message_file')
    
    def show_log(self):
        self.log_data('// Process: User Requested to print Log File data.','yellow')
        with open('log.txt','r') as data:
            print(data.read())
    
    def show_history(self):
        self.log_data('// Process: User Requested to print Message File data','yellow')
        with open('pywakit_db.txt','r') as data:
            for i in data.read().split('\n'):
                if "Message is successfully" in i:
                    print(i)

if __name__ == "__main__":
    ob= WhatsApp()
    ob.show_history()
             