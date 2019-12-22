
# Purpose: Set up an Jump box (public instance) in AWS allowing to access in your instance private #

### STEP 1 : Environment requirement (Create VPC, subnet, IGW, Elastic IP, Instances) ###

Public subnet
```{r}
Create VPC, subnet public, internet gateway (IGW)
```
Output (Public subnet)

       ![1](https://user-images.githubusercontent.com/51121757/69834360-c077de00-1231-11ea-9d16-1616a0f32df2.PNG)

Private subnet
```{r}
*Private Subnet will be attached to the NAT instance. 
For that, Create first one route table, go to "edit route table association", choice the previous route table. 
This one will be replace by the NAT instance --> Obtain (in the route table) "eni-0c56e.....".
```
Output (Private subnet)

       ![9](https://user-images.githubusercontent.com/51121757/70646282-797ce600-1c3e-11ea-8654-a15b32e1c1bf.PNG)

### STEP 2. Set up 3 instances (private, Jumpbox and NAT instance) ###
The Jumpbox and NAT instance are in public subnet

Jumpbox (installed in the public subnet)
```{r}
Jump box :possibility to add Elastic IP for more flexibility of your instance.
Otherwise, choice enable in <Auto-assign Public IP> during the set up (Red box in the picture)
```

Output (Auto-assign public IP)

      ![8](https://user-images.githubusercontent.com/51121757/69897369-12f4ef80-1343-11ea-9908-d2fd3698d8ff.PNG)

Output (Private subnet)

      ![3](https://user-images.githubusercontent.com/51121757/69834395-00d75c00-1232-11ea-98eb-0552028c4570.PNG)

NAT instance (installed in the public subnet)
```{r}
NAT instance: Possibility to add Elastic IP for more flexibility of your instance. 
In AWS management console, Choice EC2 then Launch instance.
In the left navigation pane, choice community and search <amzn-ami-vpc-nat>, take in preference the first.
```
Output (NAT Instance)

      ![4](https://user-images.githubusercontent.com/51121757/69834399-0765d380-1232-11ea-8479-3d1b176f3c73.PNG)

```{r}
Note: tick these statements following (in the private instance) : 
```
Output
![5](https://user-images.githubusercontent.com/51121757/69834402-0c2a8780-1232-11ea-96db-7c87a1d60b74.PNG)

Private Instance 
Output
![6](https://user-images.githubusercontent.com/51121757/69834408-1056a500-1232-11ea-8ccb-74cce9d3cbee.PNG)


### STEP 3. Checking If it’s work or not by pinging google.com in Ubuntu console ###

```{r}
* First access in your local directory of Key < JB_key.pem >

cd /mnt/c/Users/

* Copy the key file in your home directory ubuntu


cp -i <JB_key.pem> ~
cd ~

* Use Ssh allowing to access in the instance

chmod 400 < JB_key.pem >

* Connect to the Jump  box


ssh -i "JB_key.pem" ec2-user@<IP address Jump box>

* Connect to the Instance private


ssh -i "JB_key.pem" ec2-user@<IP address private instance>


* Check if it’s work or not

ping google.com

```

Output (End)
![7](https://user-images.githubusercontent.com/51121757/69834414-15b3ef80-1232-11ea-86e4-6989c31d9903.PNG)
