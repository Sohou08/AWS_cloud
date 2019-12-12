 ## SET UP, PYTHON, JUPYTER, LIBRARY ENVIRONNMENT IN YOUR DISTANCE MACHINE AND HOW TO USE IT ##
 
 JUPYTER allows to have a virtual environnment 
 
 ### Step1: Environnment requirement (instance, package) 
 
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
--> Making access to jupyter notebook to everywhere: jupyter notebook -–ip=0.0.0.0
--> To access in your instance: replace the token by this one given through jupyter notebook --ip=0.0.0.0

Note: For holding jupyter run always even the terminale is close, use this commande --> nohup jupyter notebook -–ip=0.0.0.0 & 
The command following --> (cat nohup.out ) will display the content of the file within your command line.

```
 
![1](https://user-images.githubusercontent.com/51121757/70657585-01211f80-1c54-11ea-9ea7-959ff07f8bcc.PNG)


 ## Step 2: Create a virtual machine: Anaconda
Anaconda is an open-source package manager, environment manager, and distribution of the Python and R programming languages. It's very powerful virtual machine if you need a multiple version of python.
Retriieve the last version of Anoconda linux --> https://www.anaconda.com/distribution/

```{r}
In your jupyter terminal, Create one folder called tmp and this one will contain Anoconda
Create folder: mkdir <file name>
install anoconda: curl -O https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
 ```
![2](https://user-images.githubusercontent.com/51121757/70663939-4ac43700-1c61-11ea-9d74-0d74a2cec485.PNG)


```{r}
To execute  Anaconda: bash <File Name> -u
``` 
![anaconda](https://user-images.githubusercontent.com/51121757/70666397-70a00a80-1c66-11ea-8589-a88ffd8663f0.PNG)

```{r}
Create environnment: conda create -n myenf2.7 python=2.7
Access in an environnment: conda activate myenf2.7
``` 

 ## Step 2: Create a virtual machine: Pew
 
```{r}
Download pew: pip3 install pew
``` 
 
 ![7](https://user-images.githubusercontent.com/51121757/70666095-dcce3e80-1c65-11ea-8b00-1c86e5718a0d.PNG)
 
```{r}
 Check pew: pew
 ```
 
![8](https://user-images.githubusercontent.com/51121757/70666152-fb343a00-1c65-11ea-8810-41b128e5a6ca.PNG)

 
```{r}
 Create a new environnment and launch it:  pew new <File name>
 Find your environnment: pew ls
 get there: pew workon <File name>
 Note: Everything making there, will specify in this environnment
```
 ![9](https://user-images.githubusercontent.com/51121757/70666937-a0034700-1c67-11ea-8da6-9d3db5108c76.PNG)
 

 
 ## Step 3: Connect the virtual environnment (pew) to jupyter
 
 
 ```{r}
 In your environnment , install kernel: pip3 install ipykernel 
 Configure: python3 -m ipykernel install --user --name= thenameyouwant.injupyter
 ``` 
 
 ![10](https://user-images.githubusercontent.com/51121757/70668631-0c804500-1c6c-11ea-8403-b84783d3e13c.PNG)

 
  ## Step 4: Check the differents packages presents a virtual environnment
 
  ```{r} 
 Check package: pip3 freeze 
 Create a text file for all package: pip3 freeze > myEnv.txt
 Check the content of the file: cat myEnv.txt
 ``` 
 
 ![11](https://user-images.githubusercontent.com/51121757/70671237-3e48da00-1c73-11ea-9736-dcfe422a353d.PNG)

 
 
 
