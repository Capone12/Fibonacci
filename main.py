from instabot import Bot

user = input("Su nombre de Usuario: ")
passw = input("Su contraseña: ")
cuenta_followers = input("Cuenta de la persona: ")


elBot = Bot()
elBot.login(username= user, password= passw)

elBot.follow_followers(cuenta_followers)