# Write a class to hold player information, e.g. what room they are in
# currently.
from .room import Room
class Player(Room):
  def __innit__(self, location, direction,
                attack, defense, health,
                items, luck, misfortune, specials, perks, stats):
    self.location = location
    self.direction = direction
    self.attack = default=10
    self.defense = default=20
    self.health = 100
    self.items = []
    self.luck = 1
    self.specials = []
    self.misfortune = 0
    self.stats = []



  def decrement(self, snumber):
    self.health - number
    

  def got_hit(self, health, **kwargs):
    print('AUUGH!!!')
    print('You got hit!')
    self.health = 