#How access of the functionnality rekognition In AWS programmatily by using python

""" First you need to create your own IAM

AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources. 
You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources. 
This one complete access to AWS rekognition API.

Step

Go to IAM--> User --> add user
In set persmission , you have to attach certain quality to this user to access to AWS rekognition
--> AmazonRekognitionFullAccess
Where you keep your images in your S3 bucket, for that purpose you need to access
--> AmazonS3FullAccess
After you create the user before to close the interface, you have to download the credentials.csv 'download.csv' file

Object and scene detection using AWS rekognition API

How to access this functionality of AWS programming by using python. We can do that by access the boto 3 library 
which the officel library by AWS.
Check this site to get more information: boto3 Docs 1.9.98 documentation
In Docs/Available Services /Rekognition Section , if you scroll down, you will see the method  "detect_labels"

Notice that AWS rekognition return differents kind of labels and results. """

## Example

import boto3

client = boto3.client ('rekognition',
                       aws_access_key_id = 'your_key',
                       aws_secret_access_key = 'your key',
                      region_name = 'us-east-1')
#Now we need to convert the input image as base64-encoded image bytes
#Note : if your image is in your local computer you have convert it
# in bytes types otherwise for example present in S3bucket, you just can directly pass
#
with open ('photo.jpg', 'rb') as source_image :
    source_bytes = source_image.read ()

response = client.detect_labels(Image = {'Bytes': source_bytes},
                                MaxLabels = 10)
print (response)

