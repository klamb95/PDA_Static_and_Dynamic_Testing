### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

#remove CardGame class
class CardGame:




#indentation is wrong should be def check_for_ace(card):
  def check_for_ace(self, card):
    #should be if card.value == 1:
    if card.value = 1:
      return True
      #missing : after else
    else
      return False
   
#  should be def highest_card(card_1, card_2):
  dif highest_card(self, card1 card2):
  # should be if card_1.value > card_2.value:
  if card1.value > card2.value:
    #should be return card_1
    return card
  #should be elif card_1.value == card_2.value:
  # return 'its a draw'
  else:
    #should be return card_2
    return card2
  

#should be def cards_total(cards):
def cards_total(self, cards):
  #should be total = []
  total
  for card in cards:
    #should be total.append(card)
    total += card.value
    #should be return f"You have a total of {len(total)}"
    return "You have a total of" + total
  
```
