# Once that you have generated your merged dataset, you will use the following code cell to write a small program with the following four options:
# Admin login: This option will simulate how the fast-food operator validates their credentials. When this option is selected, the user should be prompted to input their username and password. The username should be admin and the password should be any number smaller than 10 (including float and negative numbers). You should allow the user to try four times, if all of them are incorrect, then the program stops and the program cell needs to be run again.
# Note: Once that an admin has logged in, this option has to be disabled (i.e. the user cannot go back and select this option). 
# Add products: This option can only be accessed once option 1 has been completed, otherwise the message login first! should be displayed and the program should go back to the main menu. In this option, the admin will be shown the list of foods and categories in the fast-food menu. Then, the admin can input a menu number to add one more product for that certain menu slot. Afterwards, the program should show the new foods and go back to the main menu.
# Note: Keep in mind that each space in the fast-food menu can hold a maximum of eight products (of the same food, of course). Also, you cannot add products in the empty menu slots. Therefore, your program should warn the admin in case that they want to add more products of a specific food in a menu slot, or if the admin wants to add products in an empty slot. 
# Buy food: This option can be accessed by "anyone", so there is no need for a validation. If this option is selected, the user will be shown the list of foods, amounts and prices. Then, the user will be requested to select one food item based on the menu_number. Once the food is selected, your program must display the price of the selected product. Then, the user will be prompted to pay. To simulate this payment, you will ask the user for an input and write any positive number (if the user inputs something invalid, ask to try again). Then, your program must check this number against the price of the product to be bought. If the input number is larger than the price, then you should return your change is... and the subtraction of the payment minus the price of the snack. If the number is equal to the price, then you must return thanks for paying. Else, you should output you need to pay more and allow the user to write another amount. After the "purchase", you should output to the user the number of products left for that particular food (therefore, you need to update the data frame!). Notice that if there were zero products left for the food selected, then you must prompt this to the user in advance before letting them buy, and ask them to select another food.
# Exit

import numpy as np
import time

loop = True
option1_completed = False
while loop == True:
  print('Welcome to the Tee fast-food menu. Select an option:')
  if not option1_completed:
    # deactivate option after successfully login
    print('1. Log in (admin only)')
    # printing other options
  print('2. Add one more product of a certain food (admin only)')
  print('3. Buy products')
  print('4. Exit')

  login_attempt = 0
  username='admin'
  password = ''
  
  option = int(input('Enter an option'))
  # print(f"OPTION: {option}")
  if option == 1:
    # Admin login
    while login_attempt < 4:
      username = input('Username: ')
      password = input('Password: ')
      if username == 'admin' and float(password) < 10:
        print('Login successful!')
        print(" ")
        time.sleep(2.0)
        option1_completed = True
        break # To leave the loop and move on
      login_attempt += 1
      # if the user name and password isn't correct
      print("Invalid username or password. You have", 4 - login_attempt, "attempts left.")
      print(" ")
    if option1_completed:
      continue
    elif not option1_completed:
      print('Error!!! Too many attempts. Exiting...')
      print(" ")
      time.sleep(5.0)
      break  

  elif option == 2: 
    # Add products
    if option1_completed:
      # checking if option1 has been completed, if yes return the below
      list_cat = merged_data[['food','category']]
      print(list_cat)
      print(" ")
      time.sleep(3.0)
      menu_number = input('Enter Menu Number: ')
      # when menu has beeninputted
      if (merged_data.loc[menu_number, 'food']is np.nan) or (merged_data.loc[menu_number, 'amount'] >=8):
        print("The product for the selected menu number can't be added")
        print(" ")
        time.sleep(3.0)
        continue
      elif (merged_data.loc[menu_number, 'amount'] < 8):
        merged_data.loc[menu_number, 'amount'] += 1
        print('A new product has been added to ', menu_number,' amount')
        print(" ")
        time.sleep(3.0)
        print (merged_data)
      else:
        print('The maximum number of product for ',menu_number,' has been reached')
        print(" ")
        time.sleep(5.0)
        continue
 
  elif option == 3:
    print(merged_data)
    print(" ")
    time.sleep(3.0)
    menu_number =  input('Kindly select a menu number: ')
    if (merged_data.loc[menu_number, 'food'])is not np.nan:    
      price = merged_data.loc[menu_number, 'price']
      print('The price of the selected menu is ', price)
      print(" ")
      time.sleep(3.0)
      payment = float(input('Enter payment: '))
      if payment > price:
        change = payment - price
        print('Your change is ', change)
        print(" ")
        time.sleep(3.0)
        merged_data.loc[menu_number, 'amount'] -=1
      elif payment == price:
        print('Thanks for paying')
        print(" ")
        time.sleep(3.0)
        merged_data.loc[menu_number, 'amount'] -=1
      else:
        print('Insufficient amount!!! payment not successful')
      
    else:
        print('select another menu number, this menu is presently unavailable')
        print(" ")
        time.sleep(5.0)
        continue

  elif option == 4:
    print("Thank you for using our system. Goodbye!")  
    break    
              
  else:
    print('Enter valid option')
    print(" ")