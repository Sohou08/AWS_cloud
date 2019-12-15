

## STEP 1 : CREATE JUPYTER, TRAINING OUR MODEL, SAVE MODEL ##

```{r}
Create instance
Update --> sudo yum update -y
Install jupyter toward Anaconda --> wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
display anaconda --> wget <File name> -u
launch conda --> conda init ## Reload the terminale if it's not work
Install Jupyter Notebook --> jupyter notebook --ip=0.0.0.0 --no-browser
Connect to it --> Copy the 

Create a new virtual environnment
--> conda create -n nameofyourenv python=3.6
--> conda install nb_conda
--> conda conda activate nameofyourenv 
--> conda install ipykernel
--> ipython kernel install --user --name=nameyouwanttodisplay
Clone Your Github
--> sudo apt-get install git
--> git clone <Github link>
--> Choose your kernel (virtual environnment created previously)
--> In your virtual environnment:  Run the model and save it
The only thing that you need here is the model that you save called <cnn-mnist>
```

## STEP 2 : SET UP WEB SERVER APPLICATION##

```{r}
launch ubuntu 18.4
install apache2 --> sudo apt install apache2
Check --> In the browser, paste your public IP address ##don't forget to add the port
```
![Capture](https://user-images.githubusercontent.com/51121757/70862733-eee70000-1f37-11ea-8cca-523a76b47413.PNG)

```{r}
Clone your Github:
--> sudo apt-get install git
--> git clone <Link name>
--> sudo mv AWS_Tutorials/MNIST/index.html /var/www/html/# make yes
Get following output after refreshing the web application
```
![2](https://user-images.githubusercontent.com/51121757/70862736-f1e1f080-1f37-11ea-8f21-00d88b6a9996.PNG)


```{r}

--> sudo mv AWS_Tutorials/MNIST/static/ /var/www/html/
End results:
#if it's work you have the ability to draw
```
![3](https://user-images.githubusercontent.com/51121757/70862737-f3abb400-1f37-11ea-9908-ecea1965da35.PNG)
![4](https://user-images.githubusercontent.com/51121757/70862739-f5757780-1f37-11ea-818f-1303978de389.PNG)

## STEP 3 : SET UP FLASH  ##
