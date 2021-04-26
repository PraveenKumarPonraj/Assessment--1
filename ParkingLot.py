my_list=[]
vehicle_num=[]
add_list=[10]
view_list=[10]
my_floor=[4,3,2,1,0]
floor=[0]

def vehicle_add():
        
    slot=add_list[-1]
    last_slot=0
    if slot >= last_slot :
        i=0
        i=floor[-1]
        print('\t\t',"---VEHICLE CATEGORY---")
        print("you are in ",my_floor[i],"floor")
        print("\n1. Two-Wheeler","\n2. Three-Wheeler","\n3. Four-Wheeler","\n4. Others" )
        vehicle_type=int(input("Vehicle type:"))
        if vehicle_type > 4:
            print("Incorrect")
        else:
            vehicle_number=input("Enter Vehicle Number:")
            vehicle_num.append(vehicle_number)
            my_list.append(vehicle_type)
            print('\nSlots Occupied:',slot,'to',slot-vehicle_type+1)
            if slot-vehicle_type < 0:
                print("\nInvalid,Please select within the slot") 
            else:    
                view_list.append(slot)
                nextslot=0
                nextslot=slot-vehicle_type
                try:
                    print('Available Slots in this Floor:',nextslot)
                    add_list.append(nextslot)
                    assert nextslot > 0
                except AssertionError:
                    pass

            
                if nextslot <= 0:
                    i=i+1
                    floor.append(i)
                    print("Full,Please go to nextfloor ")
                    add_list.append(10)
                    main_menu()
                                                    
                else:    
                    print('\nRecord added successfully...')
                            

def vehicle_remove():    
    remove=input("Enter the vehicle number:")
    if remove not in vehicle_num:
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
        #for view in vehicle_num:
            print("vehicle number:",vehicle_num[-1])
            slot=view_list[-1]
            print("IN slot",slot)
                

def back():
    pass


def main_menu():

    while True:
        print( "W E L C O M E  TO  P A R K I N G   S Y S T E M")
        print("*************************************************")
        print("\n1.IN","\n2.OUT","\n3.VIEW STATUS","\n4.EXIT")
        choice=int(input("Enter your choice :"))
        if choice==1:
            vehicle_add()
        if choice==2: 
            vehicle_remove()
        if choice==3:
            view_status()
        if choice==4:
            back() 
        if choice > 4:
            print("Invalid!") 

if __name__ == "__main__":
    main_menu()            