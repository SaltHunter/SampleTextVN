﻿# The script of the game goes in this file.
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


# Definition of Misc characters go here
define yak1 = Character("Yakuza Member #1")
define cl = Character("Caller Voice #1")
define to = Character ("Train Operator")
define w = Character("Woman")
define cr = Character("Crowd")
define yh = ("Yosano Group Henchman #1")
define yh1 = ("Yosano Group Henchman")
define yh2 = ("Yosano Group Henchmen")
define x = ("???")

# Definition of Flags go here.

$ flag_1 = False
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
# The game starts here.

label start:
    scene black 
    with fade
    $ reimi_pts = 0
    # Intro Narration 
    # TODO format it...
    nvl clear
    n "The world ended 20 years ago."
    n "A great disaster known as the great rising razed the cities of the world. Now most of the population live in island cities."
    n "One of these cities is Shinjuku, a shining beacon of decadence amidst the endless seas."
    n "Mankind also discovered the full extent of their powers, the people of Shinjuku call it Talent. An extension of the physical which allows people to go beyond their physical limits."
    n "With no government, the cities came under control of criminal organizations."
    n "And in the center of it all, a Freelance Fortune Teller. A man who can show the future to these crime lords."
    n "This is the story of Sakaguchi Ryouhei."
    nvl clear
jump day_1

label day_1:
    # Chapter 1 begins here.
    #Day 1

    #[A/N Setting: ryouhei’s room]
    scene bg room 
    with fade
    
    ry "Mnghh..."

    "My phone sprang to life, its familiar buzz pulling me out of my sleep."

    ry "God, give me 5 more minutes."

    "The phone continued to ring, with not much way to avoid it, I quickly picked it up, despite my half-asleep state."

    ry "Good Morning, this is Sakaguchi Ryouhei, sorry I just woke up . . .how can I help you today?"
        
    cl "Good morning Mr. Sakaguchi, my name is Yamada Tatsuhiro representing Madame Ozaki."

    ry "Ah, I'm sorry."

    th "Madame Ozaki has requested your services."

    ry "My services, when and where if I may ask?"

    th "Today at Bar Poirot, Upper Shinjuku around 10AM Today."

    ry "T-today?!"

    th "Yes today."
        
    ry "A-alright then, I'll be there in a bit."
        
    th "Very well then, I will inform Madame Ozaki about this thank you for your time Mr. Sakaguchi."

    ry "Mm, thank you as well."

    ry "Ahh. Another day, another job huh."


    # TODO reformat this as monolog that showsa nd scrolls down something something.
    # For all theese "monlogue bricks"
    
    "For the past few years of my life, I've been stuck within this loop of living."
    "A constant state of being awake and not trying at all."
    "To best describe it, I'm living for the sake of living. I'm on autopilot I suppose."
    "But to my knowledge, there's nothing much that I can do about it."
    "Since I was a child, I've been abandoned here in the streets of Shinjuku."
    "I've always been afraid of death, afraid of the unknown."
    "But through some incredible accident, I found out that I had special powers, what people call Talent."
    "A pendant with a large emerald in its center, I call it 'Samsara'."
    "Those who see through the gem are able to see their future"
    "As long as they follow what they see, then their future will not change."
    "In a way for myself and others, this is a way to feel safe about our future."
    "And to the lords of Shinjuku, a way to keep control of their empires."
    "Though things like that are rather trivial to me."
    "Each passing day is no different, a type of mutual understanding between the houses and myself."
    "Because I cannot control what Samsara shows, it helps these lords prepare against their inevitable deaths."
    "Between the three houses of Shinjuku, The Ozakis, The Hirotsus and The Yosanos. I'm one of the few who can freely roam between their territories."
    "Those who seek to hurt me will eventually be killed by one of the three houses."
    "At the end of the day, I'm only a pawn for them."
    "I cannot die because they do not let me."
    "But at the same time I cannot live because they rely on me."
    

    ry "I'll be off."

#[A/N Opening door sound]
# TODO, Opening Door SFX???
    "Who am I kidding, I live alone anyway."
    "Despite making more than enough money to live, I cannot live in the decadent territory known as Upper Shinjuku."
    jump shinjuku

label shinjuku:
#[A/N Transition to Upper Shinjuku]
    scene bg shinjuku
    with fade
    "That place corrupts people; wealth and greed fuel those who live there."
    "Just last week the Ozaki clan toppled a famous host club, murdered the owner and pinned him to the signboard by stabbing a katana through his heart."
    "But as I said, fighting back would mean that I'll be next on their hit list."
    "Living in lower Shinjuku is not any better either."
    "It's a den of scum and villainy, eventually everyone has to kill here at some point."
    "Be it the lower class or the upper class, everyone has blood in their hands."
    "Suddenly I felt a buzz in my pocket, a notification from my phone."

    nvl clear
        # TODO, Format for text message??? otherwise its a custom scene bg
    rit "hey ryou-chan! I'll be around upper shinjuku around 12pm for lunch with a bunch of my friends."
    rit "if you want there's a new ice cream parlor opening soon, we can meet around 1 or 2pm"

    "Begrudgingly, I opened my messaging app and replied"

    ryt "mm, i'll see if I'll be there."

    "As quickly as I replied, I turned off my phone."
    ry "That woman . . ."

    nvl clear

    "Reimi is a friend I met by chance, she lives nearby my house and coincidentally she has a Talent of her own."
    "Strangely enough, despite the bleak situation we live in, she's always able to smile."
    "Sometimes I wonder if I could be like her, but having company in misery is better than nothing."
    "At the very least, I have something to look forward to after this job."
    "I quickly hopped onto a tram heading towards Upper Shinjuku."
    "Upper Shinjuku and Lower Shinjuku is divided by a tram system connecting the two."
    "To get to the upper city, you need to take"

    to "We have arrived at the Southern Terrace, next stop is Kabuki-chou"

    "Quickly I stood up and left the tram."

    ry "Keep the change."

    "Upper Shinjuku is a whole different world to me, open spaces and the tall skyscrapers it is truly a sight to behold."
    "Unlike the crummy Lower part of town, there is air to breathe here, a sense of unattainable freedom."
    "Checking the clock on my phone, it's only 9:30AM. I still have 30 minutes free."
    "Though Reimi is not around, I guess I should just head towards Bar Poirot."
    jump barlabel
label barlabel:
    #[Transition to Bar Poirot]
    scene bg poirot
    with fade
    "Entering the bar, the air within was filled with smoke coming off cigarettes."
    "Murmured chatters of secrets and unknown affairs pass through my ears."
    "It felt warm, but in the sense that you were in hell, boiled alive with the sinners."
    "As I powered through the tobacco-scented air, there sat a woman and two of her bodyguards."
    "The man to her right stood up and approached me."

    th "Good morning, my name is Yamada Tatsuhiro. I assume you are Sakaguchi Ryouhei."
    ry "Yes, yes I am."
    th "Alright, right this way please."

    "And there the woman sat, her pale face and white kimono contrasting against the old brown leather of the sofa she sat on."
    "Her eyes were sharp and judgmental, just as expected from the leader of the Ozaki Clan."
    "Her name was Ozaki Kei, queen of Kabuki-chou."

    show ozaki_kei happy:
    
    #Question, mending di address si ozaki kei jd Ozaki, Kei ato Ozaki Kei?
    w "I've been expecting you, Mr. Sakaguchi, very nice to meet you."
    ry "A... Ah, yes. Good to meet you again, Madame Ozaki."
    o "As per last time you showed me that I will take control of Kabuki-chou, which thankfully happened as per your prediction. Now I'd like to ask you for some . . . extra favors."

    "Another one of her bodyguards handed her an ivory cigarette holder and lit a fire."
    "Meanwhile Yamada opens a bottle of cognac and pours it into a wine glass."

    o "Would you like some yourself? On the house."
    ry "Thank you, Madame Ozaki but I don't drink."
    o "Well you're still quite the sourpuss aren't you. Working for the mafia and yet you still try your best to stay clean, I'm more surprised you're still clean up until now."
    o "Either way, I called you here today for some . . . fortune telling."
    ry "Of course, give me a minute."

    "I took off the pendant around my neck, handing it to her bodyguard, Yamada."
    "Slowly he held the jewel in the middle in front of Madame Ozaki's eyes."
    "In a flash, Madame Ozaki looked overwhelmed."

    o "Something has changed, Sakaguchi tell me why it changed!"
    ry "W . . . what? What's the matter?"
    o "Last time it showed that after I have taken control of Kabuki-chou that I will live up to the age of 89."
    o "Now why does it show that I will die in two months time!"
    o "Tell me, Sakaguchi!"

        # TODO have an angry expression for ozaki chan

    "After Madame Ozaki shouted, the lively bar turned silent."
    "I felt the stare of a hundred pairs of eyes."
    "Inhale."
    "Exhale."
    "This is why I dislike being in Upper Shinjuku."

    o "I know that your Talent always tells the truth, but how did I get killed by some low henchmen from another clan!"

    "Madame Ozaki slammed her glass onto the table, breaking the cup."

    ry "I guess uhh . . . "
    ry ". . . can you tell me what happened right before you died."
    o "Then why don't you look at it yourself?!"
    ry "I cannot see other people's visions . . . and I do not know of any plans from the other clans."
    o "Then explain how your Talent predicted something wrong."

    "Kei’s eyes stare me down like daggers"
    "Her bodyguards look equally frustrated."

    o "Explain!"

    "I leaned my body forwards, twiddling my thumbs."
    "I could only think, think what may have happened to cause such a major change."

    ry "Maybe it's because you took control of Kabuki-chou."
    o "Haaa?"
    ry "Because Samsara accounts for changes in the world, every major deviation results in a new prediction."
    o "Maybe because you gained control of Kabuki-chou, the other clans are now seeking to take it back from you."
    ry "The prediction did not account for the other clans planning to kill you. Because those plans did not exist before you gained control of Kabuki-chou"
    o "Then what if I decided to not be in Kabuki-chou?"

    "Yamada hands over Samsara back to Madame Ozaki."
    "Madame Ozaki held the pendant close to her eye and watched."

    o "62 years old, that seems better than two months. I suppose I should stay in my headquarters knowing that they might kill me."
    o "Yamada, Murasaki. Tell the guards to safeguard my office."

    "The two of the bodyguards nodded."
    "Though this may seem like a rare occurrence, there is a reason why I sometimes feel like abandoning this profession."
    "These leaders are always one step away from death."
    "Samsara is able to see through that, but because I own the Talent I'm also the one to blame."

    o "I appreciate your work, Mr. Sakaguchi. Without you I might have died too early."
    ry "A.. ah. No worries."
    o "I'll pay you the usual alright, 50,000 yen?"
    ry "Alright, thank you Madame Ozaki"
    hide ozaki_kei happy
label uppershinjuku:
#[Transition to Upper Shinjuku]
# Question, scenes here would be izakaya outside? shinjuku? or what? how are we going to transition this?
    scene bg baroutdoor
    with fade
    "I exhaled . . . thank God this job is over."
    "Thankfully, despite her temper, Madame Ozaki is a well paying client"
    "Even if things don't go her way at all times, I'm still able to reason with her."
    "It's something at least."
    "She handed me the money in a bag and Yamada returned Samsara to me."

    o "Don't spend it all in one place, Mr. Sakaguchi. Pardon my temper."
    ry "Thank you, Madame Ozaki."
# Tentative Transition to shinjuku Background
    scene bg shinjuku
    with fade
    "As soon as she handed over the money, I quickly left the bar."
    "Just as I stepped out of the place, my phone started to ring."
    "Looking at the contact name, it's Reimi."
    "I could only exhale and pick it up."

    r "OI RYOU-CHAN!"
    ry "Y-yes?"
    r "I got off early, let's go to that parlor now!"
    ry "Well, I'm near Kabuki-chou right now, where is the parlor at?"
    r "Harajuku. Can you make it on time?"
    ry "I'll probably go borrow a scooter, give me 30 minutes alright?"
    r "If you're not here in 30 you're buying me an extra scoop alright!"
    r "Ehehehe, I'm just kidding."
    ry "I just got paid, so I can get you that if you want."
    r "E-eh? Well then, I'll be waiting for you."

    "She turned off the call from her side"
    "Well, next is to find a scooter rental spot. At least it's everywhere here in Upper Shinjuku."

# TODO make this a title card format?
    scene black
    with fade
"-Title Card: 35 minutes later-"
jump harajuku
#[Transition to Harajuku]
label harajuku:
    scene bg harajuku
    with fade
    "Had I known . . ."
    "Traffic was light today . . ."
    "I would've . . ."
    "TAKEN THE TAXI!!" with vpunch #(Screen jitter here) # TODO Screen Jitter
    "I could only drag my own body to Harajuku, right in front of the gate there I saw her, surrounded by other folks."
    "Reimi Yanagiwara, a professional athlete and a fellow Talent user."
    "A famous gladiator who fights at the Shibuya Arena."
    "I'm not surprised that someone like her is constantly surrounded by fans."

    ry "Oi! Yanagiwara!"
    show reimi happy
    with fade

    "She turned her heads towards me"

    r "Ah! Ryou-chan!"

    "Reimi launches herself towards me."

    r "Ryou-chan! You're finally here!"
    ry "Please, can we not use our first names here, people will get the wrong idea!"
        # Programmer's Note: Jesus Thats a lot of characters to define
    cr "Is he . . ."
    cr "Reimi-chan is . . .?"

    "What did I bring myself into? This woman . . ."

    r "Ah, Sakaguchi I'm sorry I forgot!"
    r "I'm sorry guys but I have to go for a bit!"

    "Reimi took my hand and dragged me away into Harajuku."

    ry "You didn't tell you were busy with your fans?!"
    r "Does it look like I can control my fans?!"
    r "Anyway Ryou-chan, the ice cream parlor?"
    ry "Mhm, you said you want two scoops right?"
    r "From the price I've seen, it's not terribly expensive."
    ry "Don't worry, price isn't an issue."
    r "By the way, you said you got a payment just now, Ryou-chan?"
    jump choice1


menu choice1:
    "Ah, I was getting a payment for a previous job":
        jump choicea
        $reimi_pts += 5
        
    "Yeah, they asked me to do some fortune telling":
        jump choiceb
        $reimi_pts -= 5



#[Choice A]
label choicea:
    ry "Ah, I was getting a payment for a previous job"
    r "Hmph, I thought you were doing that fortune telling job again."
    ry "Well, the payment was for a previous fortune telling job but, yeah."
    r "Well, the good thing is that you're not really stuck there anymore."
    jump commonroute

#[Choice B]
label choiceb:
    ry "Yeah, they asked me to do some fortune telling"
    r "Again? I thought you said that you were thinking of stopping."
    ry "I have to live too, you know."
    r "Well, as long as you're safe. I really don't like you being with those people."
    jump commonroute


#[back to normal]
label commonroute:
    ry "I'll keep that in mind, I'm sorry if I worried you."
    ry "There's been a lot of short notice jobs lately, I don't understand why."
    r "And that's why you come to the Shibuya Arena, it's a neutral area so you don't have to worry much. Also, there's me!"
    ry "Then who's going to buy you that double-scoop ice cream if I don't get paid?"
    r "Oh shut up! I have my own money, Ryou-chan."

    "Eventually we reached the ice cream parlor, Reimi was already excitedly looking through the flavors"
    "But for myself, I don't really know what I want to pick."

    ry "Reimi . . . tell me which flavor is the best?"
    r "The best huh? From what I've seen on SNS, people seem to like the caramel apple flavor."
    ry "What about you? Which flavor do you want? I kind of promised that I'll get you two scoops."
    r "It's only 300 yen per scoop. I can pay for myself, you know."
    ry "300? That sounds like a full dinner."
    r "Let's be a little hedonistic for once, Ryouhei. Besides, don't worry too much, I'll pay for myself."
    ry "Nah, I'll pay for you, Reimi!"
    r "Fine then if you insist."

    "I ended up buying her a choco-mint and bubblegum ice cream cone."
    "While I got myself an apple caramel flavored cone."
    "Honestly, even if she may act a little clingy."
    "I'm glad to have a friend like her handy."
    "Sometimes looking at her battle-hardened face, I can only wish to have that kind of strength"
    "To face near-death experiences on the daily."
    "To ride against her opponents . . . ."
    "Really she is so much cooler than I am."

    r "Oi, Ryou-chan. What's the matter?"
    ry "Hmmm? Why?"
    r "Nah, you've been staring at your cone for quite a bit, is there something in your mind?"
    ry "I'm sorry about being so busy lately."
    ry "I want to make time for you but . . . circumstances."

    "Reimi leaned back to the wall"

    r "Tell me, Ryou-chan."
    ry "Hmm? What's the matter?"
    r "Have you ever thought . . . ."
    ry "Thought of what?"
    r "Have you ever thought of running away?"
    r "Just . . . leaving this insanity behind and run."

    menu escapechoice:
        "Honestly given the chance. I'd like to run too.":
            jump choicea2
            $reimi_pts += 5
        
        "I feel fine with this life.":
            jump choiceb2
            $reimi_pts -= 5


#[Choice A]
label choicea2:
    ry "Honestly, given the chance. I'd like to run too."
    r "Really?"
    ry "I get a little tired about this fortune telling stuff."
    r "That's kind of understandable."
    ry "Even if I can't run, I just want out of this business. I want to open an izakaya, you know."
    ry "I'd be happy, even with a life like that."
    jump commonroute2

#[Choice B]
label choiceb2:
    ry "I feel fine with this life, I've checked my fortune several times and I'll be fine"
    r "Well then, I mean . . . you do get decent pay. I'm not surprised hahaha."
    ry "Even if I do get rich, I don't want to be greedy like those folks."
    ry "Maybe I can even own my own izakaya."
    jump commonroute2

# Programmer's note: Both choices jump back to the common route label.in [back to normal]

#[back to normal]
label commonroute2:
    r "You're gonna serve your yakisoba there?"
    ry "Of course haha."
    ry "Speaking of, do you want some yakisoba?"
    r "Only if you do it at my place, I need an extra hand to clean up my room."
    ry "Well, we can go to the convenience store first then we go back to your place."
    r "Sounds like we got dinner!"

    "After finishing our ice cream, we decided to head to a local corner store to get some yakisoba."
    "Yakisoba is her favorite food, often saying that it reminds her of our childhood."
    "At the end of the day, the two of us decided to head home together."
    "But before that we decided to buy some things to add to our yakisoba."

"-Title Card: 30 minutes later-"
#[Transition to Reimi Room]
jump reimi_room
label reimi_room:
    scene bg room1
    with fade

    show reimi happy
    with fade
    r "Ahhhh, I'm beat."

    "Reimi shouted, immediately jumping onto her bed."

    ry "Can you at least take the gas stove out while I prepare the ingredients"
    r "Yeah, give me a minute."

    "Eating yakisoba together is almost tradition at this point, she prepares to cook the noodles while I prepare the other ingredients."
    "Sliced pork yakisoba is a delight."
    "After some preparations I started working on the Yakisoba."

    r "It's relaxing to do this sometimes, though I wish we could invite more friends."
    ry "You don't have friends in the arena?"
    r "I do but I'm just afraid if they'll disturb these quiet moments, haaaa."
    ry "I don't mind honestly, the more the merrier."
    r "I thought you were more low-key, you know. You seem to be the type to enjoy a smaller company."
    ry "Well, for one I feel like I need more social interaction."
    r "True, true."
    ry "By the way, get two plates, the yakisoba is done."

    "Reimi sat on her bed while I sat on the floor leaning against the closet."
    "These small moments, even if its just eating a simple meal."

    r "Haaaaa, Ryou-chan. Your yakisoba is the best!"
    ry "You don't have to put it that way."
    r "I'll try to invite friends when I have the time!"
    ry "Mhm, it might be fun honestly."

    #TODO transition and bg for this scene 
    scene bg apartment out
    with fade
    "After eating, I decided to clean up and as quickly as I arrived, I walked home alone."
    "By this point the moon was bright . . ."
    "The walk home was somber, accompanied by the chirping of birds."
    "Having friends like Reimi keeps me going, even though we live completely different lives . . ."
    "She's really one of the few people who care for me."
    "I opened the door to my house and dropped onto my bed."
    "Before I knew it, I fell asleep"
    jump day_2
#[End Day 1]


label day_2:
    scene bg room
    with fade
    # Chapter 2 begins here.
    "I woke up slightly late this morning, resolving to take the day easy."
    "Brushing my teeth before a breakfast of ramen and leftover bottled tea, I decide to eat on my bed and watch some early morning cartoons."
    "The peak of decadence in this part of town, by most standards."
    "*Knock knock*"
    "Past tense now, I guess. Sigh..."
    "I try to look as presentable as I can with my pajamas."
    "Of course, not *too* presentable. Can't let them think I'm so cheap they can just knock on my door first thing in the morning."
    "I take a deep breath, and open my front door."
    "What greets me is three young men, sharply dressed."
    "All three wear an armband identifying them as low ranking members of the Yosano Group."

    scene bg apartouter
    with fade

    ry "Who is it?"
    yh1 "Good morning, fortune-teller. I am here under the orders of Madame Yosano."
    yh1 "Madame Yosano asks for your presence post haste."
    yh1 "Transportations will be provided. We have a car waiting."
    yh1 "Sounds like something important, alright."
    ry "Give me 30 minutes."
    yh1 "Understood."

#---
#[A/N Car interior BG]
# NOTE I'll use bg shinjuku as a placeholder for now.
    scene bg shinjuku
    with fade
#...
#[A/N Ringtone]
    "I frantically reached into my pocket for my phone and out of reflex rejected the call."
    ry "I'm sorry, I forgot to put this damn thing on mute."
    yh1 "That's fine, you may answer it."
    ry "That's not what I me-"
    yh1 "We are sworn to secrecy, if that is what's required at the moment."
    "Sigh..."
    "It was Reimi. Of course it was Reimi."
    "A double serving of sigh coming right up."
#[A/N WA ringtone or something similar]
# Note, NVL Mode Here
    rit ":("
    rit "pick your damn phone jerk"
    ryt "I'm busy."
    rit "fine be like that"
    rit "what am i supposed to do with this ticket for the shinjuku arena fight later this afternoon then"
    ryt "I don't know, you have lots of friends, you'll figure something out."
    rit "everyone has backstage pass already dumbass"
    jump arenachoice

    menu arenachoice:
        "Go to the Arena":
            $ choice = "1"
            jump choice1arena
        
        "Don't Go to the Arena":
            $ choice = "2"
            jump choice2arena


label choice1arena:
    ryt "Fine, I'll go."
    rit "cool see you after the fight you can pick up the ticket at the usual spot"
jump day2commonroute
#[A/N End Alt A]


label choice2arena:
    ryt "Just write an ofuda on it or something."
    ryt "You actually are a miko, right?"
    rit "ha ha very funny"
    rit "maybe i'll even attach it to your head see if that fix your personality or something"
jump day2commonroute

#[A/N End Alt B]

label day2commonroute:

    "Never a dull moment..."

#---
    scene bg shinjuku
    with fade

    "Ichigaya."
    "Back in the days before the catastrophe, this was a commercial center for Old Tokyo. That, and where the defenders of the old world convened. Or traded death, depending on how jaded you are."
    "These days, it's colored more by small workshops and houses of the city's artisans, creating whatever trinkets the city's elites may want."
    "The car stops just before Akebonobashi, where it crosses the Yasukuni-Dorei, now a canal towards the Kanda River."
    "The Kanda River went up all the way to the hill where the Shinjuku City Council of Guilds and Neighborhood Associations complex now stands."
    "The beating heart of the city's government, one may say."
    "Well, that, and the Yosano Group's compound. Guess which one is more important these days?"
    "To be sure, the Yosanos still have quite the influence and thus vested interest in the Shinjuku municipal government."
    "One can even say the city government and the Yosanos are joined at the hips these days."
    "But considering the breakdown in public order and the incessant gang wars, it's not wrong per se to say that the city government is filled with Yosano goons, or at least not trusted."
    "I'm not one for politics, but I don't even remember anyone from my ward even giving lip service to the government anymore."

    "One boot for another, I guess. Not much difference between those wearing a badge and those with a Kei armband."
    "Entering the compound was a slight uphill trudge, all under the watchful eyes of the city constables, daring you to make a move."
    "As I am about to take up the steps into the City Council building, the henchmen that have been silent for the entire journey stopped me, holding my arms."
    yh1 "Master fortune-teller, as per standard procedure, from this point on, I must respectfully request you be blindfolded."
    yh1 "Madame Yosano has many enemies, unfortunately, and this is simply a precautionary measure. On her behalf, I must apologize."
    yh1 "Ah, no phones either, I'm afraid."

    "I simply nodded and handed over my phone, allowing myself to be blindfolded. He then proceeded to frisk me."
    "After that, I can feel my body being gently prodded from behind, pointing where I should walk."
    "Not long after, I can feel the upward motions of an elevator."
    "And then it stops. The man gently prodded me forward out of the elevator and allowed me to release my blindfold."
    "What greeted my eyes was no other than the personal office of Hibana Yosano, one of the two heads of the Yosano Group."

    yh "Ah, the fortune-teller, come, sit. I have been expecting you."
    "And speak of the devil herself."
    "Hibana Yosano has a fearsome reputation. The Shinjuku Council of Guilds and Neighborhood Associations was very recently an independent organization, a fourth sphere in the city."
    "Within 2 years, that organization has been subsumed completely under the Yosano Group."
    "Either this is something really important or this is some kind of test."
    "And I don't know which is worse."
    yh "Thank you for bringing the young master over, young man. Now, could you be a dear and bring some tea for him too?"

    yh1 "Of course, madam." #[A/N Closing door sound]

    "Cunning as a fox, word on the streets say."
    "She doesn't look any different from any shopkeeper granny, no."
    "But you don't hold the Council in just a couple of years without having a few tricks up your sleeve."

    yh "Now, in regards to why I summoned you, next week, the city hall is organizing Obon."
    yh "My husband would like to contribute handsomely to the endeavor."
    yh "I was wondering if this particular course of action is an auspicious one."

    "...That's it?"
    "This isn't even in my line of work, this should be Reimi's stuff!"

    ry "Of course. That should be rather simple."

    "I begin the standard fortune telling procedure."

    ry "Now, if you could please put your hands around this necklace."

#---

    yh "Well, it does seem that things are fine as is."
    yh "You can pick up your payment when you leave the building, I believe the hourly rate is still the same?"
    ry "Ah, actually I'd rather not charge you the full amount, we've barely gone past 30 minutes."
    ry "Wouldn't feel right."
    yh "Ah. Then why not do small talks?"
    ry "It's okay, I'll take-"
    yh "I insist, young man."
    ry "...Fine. Do note this means I'll charge by the hour."
    yh "Naturally."
    yh "Now, how has life been treating you so far?"
    ry "So-so I guess. Can't complain."
    yh "I'd imagine being the go-to fortune teller for the city's underworld would pay well."
    yh "Have you considered moving out of the undercity? After all, it is within your means."
    ry "I like the neighborhood. Can't see myself moving up like that, honestly."
    yh "Ah, yes, good neighbors. Can't really buy those I suppose."
    yh "Speaking of neighbors."
    "Here we go. What has she got up her sleeve now?"
    yh "Is it not unfortunate that one must have such unruly neighbors?"
    yh "The collapse of the constabulary last year was bad enough, but now this frightful wave of violence."
    yh "Open street fighting in Kabuki-Cho, gunning down of yakuza members in broad daylight in view of the public…"
    ry "I don't think it's my place to comment on such matters."
    yh "Surely someone in the middle of all this cannot afford to have no opinion?"
    ry "I'll try my best, madame."
    yh "Even if he were to, hypothetically, be called by one of the main actors of this play, who isn't quite sure if she'll make it through with her head on her shoulder?"
    ry "..."

    "How'd she know?!"
    "Calm down, Ryouhei. Deep internal breathes. More bark than bite."

    ry "*Especially* if that were the case, madame."
    yh "A man of integrity. Not a common sight."

    "She proceeded to pull something out of the obi of her red floral kimono."
    "...A gun?"
    "Pointed at my head?!"

    yh "This is hypothetical, of course, but would that same integrity stay with a sword pointed at your neck?"

    "A hypothetical sword yes, but a very real gun!"

    yh "Now, what did that disgrace ask? And how did you answer her?"
    ry "I-I can't possibl-"

    "She proceeded to put her finger on the trigger, and smiled."

    yh "Don't make this hard on either of us, master fortune-teller, getting blood out of velvet is such an inconvenience."
    ry "Y-you're asking me to breach the confidence clients enjoy, and I can-"
    "*Bang*"

    "Hibana Yosano let out an amused hum. And I am still alive."
    "It was now obvious that the shot was a blank, but I damn near shat myself right then and there."

    yh "Now this is a rarity."
    yh "Perhaps the faith the Old Cabal placed upon you was not misplaced at all."

#---

    "he rest of the time was spent in actual small talks. Or attempts to."
    "I cannot even hold a conversation after a gun is pointed at my head."

#[A/N Door opening noises]

    x "Mother, it's time for your division with the Council President."
    yh "Oh my, is it that late already?"
    yh "This has been a pleasant hour, master fortune-teller, but I must take my leave."
    yh "If you do not mind, my son Haruo will escort you out."
    ry "That would be fine."
    yh "Splendid. Haruo, if you would do the honors?"
    h "Of course. If I may."

    "I allow myself to be blindfolded yet again."
    "At least they’re respectful about it. Can’t say the same about the other clients."
#---

    h "Here is your phone, and here is your payment."
    ry "...You didn’t put a bug or anything on this right?"
    h "Heh, of course not. If anything I’d actually encourage you to have it checked just in case."
    h "My parents try their best to keep their words, and in your case they’ve seen that respect is mutual."
    ry "Good to know."


    "As I accepted the enveloped payment, I am tempted"
    "to ask how the Yosanos found out what the Ozakis asked."
    "But I figured that would be asking for trouble, so I kept my mouth shut."

    h "Well, pleasure doing business with you, master fortune-teller."
    ry "Please, just Ryouhei is fine. We’re the same age, give or take, from the looks of it anyways."
    h "Of course, Ryouhei-san. Of course, I must now take my leave."
    ry "Sure, I’ll also be on my way."
    if choice == "1" :  
        jump menua

    else:
        jump choice2postarena

    
#---

label menua:
#[A/N Start of Alt A Backstage or Night City CG]

    ry "Great fight."
    r "I aim to entertain." #(A/N Smug)
    r "By the way, I have someone I want to introduce you to."
    r "Ta-daaaa! Meet my friend and colleague, Takeshi."
    tk "Pleasure to meet you. Reimi seems to have taken a liking to you."

    "Guy’s massive. I wouldn’t be surprised if he is ex-constable."
    "Gotta make a living I guess."


    tk "You told me this guy can tell your fortune?"
    r "Never misses too, guy’s got talent."

    "Well, capital T Talent, yes, but no need to advertise that."

    ry "Putting that aside, is this okay?"
    r "I wouldn’t have invited you if it wasn’t okay."
    ry "Not that. You guys have to keep the act in public, right?"
    r "First time I heard of it."
    tk "Old school too. Where’d you find this relic?"
    r "The lower town is an interesting place."
    tk "Can’t disagree, won’t disagree."
    r "Anyways, since today is my payday-"
    ry "Mine too as a matter of fact."
    r "Shhh. I’m paying, and I’m hankering for some izakaya yakitori."

    "I shrugged. I wasn’t about to turn down a free dinner, after all."

    tk "Well, I guess you’re paying for some glasses too?"
    r "Sure, throw it in, I’m feeling generous today."
    jump menub

label menub:

#---

#[A/N Izakaya CG]
    r "Man, I’m full."
    r "I'm gonna go worship the Porcelain Throne for a bit, you boys don't kiss each other while I’m away."
#[A/N Shuffling boots sounds]
    ry "So, Takeshi. Can I call you that, by the way?"
    tk "Go ahead, I won't bite."
    ry "Cool. I’m actually kinda curious, you don’t seem like the type to actually start his career with ring fights."
    tk "Well, you don’t look like the type that can afford being around this neighborhood."
    ry "Fair. You first or me first?"
    tk "Janken?"
    ry "Janken."
    jump izakayab

# implemented a jump for fade effect 
#---

label izakayab:
    tk "Really?"
    ry "Hey, at least it pays well enough."
    tk "Your soul’s being sucked completely straight out of your body though."
    tk "I know those types."
    tk "Well I guess that makes for a good place for me to make an entrance."
    tk "As you can probably guess, I was an undertown cop. 13th Precinct."
    ry "Isn’t that the worst part of town?"
    tk "Yep. Every Yakuza deal gone wrong, every gangland murder, it all happens there."
    tk "Well, it used to happen there. After I got pushed out of the Constabulary, Council Hall started pulling out of the undertown."
    tk "Said something about fiscal responsibility and budgetary deficits, but that sounds like a buncha bull to me."

    "Well, it kind of isn’t. The city always had a smuggling problem and I’d guess it put the budget into a death spiral."
    "And put quite a few constables out of jobs from the looks of it."

    tk "I’m one of the luckier ones, honestly."
    tk "When that happens, there’s three things that can happen to you."
    tk "You get reassigned to uptown, you work with the Yakuza, or you end up homeless."
    ry "You’re still somewhere between alternatives two and three though."
    tk "Nice, I like a sharp guy." #[A/N Sincere]
    tk "Yes and no. This gig is paying enough and I also sell stuff on the side."
    tk "Nothing hot. Just vegetables I grow on my own time."
    ry "You know, from your looks I was half expecting guns or something hotter."
    tk "Well, I can sell you that too but then I’ll have to arrest you."
    tk "That said I’ve got some old world chilis growing if that’s what you’re talking about."

    "We both laughed at the pun."

    r "What are you guys laughing about?"
    ry "Nothing, nothing hot."
    r "Takeshi?"
    tk "I plead my right to remain silent"
    r "Grrrhhhh-"
    ry "I don’t think you can handle the spice, Reimi."

    "Takeshi started to snort again, suppressing his laughter."

    r "Seriously you two-"
    ry "Man I better bail before this miko bonks me."
    ry "See you around Take-"

    # TODO ADD SPECIAL EFFECTS HERE SMH

    "Takeshi locked my arms before I even got to stand."

    tk "If you wanna find out what he said, you really should find his spot."
    r "O-hoooo? Tickle torture? I like the way you think."


    "Gulp...."
    "This is going to be a long night..."
    jump day_3

#[A/N End of Alt A]

label choice2postarena:

#[A/N Start of Alt B, night in front of house BG]
    "I unlock the door to my house, its familiar clicking a comforting noise." 
    "The job I’m doing pays well, but by all that is holy sometimes it feels like it’s not worth it."
    "A gun pointed at my head and a blank fired at me for 400 yen an hour..."
    "I make more than 20 times an hour most other workers in this god-forsaken city do, but how much does hazard pay go?"
    "Every day, a creeping feeling of emptiness keeps creeping into the back of my mind."
    "What do I want? Where do I want to be? Why am I still here?"
    "Maybe that damn viper is right, I should move up."
    "But then again..."

    "The vibrations of my phone in my pocket pulled me out of my thoughts."
    "Reimi again. This time with a picture, her with a massive guy, eating together in an izakaya."

    rit "hows work?"
    rit "jealous yet?"

    "Urghhhh..."

    ryt "Really not in the mood for this, Reimi."
    rit "jeez they treat you that badly?"
    ryt "If only you knew."
    ryt "Not in the mood to tell a story. Talk to me tomorrow."
    rit "ew prickly"
    rit "sure good night sweet prince <3]"

    "I swear…"
    "I’d kill for great coworkers."
    "Sigh..."
    "I’ll just take a bath, make something and go to sleep."
    "It’s not like tomorrow’s going to be any worse."
    "Kind of hard topping having a gun pushed up to your head at work."
#[A/N End of Alt B]
    "I sleep. hoping tomorrow would be better"
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
