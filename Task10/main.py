import requests
import matplotlib.pyplot as plt
from datetime import datetime

url = 'https://api.open-meteo.com/v1/forecast?latitude=55&longitude=82&hourly=temperature_2m'
response = requests.get(url)
if response.status_code == 200:
  print("success")
else:
  print("fail")
with open('test.js', 'w') as output_file:
  output_file.write(response.text)

json_list = response.json()
tempareture = json_list['hourly']['temperature_2m']
time = json_list['hourly']['time']
obj = []
for str in time:
  obj.append(datetime.strptime(str, '%Y-%m-%dT%H:%M'))

plt.plot(obj, tempareture)
plt.show()
