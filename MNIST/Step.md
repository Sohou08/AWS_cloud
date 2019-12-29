

## STEP 1 : SET UP JUPYTER, TRAINING OUR MODEL, SAVE MODEL (TRAIN MACHINE) ##

```{r}
Launch instance
Update --> sudo apt update 
Install jupyter through Anaconda --> wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
display anaconda --> bash <File name> -u
launch conda --> conda init ## Reload the terminale if it's not work
Install Jupyter Notebook --> jupyter notebook --ip=0.0.0.0 --no-browser
Connect to it  

Create a new virtual environnment
--> conda create -n nameofyourenv python=3.6
--> conda install nb_conda
--> conda activate nameofyourenv 
--> conda install ipykernel
--> ipython kernel install --user --name=nameyouwanttodisplay
Clone Your Github
--> sudo apt-get install git
--> git clone <Github link>
--> Choose your kernel (virtual environnment created previously)
--> In your virtual environnment:  Run the model and save it
The result is to get the model called <cnn-mnist>
```

## STEP 2 : SET UP WEB SERVER, DEPLOY WEB APPLICATION (FRONT END)##

```{r}
launch ubuntu 18.4 (same VPC and public subnet, size=15, new SG and same KEY)
install apache2 --> sudo apt install apache2
Check if it works --> In the browser, paste your public IP address ##don't forget to add the port
```
Output
![Capture](https://user-images.githubusercontent.com/51121757/70862733-eee70000-1f37-11ea-8cca-523a76b47413.PNG)

```{r}
Clone your Github:
--> sudo apt-get install git
--> git clone <Link name>
--> sudo mv AWS_Tutorials/MNIST/index.html /var/www/html/# make yes
Get output following after refreshing the web application
```
Output
![2](https://user-images.githubusercontent.com/51121757/70862736-f1e1f080-1f37-11ea-8f21-00d88b6a9996.PNG)

```{r}
--> sudo mv AWS_Tutorials/MNIST/static/ /var/www/html/
End results: ability to draw
```
Output
![3](https://user-images.githubusercontent.com/51121757/70862737-f3abb400-1f37-11ea-9908-ecea1965da35.PNG)
![4](https://user-images.githubusercontent.com/51121757/70862739-f5757780-1f37-11ea-818f-1303978de389.PNG)

## STEP 3 : BACK END  ## not finish

```{r}
In order to make faster, use public subnet to avoid to install Jumbox.
Launch instance (same VPC and public subnet, size=15, new SG and same KEY)
sudo apt-get update -y
install anaconda
execute anaconda
--> conda install keras
--> conda install opencv (doesn't work)
clone github

check python: python3 and pip3
Install pip3: sudo apt install python3-pip ## Pip should have the same version with python
Clone github

Make work this commande: ~/AWS_Tutorials/MNIST$ python3 ./keras_flask.py
--> pip3 install -r requirement.txt
--> pip3 install keras
--> pip3 install tensorflow==1.8.0
--> pip3 install flask
--> pip3 install tensorflow
--> pip3 install opencv # it's not work then try with anaconda
## Error getting excution conda --> conda: command not found
to resolve it --> source ~/.bashr then retape conda ##
--> conda install keras
--> conda install opencv
--> sudo apt-get install python3-opencv

--> Ip address:port(5000)/predict
--> cd /var/www/html/
--> sudo vi <File name>
--> Go to url, enter your IP address of back end
--> :
```
