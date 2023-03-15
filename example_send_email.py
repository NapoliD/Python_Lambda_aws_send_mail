def send_email():
    client = boto3.client('ses',region_name='your-region-name')
    sender_email = "your-sender-email@example.com"
    recipient_email = "your-recipient-email@example.com"
    message = "Subject: Test email\n\nThis is a test email sent using Python and Amazon SES."
    
    response = client.send_email(
        Destination={
            'ToAddresses': [
                recipient_email,
            ],
        },
        Message={
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': message,
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': 'Test email',
            },
        },
        Source=sender_email,
    )
    print("Email sent! Message ID:"),
    print(response['MessageId'])
