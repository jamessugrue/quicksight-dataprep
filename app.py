from chalice import Chalice
import pandas as pd
import boto3
from os import environ


app = Chalice(app_name='quicksight_dataprep')


# To run once a day change the annotation and paramters in function to ->
# @app.schedule(Rate(1, unit=Rate.DAYS))
# def prepareData(event):  

@app.lambda_function()
def prepareData(event, context):
    url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/us_state_vaccinations.csv'
    dataframe = pd.read_csv(url)

    s3 = boto3.resource('s3')
    s3.Bucket(environ.get('BUCKET_NAME')).put_object(Key='us-covid-vaccination-data.csv', Body=dataframe.to_csv(index=False)) 

    return {}
