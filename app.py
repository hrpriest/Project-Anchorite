import char
import mob

ui_name = input('Welcome to my game! What is your name? :')
ui_gender = input('What is your gender? :')
ui_class_type = input('What class would you like to play? :')

goat = char.Character(ui_name, ui_gender, ui_class_type)

print(goat)
