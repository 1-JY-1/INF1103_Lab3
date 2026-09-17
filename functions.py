

def get_valid_input(input_prompt, current_inventory, rejectedEntries):

    if input_prompt.lower() == 'add':

        numAmount = False

        while numAmount == False:

            print("===========================================================================")
            amount = input("Enter the number of items to add: ")
            numAmount = amount.isdigit()

            if numAmount == False:

                print("===========================================================================")
                print ("Invalid input. Please enter a valid number.")
                rejectedEntries += 1

            elif numAmount == True:

                if int(amount) < 0:
                    print("===========================================================================")
                    print("Invalid input. Please enter a positive number.")
                    numAmount = False
                    rejectedEntries += 1

                else:
                    numAmount, current_inventory, rejectedEntries = process_delivery(numAmount, current_inventory, int(amount), rejectedEntries)

                    if numAmount == True:
                        return False, current_inventory, rejectedEntries
                    
    elif input_prompt.lower() == 'calculate tax':
        calculate_tax(current_inventory)
        return False, current_inventory, rejectedEntries
    
    elif input_prompt.lower() == 'quit':
        generate_report(current_inventory, rejectedEntries)
        return True, current_inventory, rejectedEntries
    
    else:
        print("Invalid input. Please try again.")
        return False, current_inventory, rejectedEntries


def process_delivery(numAmount, current_inventory, added_value, rejectedEntries):

    current_inventory += added_value

    if current_inventory > 500:
        current_inventory -= int(added_value)
        numAmount = False
        rejectedEntries += 1
        print("===========================================================================")
        print(f"Inventory cannot exceed 500 items.\nCurrent Inventory: {current_inventory}.\nPlease enter a smaller amount.")
        return numAmount, current_inventory, rejectedEntries

    else:
        print("===========================================================================")
        print(f"Added {added_value} items. New inventory: {current_inventory}")
        calculate_tax(added_value)
        return numAmount, current_inventory, rejectedEntries



def calculate_tax(current_inventory):
    tax_rate = 0.1
    tax_amount = current_inventory * tax_rate
    print(f"Tax Amount: ${tax_amount:.2f}" )
    return tax_amount



def generate_report(current_inventory, rejectedEntries):
    print("===========================================================================")
    print(f"Final inventory: {current_inventory}")
    calculate_tax(current_inventory)
    print(f"Total rejected entries: {rejectedEntries}")
    print("Exiting the program...")
    print("===========================================================================")








