while True:
     try:
          budget = float(input("Enter your budget: "))
          current_budget = budget
     except ValueError:
          print("PRINT NUMBER AS AN AMOUNT ")
          exit(1)
          
     products_details = { "name": [], "quant": [], "price": [] }
     
     products_values = list(products_details.values())
     
     products_name = products_values[0] #product name
     
     products_quantity = products_values[1] #quantities
     
     products_price = products_values[2] #price

     while True:
          print(budget, current_budget)
          try:
              ch = int(input("1.ADD\n2.EXIT\nEnter your choice: "))
          except ValueError:
              print("\nERROR: CHOOSE ONLY DIGITS FROM THE GIVEN OPTION")
              exit(1)
          else:
               if ch == 1 and current_budget > 0:
                    product_name = input("Enter product name: ")
                    
                    product_quantity = int(input("Enter product quantity: "))
                    
                    product_price = float(input("Enter price of the product: "))
                    
                    if product_price > current_budget:
                         print("\nCAN'T BUY THE PRODUCT")
                         continue
                    else:
                         if product_name in products_name:
                              idx = products_name.index(product_name)
                              products_quantity[idx] += product_quantity
                              products_price[idx] += product_price
                              
                              current_budget = budget - sum(products_price)
                         else:
                              products_name.append(product_name)
                              products_quantity.append(product_quantity)
                              products_price.append(product_price)
                              
                              current_budget = budget - sum(products_price)
                              print("\nAmount left: ", current_budget)
                              
               elif current_budget <= 0:
                    print("\nNO BUDGET")
               else:
                    break
               
          for i in range(len(products_name)):
               print(products_name[i], products_quantity[i], products_price[i])
                    
     


