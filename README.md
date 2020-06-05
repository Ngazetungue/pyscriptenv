#### What do i have and What Is a Virtual Environment?

Simple example of running python script in the virtual environment. Virtual environments help us to create and manage our project in the separate environments from the default location. In most Linux environments, Python is installed under /usr/local , and that’s where you would find the libraries.The main purpose of Python virtual environments is to create an isolated environment for Python projects. This means that each project can have its own dependencies, regardless of what dependencies every other project has. In our  example, we’d create a virtual environment and then run our file inside the environment. We're using Python 3 in our example.

#### Let's get started

You’ll need to install the virtualenv tool with pip if you’re not using Python 3. In our case we're using Python 3, then we don't need to install since we already have the venv module from the standard library installed. But below is a simple command we could use should we have different version.
```
$ pip install virtualenv    
 ```
Let's make a new directory to work with. Let me assume that you want to create your new directory on your desktop and name it random-virtual-environments. Below i created a directory called random-virtual-environments and navigate into it using cd command. Simple command right.
```
$ mkdir random-virtual-environments && cd random-virtual-environments    
```
Let's create a new virtual environment inside the directory we created above. randomenv is a name of our environment. In this case we're using python3.

```
$ python3 -m venv randomenv
```

After creating the environment you should see the following files below.
```
bin  include  lib  lib64 pyvenv.cfg
```
Now it is time to activate our environment (randomenv) so that we can be able to use the packages in isolation, you need to do this, just run the following command:

```
$ source randomenv/bin/activate
```
Let's create our file that we want to run inside the environment we have created.
```
$ touch number.py
```
After creating our file we could see our file is added to our directory.
```
bin  include  lib  lib64  number.py  pyvenv.cfg

```
Open the file by typing the following command on your terminal. Let me assume you know how to use vim.
```
$ vim number.py
```
After opening the file, write the codes below on the file.
```py
# This program displays ten random
# numbers in the range of 1 through 50.

import random

def randomNumber():
      for count in range ( 10 ) :
# Get a random number.
            number = random.randint(1, 50)
# Display the number.
            print (number)
# Call the randomNumber function
randomNumber()
                
```
Close the file by pressing Esc button on your keyboard and write wq to save the file. Run below command to run the file.
```
$ python number.py
```
Below is the output after running the file. Bear in mind that we're expecting random number and your output might be different from the one shown below.
```
45
21
34
17
26
2
13
44
16
39
```
#### Conclusion
I hope you get a picture of how you would use virtual environment to run your python script or project. Bear in mind that this article meant for beginners who don’t know what virtual environment is or who never use it before. We have a huge Python community, you can always ask around if you have any doubt in whatever you’re doing. As you progress as a developer, be sure to take time to learn how to use different tools to your advantage for example Docker that’s work almost the same as virtual environment. In future I am planning to cover Docker so that we can compare the two.
