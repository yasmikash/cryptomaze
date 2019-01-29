# Cryptomaze - Python-powered Bitcoin Faucet
Cryptomaze Bitcoin faucet is a simple bitcoin faucet that gives the ability to registered users to claim simple amounts of bitcoin in every difined time, and has the ability to send user payments after their withdrawal limit to FaucetHUB.IO account.

Cryptomaze is developed using python's flask microframework.

# Installation
Cryptomaze currently supports with python version 3 or above.

I will guide you how to set up the application on c-panel of your hosting account. Now, let's get started!

1. In your c-panel homepage you can find a link that says 'Setup Python App'. Click on that link.

2. In this page now we're going to create a python application for Cryptomaze faucet script. Choose the python version to 3.6, and in 'App Directory' field enter a name to your python application, in my case it's cryptomaze. And then you'll have to select the faucet url to appear cryptomaze faucet. Select it from 'App Domain'.

3. Okay. Now we created our python application. Now we need to install necessary modules to our app. To do that, click on 'add' under the module field. You'll have to add all the modules and their versions one by one and click on update. Below you can find all the modules and their versions that should be installed; (also, there is available requirements.txt file which includes all the module names and versions sould be installed if you're using pip command)

**Flask==1.0.2, Flask-Bcrypt==0.7.1, Flask-WTF==0.14.2, Flask-SQLAlchemy==2.3.2, Flask-Login==0.4.1**

See this screenshot after installing above modules: https://i.imgur.com/GJD7Gbs.jpg

4. Now click on restart. And then go to 'File Manager' from c-panel home and find your application directory. You should see some files and directories inside that directory. Delete the public folder in that directory and upload the cryptomaze script. You have to edit the  `passenger_wsgi.py` file. Delete all the code inside the `passenger_wsgi.py` file and add this line of code:

`from run import application`

See this screenshot how your script directory should be: https://i.imgur.com/Azkoypl.jpg

Now everything should be working as expected!

You can change the `settings.py` file according to your faucet settings.

