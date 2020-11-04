 # SET UP PYTHON, JUPYTER ENVIRONMENT AND DIFFERENT LIBRARY IN YOUR DISTANCE MACHINE AND HOW TO USE IT #
 
 
 ## Step1: Environment requirement (instance, package) 

- Launch Instance (Ubuntu instance / Connect to it)
- Check python version
- Create a small script in Notepad and Copy the file in your instance

Output
![Capture](https://user-images.githubusercontent.com/51121757/70653719-ebf4c280-1c4c-11ea-8749-5cb5f05f9c38.PNG)

- Install pip3 and jupyter
- First Update before to install

```{r}
sudo apt-get update -y
```

- Download the same version of python for pip

```{r}
Sudo apt-get install python3-pip
```
- Install jupyter

```{r}
sudo pip3 install jupyter 
```
- Get information about Jupyter

```{r}
Jupyter notebook
```

- Connected in Jupyter through browser as following

```{r}
http://localhost:8888/?token=381b1b4a8fc4f6f5d6e1444971045124ab8582bf638689f6
```
Don't forget to add the port 8888 in the security group and replace the localhost to the IP address of your instance 

- Make access the jupyter notebook to everywhere

```{r}
jupyter notebook -–ip=0.0.0.0
```

To access in your instance: replace the token by this one given through jupyter notebook --ip=0.0.0.0
- Note: For holding jupyter always run even the terminal is close, use this command below

```{r}
nohup jupyter notebook -–ip=0.0.0.0 & 
<cat nohup.out> will display the content of the file.
```

Output
![1](https://user-images.githubusercontent.com/51121757/70657585-01211f80-1c54-11ea-9ea7-959ff07f8bcc.PNG)

## Step 2: Create a virtual machine: Anaconda

Anaconda is an open-source package manager, environment manager, and distribution of the Python and R programming languages. It's very powerful virtual machine if you need a multiple version of python. The last version of Anaconda linux could be retrieved [here](https://www.anaconda.com/distribution/).

In your jupyter terminal, create a folder called tmp where anaconda will be set up.

```{r}
mkdir <file name>
curl -O https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
```

Output
![2](https://user-images.githubusercontent.com/51121757/70663939-4ac43700-1c61-11ea-9d74-0d74a2cec485.PNG)

- Execute anaconda

```{r}
bash <File Name> -u
``` 
Output
![anaconda](https://user-images.githubusercontent.com/51121757/70666397-70a00a80-1c66-11ea-8589-a88ffd8663f0.PNG)

- Create an environment
```{r}
conda create -n myenf2.7 python=2.7
```
- Access an environment
```{r}
conda activate myenf2.7
``` 

## Step 2: Create a virtual machine: Pew

- Download pew

```{r}
pip3 install pew
pew
``` 

Output
 ![7](https://user-images.githubusercontent.com/51121757/70666095-dcce3e80-1c65-11ea-8b00-1c86e5718a0d.PNG)
 ![8](https://user-images.githubusercontent.com/51121757/70666152-fb343a00-1c65-11ea-8810-41b128e5a6ca.PNG)

-  Create a new environment and launch it
```{r}
pew new <File name>
```
- Find your environment
```{r}
pew ls
# get there
pew workon <File name>
```
Output
 ![9](https://user-images.githubusercontent.com/51121757/70666937-a0034700-1c67-11ea-8da6-9d3db5108c76.PNG)
 
## Step 3: Connect to the virtual environment (pew) to jupyter
 
 - Install kernel 
 
```{r}
pip3 install ipykernel 
``` 

- Configured it
```{r}
python3 -m ipykernel install --user --name= thenameyouwant.injupyter
``` 
 Output
 ![10](https://user-images.githubusercontent.com/51121757/70668631-0c804500-1c6c-11ea-8403-b84783d3e13c.PNG)

 
 ## Step 4: Check if it works
 
-  Check package
 ```{r} 
pip3 freeze 
```
- Create a text file for all package

```{r}
pip3 freeze > myEnv.txt
cat myEnv.txt
```

 Output
 ![11](https://user-images.githubusercontent.com/51121757/70671237-3e48da00-1c73-11ea-9736-dcfe422a353d.PNG)

 
 
 
