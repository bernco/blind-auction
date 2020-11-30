'''
Blind auction program to check highest bidder without you physically be present
'''

#clear() to clear the output in the console.
from replit import clear
from art import logo
print(logo)
print("Welcome to the blind-aution")


action_dictionary = {}
name_list=[]
amount_list =[]

another_player = True


while another_player:
  name = input("What is your name?: ").lower()
  amount = float(input("What is your bid amount?: "))
  name_list.append(name)
  amount_list.append(amount)
  action_dictionary["name"] = name_list
  action_dictionary["bid"] = amount_list

  question = input("Is there any other player? Yes or no: ").lower()
  if question =="no":
    another_player = False
    highest = max(action_dictionary["bid"])
    pos = action_dictionary["bid"].index(highest)
    winner  = action_dictionary["name"][pos]
  clear()

        
print(f"The highest bidder is {winner} with amount of {highest}$")
