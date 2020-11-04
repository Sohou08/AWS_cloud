

## STEP 1 : SET UP JUPYTER, TRAINING OUR MODEL, SAVE MODEL (TRAIN MACHINE) ##

```{r}
Create an instance (from ubuntu for an public subnet)
- Update package
sudo apt update 
- Install jupyter through Anaconda 
wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
- display anaconda 
bash <File name> -u
- launch conda 
conda init # Reload the terminale if it's not work or type <export PATH=~/anaconda3/bin:$PATH>
- Install Jupyter Notebook 
jupyter notebook --ip=0.0.0.0 --no-browser
Connect to it  

- Create a new virtual environnment
conda create -n nameofyourenv python=3.6
conda activate nameofyourenv 
conda install ipykernel
ipython kernel install --user --name=nameyouwanttodisplay

- Clone Your Github
sudo apt-get install git
git clone <Github link>
Open the <00-mnist-cnn.ipynb> File then choose your kernel (virtual environnment created previously)
- Run the requirement file
pip install -r AWScloud/MNIST/requirement.txt
In your virtual environnment, run the model and save it. The final result is the model called <cnn-mnist>
```

## STEP 2 : BACK END  

```{r}
The back end is placed on a private server and accessed through the Jumpbox. 
For more details, check in --> https://github.com/Sohou08/AWS_cloud/tree/master/Jump%20box
 
- Launch instance
sudo apt-get update -y
Install anaconda # You can get an error when you execute conda command <command not found>
It can be resolve it through this command below
source ~/.bashr
conda 
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
- Prepare the file of Front-End server  
In front-end folder (https://github.com/Sohou08/AWS_cloud/tree/master/MNIST/front-end), you will see file "index.html"
Copy Public IP address of your Back End Server and paste it in indext.html file as below (red box)
```
Output
![2](https://user-images.githubusercontent.com/51121757/73666080-1b96d880-469a-11ea-98a2-5c28afa6f110.PNG)

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
End results: ability to draw and predict 
```
Output
![3](https://user-images.githubusercontent.com/51121757/73665534-2dc44700-4699-11ea-9d9f-aadac6c09a55.PNG)

