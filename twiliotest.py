from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC8344bd3ebe15815bd6be95b8b0cc5f57'
auth_token = 'b04525e7a9478ed99af4b20d51c35568'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Ben Dover and Moe Lester need to talk to you.",
                     from_='+14082157063',
                     to='#'
                 )

print(message.sid)
