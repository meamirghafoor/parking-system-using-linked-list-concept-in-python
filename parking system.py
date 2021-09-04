from datetime import datetime
class node:
    def __init__(self,name,num,price,time,mode,exit_time,next):
        self.name=name
        self.number=num
        self.price=price
        self.time=time
        self.mode=mode
        self.exit_time=exit_time
        self.next=next
class linked_list_class:
    def __init__(self):
        self.head=None
    def check_duplicate(self,number):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        pre = self.head
        ans=False
        while pre:
            if pre.number == number:
                print(f"\n*********************************************\n"
                      f"Vehicle Number : {pre.number}\n"
                      f"Vehicle Name : {pre.name}\n"
                      f"*********************************************")
                choice=int(input("This Vehicle to is already in record\n"
                                 "Press 1 to re-enter || 0 to cancel : "))
                if choice==1:
                    pre.mode = "Entered"
                    pre.exit_time = None
                    pre.time = current_time
                ans=True
                break
            pre = pre.next
        return ans
    def insertion_func(self,number):
        current_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        name = input("Enter Vehicle name (MNM) : ")
        price = int(input("Enter parking price      : "))
        if self.head is None:
            self.head=node(name,number,price,current_time,"Entered",None,None)
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=node(name,number,price,current_time,"Entered",None,None)
    def search_data(self,number):
        temp=self.head
        status=False
        while temp:
            if temp.number==number:
                print(f"*********************************************\n"
                      f"Vehicles record below\n"
                      f"*********************************************")
                print(f"Name is    : {temp.name}")
                print(f"Number is  : {temp.number}")
                print(f"Price is   : {temp.price}")
                print(f"Entry time : {temp.time}")
                print(f"Status     : {temp.mode}")
                status=True
                if temp.exit_time!=None:
                    print(f"Exit time  : {temp.exit_time}")
            temp=temp.next
        if status==False:
            print("*********************************************\n"
                  "Vehicle not found in record")
    def Vehicles_list(self,mode):
        temp = self.head
        status=True
        count=1
        print(f"*********************************************")
        while temp:
            if temp.mode ==mode:
                print(f"******************************\n"
                      f"Vehicles No : {count}\n"
                      f"******************************")
                print(f"Name is    : {temp.name}")
                print(f"Number is  : {temp.number}")
                print(f"Price is   : {temp.price}")
                print(f"Entry time : {temp.time}")
                print(f"Status     : {temp.mode}")
                status=False
                count+=1
                if temp.exit_time != None:
                    print(f"Exit time  : {temp.exit_time}")
            temp = temp.next
        if status:
            print(f"*********************************************\n"
                  f"{mode} Vehicles not found in record")
    def update_data(self,num):
        temp=self.head
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        while temp:
            if temp.number==num:
                print(f"\n*********************************************\n"
                      f"Vehicle Number : {temp.number}\n"
                      f"Vehicle Name : {temp.name}\n"
                      f"*********************************************")
                choice = int(input("This Vehicle to is in record\n"
                                   "Press 1 to exit Vehicle || 0 to cancel : "))
                if choice == 1:
                    temp.mode="Exit"
                    temp.exit_time=current_time
                    print("*********************************************\n"
                          "Vehicle exit successfully")
                else:
                    print("*********************************************\n"
                          "Vehicle not exit")
                break
            temp=temp.next
    def count_amount(self):
        temp=self.head
        amount=0
        while temp:
            amount=amount+int(temp.price)
            temp=temp.next
        return amount
    def del_all_record(self):
        del(self.head)
        self.head=None
        return True
    def del_record(self, num):
        temp=self.head
        temp2=self.head
        status=False
        if temp!=None and temp.number==num:
            self.head=self.head.next
            status=True
        else:
            while temp and temp.number!=num:
                temp2=temp
                temp=temp.next
            if temp!=None:
                temp2.next=temp.next
                del(temp)
                status=True
        if status:
            print(f"*********************************************\n"
                  f"Vehicle No({num}) record delete successfully")

if __name__=='__main__':
    print("Wellcome to VIP Parking System")
    obj=linked_list_class()
    while(True):
        choice=int(input("*********************************************\n"
                             "Press 1 for Vehicle entry          : \n"
                             "Press 2 for exit Vehicles          : \n"
                             "Press 3 for search Vehicles        : \n"
                             "Press 4 for Entered Vehicles list  : \n"
                             "Press 5 for Exit Vehicles list     : \n"
                             "Press 6 for delete Vehicles record : \n"
                             "Press 7 for delete all record      : \n"
                             "Press 8 for check current balance  : \n"
                             "Press 9 for Exit program           : \n"
                             "Enter your choice : "))
        if choice==1:
            """
            entry part of program
            """
            v_num=input("*********************************************\n"
                        "Enter Vehicle number : ")
            if obj.check_duplicate(v_num)==False:
                obj.insertion_func(v_num)
            print("*********************************************\n"
                  "Vehicle entered successfully")
        elif choice==2:
            """
            Vehicles exit part code
            """
            v_num = input("*********************************************\n"
                          "Enter Vehicle number : ")
            obj.update_data(v_num)
        elif choice==3:
            """
            program searching  part code
            """
            v_num = input("*********************************************\n"
                          "Enter Vehicle number : ")
            obj.search_data(v_num)
        elif choice==4:
            """
            all parked Vehicles list part code
            """
            obj.Vehicles_list("Entered")
        elif choice==5:
            """
            all exit Vehicles part code
            """
            obj.Vehicles_list("Exit")
        elif choice==6:
            """
            program delete per Vehicle record part code
            """
            v_num = input("*********************************************\n"
                          "Enter Vehicle number : ")
            obj.del_record(v_num)
        elif choice==7:
            """
            program delete all Vehicles record part code
            """
            if obj.del_all_record():
                print(f"*********************************************\n"
                      f"All Vehicles record delete successfully")
        elif choice==8:
            print(f"*********************************************\n"
                  f"Current Balance is : {obj.count_amount()}")
        elif choice==9:
            """
            program exit part code
            """
            exit()
        else:
            print("Invalid choice !!!")
            continue