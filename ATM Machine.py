#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Welcome to ATM Machine of Sakib Haque Zisan')
restart='Y'
chances=2
balance=20000.00
while chances>=0:
    pin=int(input('Please Enter your 4 digit Number:'))
    if pin==(2345):
        print('Your Entered Pin is Correct.')
        print('Please press button 1 for Checking Balance')
        print('Please press button 2 for Withdraw')
        print('Please press button 3 for Payment')
        print('Please press button 0 for Return to Back')
        
        option=int(input('Please Choice your Option.'))
        if option==1:
            print('Your Balance is $',balance)
            restart=input('Would You like to Go Back')
            if restart in('No','no','Nope','nope'):
                print('Thanks for your given Time')
                break
                
                elif oprtion==2:
                    option2=('Y')
                    withdraw =float(input('How much money you want to withdraw now? 100, 500, 1000'))
                    if withdraw in[100,500,1000]:
                        balance= balance - withdraw
                        print('\n Your Balance is $',balance)
                         restart=input('Would You like to Go Back')
            if restart in('No','no','Nope','nope'):
                print('Thanks for your given Time')
                break
                
                elif option==3:
                    payment=float(input('How much You want to pay?'))
                    balance = balance + payment
                     print('\n Your Balance is $',balance)
                         restart=input('Would You like to Go Back')
            if restart in('No','no','Nope','nope'):
                print('Thanks for your given Time')
                break
                
                elif option==0:
                    print('Please wait few minutes....')
                    print('Thanks for Your Given Time.')
                    break
                    
                    else:
                        print('Please Enter Your Code\n')
                        restart=('Y')
                        
                        elif pin !=(2345):
                            chances = chances-1
                            if chances==0:
                                print('\n Entered Pin is Wrong!!')
                                break
                    
                    
                    
                
                        
                    
    


# In[ ]:




