
my_list=[]
vehicle_num=[]
end=0

def vehicle_add():
    
    start=10
    print('\t\t',"---VEHICLE CATEGORY---:")
    print("\n1. Two-wheeler","\n2. Three-wheeler","\n3. Four-wheeler","\n4. Others" )
    vehicle_type=int(input("Vehicle type:"))
    vehicle_number=input("Enter vehicle Number:")
    vehicle_num.append(vehicle_number)
    my_list.append(vehicle_type)
    print('slots occupied:',start,'to',start-vehicle_type+1)
    print('nextslot',start-vehicle_type)
    nextslot=start-vehicle_type
    print('\nRecord added successfully...')
    return start



def vehicle_remove():
    remove=input("Enter the vehicle number:")
    vehicle_num.remove(remove)
    print("vehicle",remove,"removed from the parking slot successfully")

    

def view_status():
    
    print('\t\t',"---VEHICLE IN PARKING SLOT---")
    for view in vehicle_num:
        print("vehicle number:",view)


def back():
    pass


def main_menu():

    while True:
        print( "W E L C O M E  TO   P A R K I N G    S Y S T E M")
        print("***************************************************")
        print("1.IN")
        print("2.OUT")
        print("3.View Status")
        print("4.Exit")

        choice=int(input("Enter your choice :"))
        

        if choice==1:
            vehicle_add()
        if choice==2: 
            vehicle_remove()
        if choice==3:
            view_status()
        if choice==4:
            back() 



if __name__ == "__main__":
    main_menu()            