import pandas as pd
import boto3



Total_historico=pd.read_csv(data)
datacant=len(Total_historico)
dataset = Total_historico.to_html()
print('preparar html')
html2 = f"""<html>
    <head></head>
    <body>
    <h1> Datos desde Lambda </h1>
    <p>Cantidad de bases actualizadas cant:{datacant} el día {day} .

    {dataset}


    .</p>
    </body>
    </html>"""

def enviar_mail(mails,html2,SUBJECT):
    import boto3
    client = boto3.client('ses',region_name = 'us-east-1')
    return client.send_email(Destination={'ToAddresses':mails },
    Message={'Body': {'Html': {'Data': html2},'Text': {'Charset': 'UTF-8','Data': ''},},'Subject': {'Data': SUBJECT},},
    Source="xxx@xxx.com")
  
SUBJECT = f"""Carga de datos desde Lambda - {fecha}"""
mails=["xxi@xxx.com"]
enviar_mail(mails,html2,SUBJECT)
