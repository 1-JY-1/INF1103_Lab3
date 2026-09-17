    # if user_input.lower() == 'add':

    #     numAmount = False

    #     while numAmount == False:

    #         print("===========================================================================")
    #         amount = input("Enter the number of items to add: ")
    #         numAmount = amount.isdigit()

    #         if numAmount == False:
                
    #             print("===========================================================================")
    #             print ("Invalid input. Please enter a valid number.")
    #             rejectedEntries += 1

    #         elif numAmount == True:

    #             if int(amount) < 0:
                    
    #                 print("===========================================================================")
    #                 print("Invalid input. Please enter a positive number.")
    #                 numAmount = False
    #                 rejectedEntries += 1

    #             else:

    #                 inventory += int(amount)

    #                 if inventory > 500:

    #                     inventory -= int(amount)
    #                     numAmount = False
    #                     rejectedEntries += 1
    #                     print("===========================================================================")
    #                     print(f"Inventory cannot exceed 500 items.\nCurrent Inventory: {inventory}.\nPlease enter a smaller amount.")

    #                 else:
    #                     print("===========================================================================")
    #                     print(f"Added {amount} items. New inventory: {inventory}")

    # elif user_input.lower() == 'quit':

    #     print("===========================================================================")
    #     print(f"Final inventory: {inventory}")
    #     print(f"Total rejected entries: {rejectedEntries}")
    #     print("Exiting the program.")
    #     print("===========================================================================")
    #     toQuit = True

    # else:
    #     print("Invalid input. Please try again.")