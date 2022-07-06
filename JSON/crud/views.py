
import json
import random



FILE_PATH = 'data.json'

def get_data():
    with open (FILE_PATH) as file:
        return json.load(file)

def list_of_products():
    data = get_data()
    return data

def retrieve_product():
    data = get_data()
    id = int(input('Enter id products: '))
    product = list(filter(lambda x: x['id']==id, data))
    return product[0]



def get_id():
    data = get_data()
    with open('id.txt', 'r') as file:
        id = int(file.read())
        # print(id)
        # print(type(id))
        id += 1
    with open('id.txt', 'w') as file:
        file.write(str(id))
    return id
    
def create_product():
    data = get_data()
    product = {
        'id': get_id(),
        'title': input('Enter name products: '),
        'price': float(input('Enter price: ')),
        'descripption': input('enter discription: ')
        }
    data.append(product)

    with open(FILE_PATH, 'w') as file:
        json.dump(data,file)
    result = {'msg':'Created', 'product':product}
    return result


def update_product():
    data = get_data()
    flag = False
    id = int(input('Enter id product: '))
    product = list(filter(lambda x: x['id']==id, data))
    if not product:
        return {'msg':'Invalidid, product doesnt not exist!'}
    

    index = data.index(product[0])
    choice = input('What are you wanr to change\'?(1 - title, 2 - price, description): ')

    if choice =='1':
        data[index]['title'] = input('Enter new name: ')
        flag = True
    elif choice == '2':
        data[index]['price']= float(input('Enter new price: '))
        flag = True
    elif choice =='3':
        data[index]['descripption'] = input('Enter new description: ')
        flag = True
    else:
        print('Invalid Choise to update')
    
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
    if flag:
        return {'msg': 'Updated', 'product': data[index]}
    else:
        return {'msg': 'Not Updated'}

def delete_product():
    data = get_data()
    id = int(input("enter id products: "))
    product = list(filter(lambda x:x['id']==id, data))

    if not product:
        return {'msg':'Invalid id, product not exist!'}
    index = data.index(product[0])
    deleted = data.pop(index)
    json.dump(data, open(FILE_PATH, 'w'))

    return {'msg':'Deleted', 'product': deleted}


