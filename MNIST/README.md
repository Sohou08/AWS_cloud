

## STEP 1 : SET UP JUPYTER, TRAINING OUR MODEL, SAVE MODEL (TRAIN MACHINE) ##

```{r}
Create an instance (ubuntu for an public subnet)
Update --> sudo apt update 
Install jupyter through Anaconda --> wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
display anaconda --> bash <File name> -u
launch conda --> conda init ## Reload the terminale if it's not work or type <export PATH=~/anaconda3/bin:$PATH>
Install Jupyter Notebook --> jupyter notebook --ip=0.0.0.0 --no-browser
Connect to it  

Create a new virtual environnment
--> conda create -n nameofyourenv python=3.6
--> conda activate nameofyourenv 
--> conda install ipykernel
--> ipython kernel install --user --name=nameyouwanttodisplay

Clone Your Github
--> sudo apt-get install git
--> git clone <Github link>
--> Open the <00-mnist-cnn.ipynb> File then choose your kernel (virtual environnment created previously)
--> Run the requirement file: pip install -r AWScloud/MNIST/requirement.txt
--> In your virtual environnment:  Run the model and save it
The result is to get the model called <cnn-mnist>
```

## STEP 2 : BACK END  

```{r}
Back End required to put in private server and acces through an Jumbox. 
For more details on that, check in --> https://github.com/Sohou08/AWS_cloud/Jump box
 
Launch instance (same VPC and public subnet, size=15, new SG and same KEY)
sudo apt-get update -y

install anaconda ###### Error getted during conda excution --> conda: command not found
to resolve it --> source ~/.bashr then retape conda ######

conda update --all --yes
conda create -n FileName python=3.6
conda activate FileName
conda install opencv
pip install -r requirements.txt

copy cnn-minst / keras_flask.py
launch keras_flask.py: python keras_flask.py
```
Output
![Capture](https://user-images.githubusercontent.com/51121757/73125665-536a9580-3fa1-11ea-8ded-ed7a99c6b023.PNG)

# STEP 3 : SET UP WEB SERVER, DEPLOY WEB APPLICATION (FRONT END)

```{r}
Prepare first the file for Front End Server 


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
--> sudo cp -r AWS_Tutorials/MNIST/index.html /var/www/html/# make yes
Get output following after refreshing the web application
```
Output
![2](https://user-images.githubusercontent.com/51121757/70862736-f1e1f080-1f37-11ea-8f21-00d88b6a9996.PNG)

```{r}
--> sudo cp -r AWS_Tutorials/MNIST/static/ /var/www/html/
# check the copied files
 cd /var/www/html/
 ls
End results: ability to draw
```
Output
![3](https://user-images.githubusercontent.com/51121757/70862737-f3abb400-1f37-11ea-9908-ecea1965da35.PNG)
![1](https://user-images.githubusercontent.com/51121757/73137398-663ba380-404f-11ea-9ae8-e8d2e086f3f3.PNG)
