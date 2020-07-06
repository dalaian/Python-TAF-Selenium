# Part II
This is the solution for the part two of the assessment

## Requisites

You need the following in your computer to run the framework
* Selenium grid
* Python

If you already have a selenium grid, you only need to go to [UI/config/config.ini](https://github.com/dalaian/Test/blob/master/part_two/UI/config/config.ini#L3) and make sure the seleniumAddress is the correct

### How to install python
See instruction in the readme file of the part_one folder, section [How to install python](https://github.com/dalaian/Test/tree/master/part_one#how-to-install-python)

### How to install Selenium grid
For this framework, we are going to install webdriver-manager as the selenium grid. 
There are several ways to install it, you can use brew if you are on Mac 
but I'd recommend to install it using NodeJS because it will run on Windows or Mac

#### How to install NodeJS
Get the executable from the Node JS page https://nodejs.org/es/download/
and install it, or you can install it from brew

Once you are done, NodeJS and npm will be installed
> Remember to check that the commands *node --version* and *npm --version* work as expected

Run the following command to install the web-driver
```
npm i webdriver-manager -g
```

Now, run the following command to update it
```
webdriver-manager update
```


## Running the test
Now, if everything is correct start the web manager by the command (or if you used another grid, start it as usually)
```
webdriver-manager start
```
>You should not close this terminal

To check that the webdriver is up, check that at the end of the console it says
>Selenium Server is up and running on port 4444

Also, verify that you can go to http://localhost:4444/wd/hub/ in your browser

### Installing requirements

Open a terminal, and go to the folder **part_two**

Run the following command to install the [requirements](https://github.com/dalaian/Test/blob/master/part_two/requirements.txt)
```
pip install -r requirements.txt
```

Execute the test case by the command
```
python UI/tests/product/TS001ValidateProductCanBeAddedToCart.py
```

## Parameters
It's possible to indicate in which browser you want to run the test case 
using the parameter **-b** or **--browser**, by default it is CHROME
```
python UI/tests/product/TS001ValidateProductCanBeAddedToCart.py -b <CHROME/FIREFOX/SAFARI>
``` 
For instance:
```
python UI/tests/product/TS001ValidateProductCanBeAddedToCart.py --browser FIREFOX
``` 

Or you can send a parameter to indicate to run the test case in headless mode, using the parameter 
**-hl** or **--headless**, by default it is not in headless mode
```
python UI/tests/product/TS001ValidateProductCanBeAddedToCart.py --headless <True/1/T/t/true False/0/F/f/false>
``` 
For instance:
```
python UI/tests/product/TS001ValidateProductCanBeAddedToCart.py -hl True
```
> Note: to run the automation on Safari you have to check the 'Allow Remote Automation' option in Safari's Develop menu, 
also Safari does not support headless mode yet

You can also see what parameters you can send using the **-h** parameter
```
python UI/tests/product/TS001ValidateProductCanBeAddedToCart.py -h
``` 

So, a good example to test the parameters is with the command
```
python UI/tests/product/TS001ValidateProductCanBeAddedToCart.py --browser FIREFOX -hl true
```
> Note that the browser used is firefox and the browser won't open (headless mode)

## Reports
The automation generates certain reports to give more information to the QA Automation Engineer as well as for the stakeholders

The framework logs all the actions done by the code under the folder **UI/logs**, any failure, warning or 
information will be here. The logs will be separated based on the browser

Under **UI/reports** you can find xml reports about the results of the test cases

Finally, **UI/reports/screenshots** has all the screenshots taken if any error was present, 
the name says in which test case and step the error occurred
> The reports are ignored by .gitignore