
# Purpose: Set up an Jump box (public instance) in AWS allowing to access in your instance private #

#### STEP 1 : Environment requirement ( Create VPC, subnet, IGW, Elastic IP, Instances) ####
```{r}

* Create VPC ,one public subnet and IGW 
* Public subnet will attached to internet gateway (IGW) 
```


![1](https://user-images.githubusercontent.com/51121757/69834360-c077de00-1231-11ea-9d16-1616a0f32df2.PNG)


```{r}
* Private Subnet will be attached to the NAT instance. 

For that, Create first one route table, go to "edit route table association", choice the previous route table. Then this one will be replace by the NAT instance that you create after. Thus, you obtain something look like in the red box.
```


![2](https://user-images.githubusercontent.com/51121757/69834390-f9b04e00-1231-11ea-9d10-6a2dfcaf981b.PNG)


#### STEP 2. Set up 3 instances (private, Jump box and NAT instance) ####

```{r}

* Jump box (Possible to add Elastic IP for more flexibility of your instance)
Note: During set up of the publics instances, IP address will get by choice enable
on <Auto-assign Public IP>
```

![8](https://user-images.githubusercontent.com/51121757/69897369-12f4ef80-1343-11ea-9908-d2fd3698d8ff.PNG)


![3](https://user-images.githubusercontent.com/51121757/69834395-00d75c00-1232-11ea-98eb-0552028c4570.PNG)


```{r}

* NAT instance: Possibility to add Elastic IP for more flexibility of your instance. 

In AWS management console, Choice EC2 then Launch instance.
In the left navigation pane, choice community and search <amzn-ami-vpc-nat>, take in preference the first. Normally you obtain something in below :
```

![4](https://user-images.githubusercontent.com/51121757/69834399-0765d380-1232-11ea-8479-3d1b176f3c73.PNG)

```{r}
In this instance, you need tick these statements following : 
```

![5](https://user-images.githubusercontent.com/51121757/69834402-0c2a8780-1232-11ea-96db-7c87a1d60b74.PNG)


```{r}
* Private Instance
```

![6](https://user-images.githubusercontent.com/51121757/69834408-1056a500-1232-11ea-8ccb-74cce9d3cbee.PNG)


#### STEP 3. Checking If it’s work or not by pinging google.com in Ubuntu console ####
```{r}
* First access in your local directory of Key < JB_key.pem >

cd /mnt/c/Users/

* Copy the key file in your home directory ubuntu


cp -i <JB_key.pem> ~
cd ~

* Use Ssh allow you to access in the instance

chmod 400 < JB_key.pem >

* Connect to the Jump  box


ssh -i "JB_key.pem" ec2-user@<IP address Jump box>

* Connect to the Instance private


ssh -i "JB_key.pem" ec2-user@<IP address private instance>


* Check if it’s work or not

ping google.com

```


![7](https://user-images.githubusercontent.com/51121757/69834414-15b3ef80-1232-11ea-86e4-6989c31d9903.PNG)
