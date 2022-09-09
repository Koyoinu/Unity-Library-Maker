import sys
sys.dont_write_bytecode = True
import ULMAPI as api
from time import sleep

print("WARNING PUT THIS IN A FOLDER CALLED UNITY YOU HAVE 10 SECONDS")
sleep(5)
print("YOU HAVE 5 SECONDS")
sleep(5)
print("Creating new folders!")

for Furry_Avatar_Bases in map(api.concat, api.Furry_Avatar_Bases):
    api.make(Furry_Avatar_Bases)

for Premade_Avatars in map(api.concat, api.Premade_Avatars):
    api.make(Premade_Avatars)

for Anime_Avatar_Bases in map(api.concat, api.Anime_Avatar_Bases):
    api.make(Anime_Avatar_Bases)

for Unity_Packages in map(api.concat, api.Unity_Packages):
    api.make(Unity_Packages)

for Avatar_Addons in map(api.concat, api.Avatar_Addons):
    api.make(Avatar_Addons)

print("Enjoy your 1000+ folders to organize your VRC/CVR unity files!")
print("You can close the console or it will close in 50 seconds")
print("Made by Koyoinu Coded in Visual Studio Code")
sleep(50)