#QuickSight DataPrep 
A simple AWS Lambda function written in [Chalice](https://github.com/aws/chalice) to gather data from X, store it in S3 and refresh a dataset in QuickSight with the data update. 

This accompanies the tutorial [Embedded Dashboards With QuickSight](#)  

#Placeholders
Before you deploy you will need to replace {{BUCKET_NAME}} placeholder in both `config.json` and `app.py` to the name of your bucket in S3


#Deployment 
To deploy on your own AWS account simply use 
```chalice deploy --stage dev```

#Run from command line 
You can invoke the Lambda function using 
``` chalice invoke--name prepareData```