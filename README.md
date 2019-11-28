### How install R server by the user in his instance###

#!/bin/bash

###Update any software in youur instance

sudo yum update -y

###Install the R server

sudo amazon-linux-extras install R3.4 -y
wget https://download2.rstudio.org/rstudio-server-rhel-1.1.383-x86_64.rpm
sudo yum install -y --nogpgcheck rstudio-server-rhel-1.1.383-x86_64.rpm


#add user(s)

sudo useradd username
echo username:password | sudo chpasswd
