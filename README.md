Do you ever wonder sending messages automatically by just running a simple python script? Yes, you heard it right, it can be done easily by using this package with selenium.<br>
Selenium is a very smart package in python with which developers can automate the browser’s activity. With this, we can make use of Whatsapp-web through the browser and use it to automate message transfers. 
<br>

<img align="center" src="https://github.com/y-agg/pywakit/blob/master/Images/main.gif?raw=true"/>

<br>

## Basic Requirement 📖
1. Library/Packages — Selenium , Chromedriver(for web automation).
2. IDE — Jupyter Notebook, Sublime, Visual Studio Code (It can even your command prompt, it just have to run Python).
3. Browser — Opensource Chromium web browser(FYI Google chromedriver is preffered).

## Pip And Use 📋
```
# You can easily start using this Library
# Run the following command in your command prompt
# Make use pip library is install on your system. 
# run the following command to ensure it
>> pip --version
# To install pywakit, run following command
>> pip install pywakit
```

## Clone and use 📋
```
# You can also clone the repository by running the follwoing command 
>> git clone https://github.com/y-agg/pywakit.git 
```

## Get Started Code 🏃
```
# This will import whatsapp class to send message
>> from pywakit import Whatsapp

# This will create object of whatsapp class
>> wa = Whatsapp()

# [Optional] If you slow internet connection, set
>> wa.retry= 20 #or anything higher then 10
# Default value of retry is 10

# This is for initial setup to run the program
# If You dont have Chromedriver in your system, call this function with no paramenters. 
# Function will automatically download The chrome Driver file based on sys config.
# This will properly work with google chrome and window user for now. In future function functionality will be fixed to work with all platforms. 
# For rest to the users, pass chromedriver location as parameter to the functio. 
# By any chance window use is facing problem for cromedriver downloading. Download it manually and pass the location of file as parameter.  
>> wa.setup_driver()
    # Alternative option
    # CHROMEDRIVER _PATH is the path of chromedriver
>> wa.setup_driver(CHROMEDRIVER _PATH)

# This function is desgined to QR code 
>> wa.scan_code()

# This Function will send message. It require number(to whom message is be sent) and message(what should be sent?) as parameter's. 
# Both Should be of String type  
>> wa.send_message(number,message)

# This will close of all the object and pointers. Its is for better practice.
>> wa.destroy()

# This Function will show all the log generated by the program.
>> wa.show_log()

# This function will print all the number to whom message is been sent till now.
>> wa.show_history()

```
<img src="https://github.com/y-agg/pywakit/blob/master/Images/code.gif?raw=true"/> <br>

## Technologies used 🛠️
1. Python 
2. Selenium Library

## Bugs? 🍥

"I think there're some bugs on your code... !".I think there're some bugs on your code. You're, there are.

1. There are always be something, which will crash program. There is no such thing as perfect code. Some or another possibility will be discovered which will result in program failure. But I'll my best to keep this module bug be. 
2. Feel free to fix, reuse and duplicate this repopostiary.
3. Any Problem? I've must have inserted something that will point to contact detail. 

## LICENCE ✨

This project is licensed under the MIT License - see the [MIT License](./LICENSE) file for details.



## Connect 💡
<p align='center'>
<a href="https://twitter.com/yashaggarwal_">
  <img src="https://img.shields.io/badge/twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" />
</a>&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/aggarwalyash">
  <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />
</a>&nbsp;&nbsp;
<a href="mailto:yash.aggarwal.7545@gmail.com">
  <img src="https://img.shields.io/badge/email me-%23D14836.svg?&style=for-the-badge&logo=gmail&logoColor=white" />
</a>
</p>
