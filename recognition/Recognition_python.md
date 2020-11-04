# Access to the functionnality of AWS rekognition programmatily via python

## Use IAM

Firstly, you have to create an IAM in AWS. AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources. This one complete access to AWS rekognition API.

- Go to IAM then User and add user
- In set persmission, attach the user to AmazonRekognitionFullAccess and AmazonS3FullAccess 
- Don't forget to download the credentials.csv

## Object and scene detection using AWS rekognition API

In this case, boto 3 library is apppropriate. You can have more [detail(https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

In Docs/Available Services /Rekognition Section , if you scroll down, you will see the method  "detect_labels"

Notice that AWS rekognition return differents kind of labels and results


## Example

```python
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
```

