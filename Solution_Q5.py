import requests

response=requests.get('http://www.thomasbayer.com/sqlrest/CUSTOMER/')
print("status="+str(response.status_code))
print(response.text)
