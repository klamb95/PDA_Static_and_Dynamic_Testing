# Testing task 2 code:
# class CardGame:
#   def __init__ (self):
   
    
# Carry out dynamic testing on the code below.

# Correct the errors below that you spotted in task 1.
#check_for_ace
def check_for_ace(card):
  if card.value == 1:
    return True
  else:
    return False

def highest_card(card_1, card_2):
  if card_1.value > card_2.value:
    return card_1
  elif card_1.value == card_2.value:
    return 'its a draw'
  else:
    return card_2


def cards_total(cards):
  total = []
  for card in cards:
    total.append(card)
  return f"You have a total of {len(total)}"
