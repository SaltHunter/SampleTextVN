# This is the script for day 2, or chapter 2.

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
    $ flag_1 = True
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
    nvl clear

    "I swear…"
    "I’d kill for great coworkers."
    "Sigh..."
    "I’ll just take a bath, make something and go to sleep."
    "It’s not like tomorrow’s going to be any worse."
    "Kind of hard topping having a gun pushed up to your head at work."
#[A/N End of Alt B]
    "I sleep. hoping tomorrow would be better"
    jump day_3