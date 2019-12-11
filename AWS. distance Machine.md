 ## SET UP, PYTHON, JUPYTER, LIBRARY ENVIRONNMENT IN YOUR DISTANCE MACHINE AND HOW TO USE IT ##
 Note: JUPYTER allows to have a virtual environnment 
 
 ### Step1 
 
 ```{r}
 Launch Instance: Ubuntu instance / Connect to an instance.
 Check Python
 Create a small script in Notepad and Copy the file in your instance 
 ```
 ![Capture](https://user-images.githubusercontent.com/51121757/70653719-ebf4c280-1c4c-11ea-8749-5cb5f05f9c38.PNG)

 

 ```{r}
Install pip3 and jupyter
advice: 
--> Always update before to install something in your distance machine: sudo apt-get update -y
--> Download the same version of python for pip: Sudo apt-get install python3-pip
--> Install jupyter: sudo pip3 install jupyter 
--> Information about Jupyter: Jupyter notebook
```

```{r}
Connect Jupyter using browser

http://localhost:8888/?token=381b1b4a8fc4f6f5d6e1444971045124ab8582bf638689f6

--> Add the port 8888 in your instance 
--> Replace Localhost to the IP address of an instance
--> Making access to jupyter notebook to everywhere: jupyter notebook –ip=0.0.0.0
--> To access in your instance: replace the token by this one given through jupyter notebook -ip=0.0.0.0

Note: For holding jupyter run always even the terminale is close, use this commande --> nohup jupyter notebook –ip=0.0.0.0 & 
The commande following --> (cat nohup.out ) will display the content of the file within your command line.

 ```
 
![1](https://user-images.githubusercontent.com/51121757/70657585-01211f80-1c54-11ea-9ea7-959ff07f8bcc.PNG)
