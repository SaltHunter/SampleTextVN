# The script of the game goes in this file.
# TODO, Character Expressions Notes Ect do not forget!

# Declare characters used by this game. The color argument colorizes the
# name of the character.\

# Definition of Important-Ish Characters go here

define r = Character("Reimi")
define ry = Character("Ryouhei")
define t = Character("Tatsuki")
define o = Character("Kei")
define n = Character ("Naotora")
define th = Character ("Tatsuhiro")
define ih = Character ("Isurugi Hirotsu")
define yh = Character ("Hibana Yosano")
define h = Character("Haruo Yosano")
define tk = Character("Takeshi")
define isr = Character("Isurugi")


# Definition of Misc characters go here
define yak1 = Character("Yakuza Member #1")
define cl = Character("Caller Voice #1")
define to = Character ("Train Operator")
define w = Character("Woman")
define cr = Character("Crowd")
define yh = Character("Yosano Group Henchman #1")
define yh1 = Character("Yosano Group Henchman")
define yh2 = Character("Yosano Group Henchmen")
define x = Character("???")
define rc = Character("Receptionist")
define tt = Character("Traitor")
define rk = Character("Rookie")
define to = Character("Tram Operator")
define st = Character("Staff")

# Definition of Flags go here.
define flag_1 = False


# Initialization of Flags
$ flag_1 = ""
$ flag_2 = ""
$ gift = ""

# define characters that are going to have a "intro textbox"
define n = Character(None,what_xalign=0.5, #Centers text within the window
    window_xalign=0.5, #Centers the window horizontally
    window_yalign=0.5, #Centers the window vertically
    what_text_align=0.5, #Centers text within the window, just in case
    kind=nvl)
define ryt = Character('Ryouhei',
    what_color="#c8ffc8",
    kind=nvl)
define rit = Character('Reimi', 
    what_color="#ffc0cb",
    kind=nvl) 
define ist = Character('Isurugi Hirotsu',
    what_color="#ffd700",
    kind=nvl)
# The game starts here.

label start:
    scene black 
    with fade
    $ reimi_pts = 0
    # Intro Narration

    # Formatting used:
    # https://renpy.org/doc/html/dialogue.html#monologue-mode

    nvl clear
    n """
    The world ended 20 years ago.
    
    A great disaster known as the great rising razed the cities of the world. Now most of the population live in island cities.
    
    One of these cities is Shinjuku, a shining beacon of decadence amidst the endless seas.
    
    Mankind also discovered the full extent of their powers, the people of Shinjuku call it Talent. 
    An extension of the physical which allows people to go beyond their physical limits.
    
    With no government, the cities came under control of criminal organizations.
    
    And in the center of it all, a Freelance Fortune Teller. A man who can show the future to these crime lords.
    
    This is the story of Sakaguchi Ryouhei.
    """
    nvl clear
    call day_1
    call day_2
    call day_3

# label day_4:
#     "1. You have nothing to do so you go visit reimi at the sibuya arena"

#     "2. After watching the fight you two go up the upper shinjuku"

#     "3. the both of you sit on the top of the abandoned apartment building"

#     "4. Reimi asks if you want to run away"
#     # TODO menuchoice which the player decides if he/she wants to run or stay.

#     # This ends the game.

#     return