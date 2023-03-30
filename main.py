import requests
import json

#константы
status = 'available'
url = f'https://petstore.swagger.io/v2/pet'
headers= {'accept':'application/json'}
new_pet={
    'id': 100,
    'category': {
        'id': 30,
        'name': 'LKSjfjf'
    },
    'name': 'HUYGJYjdjikf',
    'photoUrls': [
        'string'
    ],
    'tags': [
        {
            'id': 0,
            'name': 'ijkuhgj'
        }
    ],
    'status': 'available'
}
pet_Id=0


#Запрос GET
print('Результат выполнения запроса GET:')
res = requests.get(f'{url}/findByStatus?status={status}', headers=headers)
print(f'Код ответа: {res.status_code}')
txt_result=''
try:
    txt_result=res.json()
except:
    txt_result=res.text
print(txt_result)

# Запрос POST
print('')
print('Результат выполнения запроса POST:')
res = requests.post(url, headers=headers, data=new_pet)
print(f'Код ответа: {res.status_code}')
txt_result=''
try:
    txt_result=res.json()
except:
    txt_result=res.text
#pet_Id=txt_result.find({'petId'})
print(txt_result)

# Запрос PUT
print('')
print('Результат выполнения запроса PUT:')
res=requests.put(pet_Id,{'name':'DfRgYn'})
print(f'Код ответа: {res.status_code}')
txt_result=''
try:
    txt_result=res.json()
except:
    txt_result=res.text
print(txt_result)

# Запрос DELETE
print('')
print('Результат выполнения запроса DELETE:')
res=requests.delete(f'{url}',petId=100)
print(f'Код ответа: {res.status_code}')
txt_result=''
try:
    txt_result=res.json()
except:
    txt_result=res.text
print(txt_result)

