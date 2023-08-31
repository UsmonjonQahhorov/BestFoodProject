from twilio.rest import Client

account_sid = 'ACa76d524849ab2384869467c81457a83a'
auth_token = '015faf8c88831338810327f67cba7e8a'
client = Client(account_sid, auth_token)

message = client.messages.create(
  body="Hey bitch",
  from_='+18145930412',
  to='+998998787323'
)

print(message.body)