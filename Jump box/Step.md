
Purpose: Set up an Jump box (public instance) in AWS allowing to access in your instance private across the NAT instance.

```{r}
Step 1 : Environment requirement ( Create VPC, subnet, IGW, Elastic IP, Instances)
```

•	Create VPC ,one public subnet and IGW 
•	Public subnet will attached to internet gateway (IGW) 

![1](https://user-images.githubusercontent.com/51121757/69834360-c077de00-1231-11ea-9d16-1616a0f32df2.PNG)

•	Private Subnet will be attached to the NAT instance. 

For that, Create first one route table, go to <edit route table association >, choice the previous route table Then this one will be replace by the NAT instance that you create after. Thus, you obtain something look like in the red box.

![2](https://user-images.githubusercontent.com/51121757/69834390-f9b04e00-1231-11ea-9d10-6a2dfcaf981b.PNG)

```{r}
Step 2. Set up 3 instances (private, Jump box and NAT instance)
```
•	Jump box (Possible to add Elastic IP for more flexibility of your instance)
For getting IP 

![3](https://user-images.githubusercontent.com/51121757/69834395-00d75c00-1232-11ea-98eb-0552028c4570.PNG)


•	NAT instance: Possibility to add Elastic IP for more flexibility of your instance. If not during Set up

In AWS management console, Choice EC2 then Launch instance.
In the left navigation pane, choice community and search <amzn-ami-vpc-nat>, take in preference the first. Normally you obtain something in below :

![4](https://user-images.githubusercontent.com/51121757/69834399-0765d380-1232-11ea-8479-3d1b176f3c73.PNG)

In this instance, you need tick these statements following : 

![5](https://user-images.githubusercontent.com/51121757/69834402-0c2a8780-1232-11ea-96db-7c87a1d60b74.PNG)


•	Private Instance

![6](https://user-images.githubusercontent.com/51121757/69834408-1056a500-1232-11ea-8ccb-74cce9d3cbee.PNG)

```{r}
Step 3. Checking If it’s work or not by pinging google.com in Ubuntu console
```
• First access in your local directory of Key < JB_key.pem >

cd /mnt/c/Users/

• Copy the key file in your home directory ubuntu


cp -i <JB_key.pem> ~
cd ~

• Use Ssh allow you to access in the instance

chmod 400 < JB_key.pem >

•	Connect to the Jump  box


ssh -i "JB_key.pem" ec2-user@<IP address Jump box>

• Connect to the Instance private


ssh -i "JB_key.pem" ec2-user@<IP address private instance>


• Check if it’s work or not

ping google.com

![7](https://user-images.githubusercontent.com/51121757/69834414-15b3ef80-1232-11ea-86e4-6989c31d9903.PNG)