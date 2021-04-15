my_list=[]
vehicle_num=[]
add_list=[10]

def vehicle_add():
                
                    slot=add_list[-1]
                    end=1
                    if slot >= end :

                        print('\t\t',"---VEHICLE CATEGORY---")
                        #print("you are in ","floor")
                        print("\n1. Two-wheeler","\n2. Three-wheeler","\n3. Four-wheeler","\n4. Others" )
                        vehicle_type=int(input("Vehicle type:"))
                        vehicle_number=input("Enter vehicle Number:")
                        vehicle_num.append(vehicle_number)
                        my_list.append(vehicle_type)
                        print('slots occupied:',slot,'to',slot-vehicle_type+1)
                        nextslot=0
                        nextslot=slot-vehicle_type
                        print('nextslot is:',nextslot)
                        add_list.append(nextslot)

                        if nextslot <= 0:
                            print("Full,Please go to nextfloor ")
                                            
                        else:    
                            print('\nRecord added successfully...')
                        
                    
              

def vehicle_remove():    
    remove=input("Enter the vehicle number:")
    if remove not  in vehicle_num:
        print("Incorrect vehicle Number")
        user_key=input("Press any key to exit:")
        main_menu()
    else:
        vehicle_num.remove(remove)
        print("vehicle Number",remove,"removed from the parking slot successfully")


def view_status():
    print('\t\t',"---VEHICLE IN PARKING SLOT---")
    if not vehicle_num:
        print("List is Empty")
        user_key=input("Press any key to exit:")
        main_menu()
    else:
        for view in vehicle_num:
            print("vehicle number:",view )


def back():
    pass


def main_menu():

    while True:
        print( "W E L C O M E  TO  P A R K I N G   S Y S T E M")
        print("***************************************************")
        print("\n1.IN","\n2.OUT","\n3.View Status","\n4.Exit")
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