from django.shortcuts import render
from responseapp.forms import MyForm
from django.template import loader
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from selenium.webdriver.chrome.options import Options
import time
import os

baseUrl1 = "https://zerodha.com/open-account?c=ZMPTJT"

WINDOW_SIZE = "1920,1080"

chrome_options = Options()  
# chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)


def responseform(request):
 #if form is submitted
     if request.method == 'POST':
        
        myForm = MyForm(request.POST)

        if myForm.is_valid():
            name = myForm.cleaned_data['name']
            email = myForm.cleaned_data['email']
            password = myForm.cleaned_data['password']
            mobilenumber = myForm.cleaned_data['mobilenumber']

            context = {
            'name': name,
            'email': email,
            'password': password,
            'mobilenumber': mobilenumber
            }

            # for MAC
            try:
                CHROME_PATH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
                PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
                DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
                chrome_options.binary_location = CHROME_PATH
                driver = webdriver.Chrome(executable_path = DRIVER_BIN, chrome_options = chrome_options)

            # for windows
            except:
                print('error in mac')
                # CHROME_PATH = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
                # chrome_options.binary_location = CHROME_PATH
                # dir_path = os.getcwd() + '\chromedriver.exe'
                # driver =  webdriver.Chrome(executable_path = dir_path, chrome_options = chrome_options)

            driver.get(baseUrl1)
            wname =  driver.find_element_by_name('user_name')
            wmobile =  driver.find_element_by_name('user_mobile')
            wemail = driver.find_element_by_name('user_email')
            wname.clear()
            wname.send_keys(name)
            wmobile.clear()
            wmobile.send_keys(mobilenumber)
            wemail.clear()
            wemail.send_keys(email)
            openButton = driver.find_element_by_xpath('//*[@id="open_account_proceed_form"]')
            openButton.click()

            template = loader.get_template('thankyou.html')

            #returing the template
            return HttpResponse(template.render(context, request))



     else:
         form = MyForm()
     #returning form

     return render(request, 'responseform.html', {'form':form});
