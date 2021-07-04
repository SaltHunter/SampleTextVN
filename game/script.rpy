# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.\

# Definition of Important-Ish Characters go here

define r = Character("Reimu")
define s = Character("Sakaguchi")
define t = Character("Tatsuki")
define o = Character("Ozaki")
define n = Character ("Naotora")


# Definition of Misc characters go here
define 1 = Character("Yakuza Member #1")


# The game starts here.

label start:
    # Intro Narration 
    # TODO format it...
    #The world ended 20 years ago.
#A great disaster known as the great rising razed the cities of the world. Now most of the population live in island cities.
#One of these cities is Shinjuku, a shining beacon of decadence amidst the endless seas.
#Mankind also discovered the full extent of their powers, the people of Shinjuku call it "Talent". An extension of the physical which allows people to go beyond their physical limits.
#With no government, the cities came under control of criminal organizations.
#And in the center of it all, a Freelance Fortune Teller. A man who can show the future to these crime lords.
#This is the story of Sakaguchi Ryouhei.

label commonroute_1:
    # Chapter 1 begins here.

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

label commmonroute_2:

label commonroute_3:



    # This ends the game.

    return
