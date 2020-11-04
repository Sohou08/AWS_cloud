

## STEP 1 : SET UP JUPYTER, TRAINING OUR MODEL, SAVE MODEL (TRAIN MACHINE) ##

- Create an instance (from ubuntu for an public subnet)
- Update package
```{r}
sudo apt update 
```
- Install jupyter through Anaconda 
```{r}
wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
```
- Display anaconda 
```{r}
bash <File name> -u
```
- launch conda 
```{r}
conda init # Reload the terminale if it's not work or type <export PATH=~/anaconda3/bin:$PATH>
```
- Install Jupyter Notebook 
```{r}
jupyter notebook --ip=0.0.0.0 --no-browser
Connect to it  
```
- Create a new virtual environnment
```{r}
conda create -n nameofyourenv python=3.6
conda activate nameofyourenv 
conda install ipykernel
ipython kernel install --user --name=nameyouwanttodisplay
```
- Clone Your Github
```{r}
sudo apt-get install git
git clone <Github link>
Open the <00-mnist-cnn.ipynb> File then choose your kernel (virtual environnment created previously)
```
- Run the requirement file
```{r}
pip install -r AWScloud/MNIST/requirement.txt
```
In your virtual environnment, run the model and save it. The final result is the model called <cnn-mnist>

## STEP 2 : BACK END  

The back end is set up in a private server and accessed through the Jumpbox. 
For more details, check [here](https://github.com/Sohou08/AWS_cloud/tree/master/Jump%20box) 
- Launch instance

```{r}
sudo apt-get update -y
Install anaconda # You can get an error when you execute conda command <command not found>
```
The above error could be resolved it as following 

```{r}
source ~/.bashr
```

Once anaconda is installed, the environment should be prepared
```{r}
conda 
conda update --all --yes
conda create -n FileName python=3.6
conda activate FileName
conda install opencv
pip install -r requirements.txt
copy cnn-minst / keras_flask.py
# launch keras_flask.py 
python keras_flask.py
```

Output
![Capture](https://user-images.githubusercontent.com/51121757/73125665-536a9580-3fa1-11ea-8ded-ed7a99c6b023.PNG)

# STEP 3 : SET UP WEB SERVER, DEPLOY WEB APPLICATION (FRONT END)

- Prepare the file of Front-End server  
In front-end [folder](https://github.com/Sohou08/AWS_cloud/tree/master/MNIST/front-end), copy your public IP address of back-end server in index.html file as following (red box)

Output
![2](https://user-images.githubusercontent.com/51121757/73666080-1b96d880-469a-11ea-98a2-5c28afa6f110.PNG)

- Launch ubuntu 18.4 (same VPC and public subnet, size=15, new SG and same KEY)
- Install apache2

```{r}
sudo apt install apache2
```

To check if it works, paste your public IP address with the port in your browser.

Output
![Capture](https://user-images.githubusercontent.com/51121757/70862733-eee70000-1f37-11ea-8cca-523a76b47413.PNG)

- Clone your Github

```{r}
sudo apt-get install git
git clone <Link name>
sudo cp -r AWS_Tutorials/MNIST/index.html /var/www/html/ # make yes
```

Get output following after refreshing the web application

Output
![2](https://user-images.githubusercontent.com/51121757/70862736-f1e1f080-1f37-11ea-8f21-00d88b6a9996.PNG)

```{r}
sudo cp -r AWS_Tutorials/MNIST/static/ /var/www/html/
# check the copied files
cd /var/www/html/
ls
```

The end result is the ability to draw and predict the output.

Output
![3](https://user-images.githubusercontent.com/51121757/73665534-2dc44700-4699-11ea-9d9f-aadac6c09a55.PNG)

