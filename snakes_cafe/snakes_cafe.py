print(""" 
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************""")

items=['Wings','Cookies','Spring Rolls','Salmon','Steak','Meat Tornado','A Literal Garden','Ice Cream','Cake','Coffee','Pie','Tea','Unicorn Tears']
 
# ("""***********************************
# ** What would you like to order? **
# # ***********************************""")
counter=[0,0,0,0,0,0,0,0,0,0,0,0,0]

order=input('>')
while order!='quit':  
    # print(order,'first before looping\n',i)
    if order in items:
        c=items.index(order)
        counter[c]+=1
        print(f'\n\n** {counter[c]} order of {order} have been added to your meal **')    
    else: 
        print('Please make sure you type you order correctly as we have in the menu :) ')
    order=input('>')
print('Thank you for visiting, we hope you enjoyed your experince with us, see you soon ')
# Print out a summary of complete order.
run=0
for i in range(13):
            if counter[i]!=0:
                if run==0:
                    print('Here is a summary of you order ')
                    run=1
                    print(f"You orderd {counter[i]} of {items[i]}")

