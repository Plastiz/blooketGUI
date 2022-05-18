# Packages that you would need to import for this code to be executed.
try:
    import requests,json,sys,math,os,time
    import PySimpleGUI as sg
    from colorama import init, Fore, Back, Style
    from selenium.webdriver.common.keys import Keys
    from seleniumwire import webdriver
except Exception:
    import os
    print("Installing required packages")
    os.system("pip install requests")
    os.system("pip install PySimpleGUI")
    os.system("pip install selenium")
    os.system("pip install selenium-wire")
    os.system("pip install colorama")
    os.system("pip install webdriver-manager")
    import requests,json
    import PySimpleGUI as sg
    from colorama import init, Fore, Back, Style
    from selenium.webdriver.common.keys import Keys
    from seleniumwire import webdriver
init(autoreset=True)
