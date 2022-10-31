import requests




res = requests.get('https://ipinfo.io/')
data= res.json()

#print(data)

location= data['loc'].split(',')
print(location)

lat= location[0]
lon= location[1]


def with_city(requests=data):
	res = requests.get('https://ipinfo.io/')

	return(requests['city'])



print(with_city())


if __name__== '__main__':
    print('yes')





