from models.character import Character
from model.monster import Monster

ui_name = input('Welcome to my game! What is your name? :')
ui_gender = input('What is your gender? :')
ui_class_type = input('What class would you like to play? :')

goat = Character(ui_name, ui_gender, ui_class_type)

print(goat)
 