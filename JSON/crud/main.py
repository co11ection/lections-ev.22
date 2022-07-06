from views import  list_of_products, retrieve_product, update_product,create_product,delete_product

def main():
    print('Hello, you can next functions: \n\t LIST-1\n\tRETRIEVE - 2\n\tCREATE-3\n\t UPDATED -4\n\t DELETED-5\n\t')
    choice = int(input('Enter functions (1,2,3,4,5): '))
    if choice == 1:
        print(list_of_products())
    elif choice ==2:
        print(retrieve_product())
    elif choice ==3:
        print(create_product())
    elif choice == 4:
        print(update_product())
    elif choice == 5:
        print(delete_product())
    else:
        print('Invalid choise')
        main()  

    ask = input('do you want contuine: Y or N: ')
    if ask.lower() == 'y':
        main()
    else:
        print('bye')

main()