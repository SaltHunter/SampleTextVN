# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.\

# Definition of Important-Ish Characters go here

define r = Character("Reimu")
define s = Character("Sakaguchi")
define t = Character("Tatsuki")
define o = Character("Ozaki")
define n = Character ("Naotora")
define th = Character ("Tatsuki Hirotsu")
define ih = Character ("Isurugi Hirotsu")


# Definition of Misc characters go here
define yak1 = Character("Yakuza Member #1")


# Definition of Flags go here.

$ flag_1 = False
$ gift = ""

# The game starts here.

label start:
    $ reimi_pts = 0
    # Intro Narration 
    # TODO format it...
    #The world ended 20 years ago.
#A great disaster known as the great rising razed the cities of the world. Now most of the population live in island cities.
#One of these cities is Shinjuku, a shining beacon of decadence amidst the endless seas.
#Mankind also discovered the full extent of their powers, the people of Shinjuku call it "Talent". An extension of the physical which allows people to go beyond their physical limits.
#With no government, the cities came under control of criminal organizations.
#And in the center of it all, a Freelance Fortune Teller. A man who can show the future to these crime lords.
#This is the story of Sakaguchi Ryouhei.

label day_1:
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

    # Todo, Add Dialog to key points above.
    # TODO Add backround and shit

    "1. Sakaguchi wakes up, phone ringing asking him to go to ozaki clan hq"

    "2. post meeting with nagotora, reimi visits outside of ozaki HQ"

    menu choice1:
        "Getting Payment For Previous Jobs":
                $ reimi_pts += 5
                jump day_1common

        "They Asked me to do some fortune telling":
                $ reimi_pts -= 5
                jump day_1common

label day_1common:
    "3. Reimi takes you to an ice cream parlor and wonders what you want more from life"

    menu choice2:
        "If i had the chance, i'd gladly run away.":
                $ reimi_pts += 5
                jump day_1next

        "I'm Fine with this life, I've seen the future and i'll  be fine.":
                $ reimi_pts -= 5
                jump day_1next

label day_1next:
    "4. You went to reimi's place and ate yakisoba together, it's the first time you've been happy in a while"

    "5. Go home and sleep"


label day_2:
    # Chapter 2 begins here.
    "1. You get called by the yosano group."

    "2. get called by reimi, menu choice to go to the shibuya arena"

    menu choice3:
        "I'll be there but not sure if i can make it.":
                $ reimi_pts += 5
                $ flag_1 = True
                jump day_2reimi

        "I'm sorry but i got a job today":
                $ reimi_pts -= 5
                jump day_2jobs

label day_2reimi:
    "With that fleeting promise in mind, you decide it'd be best to head over to the shibuya arena after work."
    jump day_2common



label day_2jobs:
    "I'll just go do my work."
    jump day_2common

label day_2common:
    "3. You go to the yosano group's HQ and finish up your work"

    if flag_1 == True:
        "3.1 You watch reimi win in the arena against her opponent takeshi fukuchi"

        "3.2 Have dinner at an izakaya with reimi and takeshi"
        jump sleep_day2

    else:
        "3.1 I go to the local convenience store, buy a cup ramen and head home."
        

label sleep_day2:
    "4. I Go home to sleep."



    jump day_3



label day_3:
    # Chapter 3 begins here.
    "1. Get called by the hirotsu family."

    "2. Go to Hirotsu HQ meet takeshi hirotsu and isurugi hirotsu"

    "3. Finish Job and get paid"

    menu choice4:
        "I should Check on reimi":
                $ reimi_pts += 5
                jump day_3reimi
        
        "I should just go home":
                $ reimi_pts -= 5
                jump day_3home

label day_3reimi:
    "3.1 I go buy some food for reimi on the way."

    menu foodchoice:
        "Buy Her Ramen":
                $ gift = "ramen"
                jump day_3continue

        "Buy Her Onigiri":
                $ gift = "onigiri"
                jump day_3continue

        "Buy Her Curry":
                $ gift = "curry"
                jump day_3continue


label day_3home:
    "3.1 I buy some cup ramen on the way home and go to sleep."
    jump day_3sleep

label day_3continue:
    "3.2 She's happy you visited."

    "3.3 she opens your gift"
    if gift == "ramen":
        "She eats the ramen, the broth soothes her spirit"

    if gift == "onigiri":
        "She eats the onigiri, the taste reminded her of your childhood days together."

    if gift == "curry":
        "She eats the curry, you forgot she couldnt take the spices, but laughed as her face turned bright red due to the spiciness of the curry."

    "3.3 She gives you a good luck charm before you head home."

    "3.4 You head home, feeling satisifed for once, that your life turned out this way instead of its predetermined course."


label day_3sleep:
    "4. i go to sleep."





label day_4:
    "1. You have nothing to do so you go visit reimi at the sibuya arena"

    "2. After watching the fight you two go up the upper shinjuku"

    "3. the both of you sit on the top of the abandoned apartment building"

    "4. Reimi asks if you want to run away"
    # TODO menuchoice which the player decides if he/she wants to run or stay.

    # This ends the game.

    return
