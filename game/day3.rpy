# This is the script for day 3.

# IMPORTANT: Be sure to uncomment the dialogue!
# I had to comment the later lines for the project to be able to run (and be tested as a result).

label day_3:
    # VN Day 3
    # [Setting: Ryohei’s Apartment Bedroom]
    # Alarm Clock Sounds 
    "I woke up to the sound of my phone’s alarm"
    ry "Ah, it seems morning has come yet again"
    "I reached out and turned off the alarm" 
    "Still lying on the bed I mumbled to myself"
    ry "Ngahh, waking up just doesn’t get easier does it?"
    "I spent a few more minutes just lying on the bed and staring at the ceiling"
    "A text notification broke the silence, I grabbed my phone and started reading the text"
    
    ist "My office, 10 a.m., don’t be late."
    
    "To no one’s surprise the text was from yet another empire in Upper Shinjuku"
    "But to my surprise the text was sent from Isurugi Hirotsu himself"
    "The head of House Hirotsu, another one of the Big 3 in Upper Shinjuku"
    ry "That’s a first, usually one of his henchmen would send the memo"
    ry "Ah shit, wait … how should I reply?"
    ry "Being casual with him is definitely out of the question…"
    ry "I guess being formal is the only option here"
    "I quickly typed up the reply" 
   
    ryt "Understood Sir…." 
    ryt "thank you …"
    ryt "for the …"
    ryt "reminder…"
    ryt "I shall …"
    ryt "see you… soon."
    
    "And sent"
    nvl clear
    "With the clock on my phone showing 9:10 a.m. I finally got out of bed and prepare myself for the day"
    "I took the usual route and hop onto one of the trams"
    #[Setting: Trams]
    scene bg trams
    with fade
    "During the tram ride I re-read the text I received this morning"
    "Granted checking back on a text is something a typical young adult would do"
    "However I am not a typical young adult, where other people would check back on a text by their loved ones"
    "Here I am checking back on a text sent by the head of a powerful crime empire"
    "The more I thought about why he sent it himself the less it makes sense"
    "Best case scenario is that I’m trustworthy and he respects me enough to reach out to me personally"
    "Worst case scenario is that he’s eager to show me something either to flex his influence, power, or both" 
    to "We’ll be arriving at out next stop shortly, please be prepared if you are departing here"
    "The announcement made by the tram operator cut off my stream of thoughts"
    #[Setting: Upper Shinjuku/ any city shot]
    scene bg shinjuku
    with fade
    "As I walked off the tram and made my way to the Hirotsu building I can’t help but feel uneasy"
    "Sure I’ve done this a couple of times, visiting crime syndicates is nothing new to me"
    "But a text from the head of said syndicate is definitely new"
    #[Setting: Receptionist] JESUS THATS A LOT OF BG CHANGES
    scene bg receptionist
    with fade
    "Upon entering the building I talked to the receptionist about my appointment with Isurugi Hirotsu"
    "At the sound of my request to meet the man himself the receptionist just replied with a quizzical look"
    "After a few moments she then proceeded to ask"
    rc "I’m sorry sir, but are you sure about having an appointment with the owner?"
    "This line of questioning isn’t really new to me either"
    "Due to the nature of my work and my services to these empires, only a handful of people in the staff actually know of these appointments at any given time"
    ry "Yes I’m sure, I even got a text from the man himself"
    "I showed her the aforementioned text"
    "In an instant her face turned pale and tried to force a smile at the sight of the text"
    rc "I see, well everything seems to be in order"
    ry "Great, I’ll head for the elevator then"
    rc "Yes that would be ideal, but let me give you a word of advice"
    rc "Be respectful at all times to Mr.Hirotsu."
    rc "those who receive that text rarely walk out those doors again"
    "Hearing those words it was my turn whose face turned pale and forced a smile" 
    ry "T-thanks for the heads up… I g-guess"
    "She sent me off with a worried smile as I made my way to the elevators"
    #[Setting: Elevator]
    # Scene is elevator, and have it play elevator music untill scene changes.
    "Looks like the worst case scenario happened"
    "I can’t do much about it now, but it looks like I’m gonna have to kissass more to get myself out of this mess"
    "The elevator ride was a long one, seeing as his office was at the highest floor of the building"
    "My thoughts are swimming with plans on how to survive this encounter" 
    "The elevator music with its mellow and melancholic melody played throughout the elevator ride"
    "I mean it is elevator music, but those sweet melodies that once helped me calm down after every appointment with these mob bosses"     
    "It felt like they were mocking me with the occasional interruption to my train of thought" 
    #[Setting: Hallway]
    "Until finally the dreaded “Ding” arrived signaling that I have arrived on my destination"
    "With heavy steps I walked up to the door and knocked" 
    "The doors opened up slowly to reveal Tatsuki Hirotsu opening the doors"
    #[Setting: Fancy Office] JESUS CHRIST!
    "Not wanting to be rude I rushed inside and bowed myself before the famed son of the Isurugi Hirotsu"
    "Once inside I was greeted with the sight of the typical mahogany desk and a chair facing the window"
    "As I was staring Tatsuki made his way to stand beside his father"
    "The moment Tatsuki arrived the chair slowly turned towards me revealing none other than Isurugi himself"
    "With a small empty rock glass in hand he stood up"
    isr "Ryohei my boy, thanks for coming… I have always liked your punctuality." 
    ry "W-well you are a client of mine … where would I be without my clients?"
    # TENTATIVE, have the bgm interupted here for laughing SFX, or a chukle of an old man
    "Isurugi laughs"
    isr "That humility of yours is something I also love"
    isr "Now tell me… Are you a spirits guy or more of a cocktail guy?"
    ry "Neither sir…"
    isr "More for me then"
    "As he says this he makes his way to a small table with a mixology kit sitting on top and started fixing himself a drink"
    ry "Uh sir? Aren’t you going to use Samsara?"
    isr "Eager to get this over with I see"
    ry "That’s not what I me---"
    isr "I can’t blame you, I would like this done soon too"
    isr "I will use Samsara, but I gotta take care of something first, and for that this drink is going to help"
    isr "Tatsuki, go and fetch our guests for our appointment today, I’m just about done with this drink"
    "Tatsuki nods and leaves, nothing but the stirring of Isurugi’s drink echoed through the room with the occasional sip"
    "The silence was finally broken when Tatsuki entered the room with 3 bodyguards of House Hirotsu beaten and bruised"
    "This is fucked, I have no words to describe this"
    "Is this how they treat their own staff?"
    "My stomach suddenly tied up in a knot I could feel myself breaking into a cold sweat"
    "Isurugi soon took notice of my plight" 
    isr "You alright boy? I thought you were used to this kind of sight, working with the big 3 and all"
    ry "Actions speak louder than words sir" 
    ry "Threats and aftermaths are one thing, but seeing it done live is something else"
    isr "I guess it’s just like those music concerts you young’uns go to, seeing it live is different"
    isr "Are you regretting turning down that alcohol offer?"
    "Isurugi sips his cocktail and laughs at the jab he made"
    isr "Relax a bit kid, seeing the way you’re trembling there, I bet that receptionist told you my personal message as being something of a calling card to off you" 
    ry "S…S-something along those lines sir"
    isr "I can see why she would misunderstand something like that, lately I’ve been using that message of mine as advertised"
    isr "Not too long ago that message was also something of a promotion of sorts to my associates." 
    isr "kinda like saying ‘I shall be handling business with you on a personal level’ cutting the middleman"
    ry "Which one of those instances apply to my case?"
    "Isurugi laughs and stood up from his desk making his way to the 3 beaten up staff members"
    isr "Kid, as long as you’re loyal and don’t fuck up your head is still going to be attached on your shoulders" 
    isr "Can’t say the same for these rats though" 
    "Isurugi forcefully grab one of the traitors by the hair and proceeded to explain what’s about to happen"
    isr "Alright listen up you maggots, you will receive disciplinary action to redeem yourself for betraying me, whether you pay with your life or not depends on you"
    "Isurugi went over to his desk, started to rummage around and pulled out a handgun"
    isr "I’m in a celebrating mood with Ryohei’s ‘promotion’ so I’m feeling a little kind today, let’s hear what you gotta say"
    rk "I...I plead g-guilty for what I’ve done sir , I see no way outta this mess so I’m coming clean"
    isr "I see, since what you did was something minor and your rank was not high enough to cause real problems, I’m gonna give you a choice."
    rk "Oh! T-thank you sir, I’ll do anything you ask"
    isr "Well then, here’s my offer, you walk out from this life and you get punished severely, or you stay and work to the bone and get off with a lighter punishment, and let me tell you working here won’t get any easier"
    "A brief silence befell the room, all eyes were on the rookie anticipating what he will say next"   
    "the rest of us know all too well that what Isurugi said was true, this line of work will never get easier"
    rk "I-- I will d-dedicate myself to you sir, I’ll w-work hard to atone for my sins"
    isr "Stupid choice rookie, but i respect it, go find Gotou about your punishment"
    rk "Y-yes Sir"
    "The rookie stood up and left, leaving only 2 more awaiting their judgment"
    isr "What about the rest of you? Got anything to say?"
    tt "Nothing sir..."
    isr "Not gonna say anything about you being a mole?"
    tt "Nope, not gonna add anything you don’t know sir, not even regret"
    tt "I was just doing my job, i’ve pledged loyalty to my employer and that’s that"
    isr "I like your work ethic, shame you ain’t workin for me"
    isr "Seeing I’m on good terms with the big 3, that would make your employer a small timer in Shinjuku" # The Big 3? or the Rest of the Big 3?
    isr "Small timers ain’t worth my time and yours, so you wanna work for me or not?"
    tt "No sir, I’ve pledged loyalty and that’s final"
    isr "Well, I’ll take that as verbal confirmation that you betrayed me"
    isr "At least this next part will be easier for me, and since I’m feeling generous I’ll let you off if you manage to keep your consciousness"
    "Isurugi loaded his gun, he twirled and fiddled with it for a while, you could see the traitor’s face getting paler with every twirl of Isurugi’s gun"
    # TODO Isurugi "Gunsprite"
    "Until Isurugi finally stopped and looked me dead in the eye with his gun pointed right at me"
    ry "U-uh Sir? I believe the gun is ---"
    scene black
    with fade
    # Insert Gun SFX here
    "*BANG!!!*"
    "AHHHHHHH!!!"
    scene bg shinjuku
    with fade
    "I flinched and instinctively shouted only to realize I was completely fine and i wasn’t the one who shouted"
    "As adrenaline started rushing I could see Isurugi still pointing the gun at me"
    isr "Burn this image in your mind, just in case you get funny ideas about betrayal"
    "Isurugi winked at me right after finishing that sentence and quickly averted his attention to the traitor writhing in pain"
    isr "Congrats, you survived the first shot, you’re one of the few who didn’t pass out right away"
    tt "A-ah, WHAT THE FUCK DID YOU DO"
    isr "As simple as using my ability, to put simply I can control bullets"
    isr "I redirected the bullet headed towards Ryohei straight to one of your intercostal space"
    tt "Iii-intercostal space?"
    isr "The space between your ribs"
    "I lightly pressed one of said spaces with my thumbs, and quickly discomfort grew, I could only shudder at the thought of a bullet passing through"
    isr "Do your best to keep your consciousness if you want to live"
    "*BANG!!!*"
    tt "AAAAHHHH, FUCK!"
    isr "Still conscious eh? Well not to worry you got about 23 spaces available and i got about 7 bullets left"
    isr "You know what they say, Third time's the charm"
    "*BANG!!!*"
    "This time no scream was heard, just silence as the traitor slumped over"
    isr "Ah well, I really thought he was gonna survive until the 3rd bullet at least"
    isr "Tatsuki, wake the man up, and no need for manners"
    "Tatsuki nodded and proceeded to kick the traitor square on his injured ribs, and without delay the traitor was jolted awake"
    tt "Who-wha, where…?"
    isr "Rise and shine snake, you lost your consciousness, you know what that means" 
    isr "You lose your life" #Omae wa MOU shindeiru lmao
    tt "W-wwait, sir just, let’s not do anything rash here"
    isr "Funny, the only rash thing done today was your cocky attitude"
    tt "P-pplease g-give me another chance"
    isr "Tatsuki, take care of him please"
    "The traitor only kept begging for his life harder as Isurugi muttered those words, but no amount of begging and grovelling changed Isurugi’s mind"
    "Tatsuki seems to show no hesitation in drawing his sword and in one fluid motion he swung his sword and sheathed it"
    "The cut was clean, so clean in fact the traitor’s head slid off the base of his neck, the room went from cries and wails to instant silence"
    "*Click*"
    isr "Be a dear for me and ask Gotou to reserve a table for one please"
    rc "A-an actual table sir?? or the---"
    isr "Yes, the clean-up kind"
    rc "A-aah right a-away sir"
    isr "I’ll tell you this since you\’re still new, I\’ll reserve an actual table if I mention an actual place, got it?"
    rc "L-loud and clear sir"
    isr "Great, we’re set then, don’t forget about telling Gotou"
    rc "Y-yes sir"
    isr "Good"
    "*Click*"
    "With Isurugi's conversation over the intercom done he turned his attention to the last person left unpunished." 
    "The last staff to be judged was visibly shaken, cold sweat had broken out far before that fiasco with the traitor."
    "Before Isurugi could ask what was wrong the man broke down in tears asking for forgiveness, begging even harder than the traitor."
    isr "Calm down boy, I'm not gonna give ya a verdict without hearing your reasons"
    st "I'm sorry for the unsightly display sir… I was just desperate"
    isr "Well, seeing your reaction i guess it's safe to assume you're guilty and regretting it right now"
    st "Yes sir, right now I’m stuck between a rock and a hard place"
    isr "So? Why’d you do it?"
    st "I had to sir, I was blackmailed to do those things"
    isr "Blackmailed? Do they have evidence of your fucked up fetish on their hands?"
    st "I wish it was, they got my family,  my wife and kid"
    isr "Family eh? What happened if you don't mind my asking?"
    st "My kid needs money for his hospital bills, my savings couldn't entirely cover it"
    isr "Let me guess, you went to loan sharks because of your affiliation with House Hirotsu?"
    st "Yes sir, but it was mostly out of principle, I'm trying to be affiliated with this life as little as possible"
    isr "That's the first time I've ever heard such a reason, so you didn't try to show off you worked for me?"
    st "Well, my wife doesn't really approve of this line of work, I try my best to avoid things affiliated with the big 3 outside of work"
    isr "So since it was a personal matter,  you went to the loan sharks with that mindset but it ended up backfiring?"
    st "That's the gist of it, when it came time to pay the loan what I had wasn't enough to clear the interest"
    st "So the trashed my house and was about to harm my family, I blurted out that I worked for House Hirotsu in hopes it would scare them"
    isr "But they got greedy and wanted you to do things else they hurt your family, which they have taken in case you chicken out? That right?"
    st "Yes sir that's the whole story"
    isr "Honestly things would've been easier for you had you went to one of the banks we own, but I can respect a man who's got integrity"
    st "I agree sir, and I'm ready to receive my punishment for this, all I ask is you don't mess up my face too much, wouldn't want my kid not recognizing his old man on his own funeral"
    isr "You went from begging for your life to accepting death pretty quick"
    st "I realized I've lived a good life, and should I die right now, I'd at least stuck to my principles and integrity besides with me gone, there's nothing they could do about my debt"
    isr "That is quite the mature thought, up until that last statement anyway"
    st "W-what do you mean sir?"
    isr "Well with you outta the picture they'll just focus even more on your wife and kids, right now they're just bargaining chips against you, but as soon as you're out..."
    isr "Believe me, things ain't gonna be pretty"
    st "S-so what you're saying is my wife and kids won't be free even if I die? But there's no one to pay them!"
    isr "I don't know if I should laugh or feel sorry for your naivety kid, in this business someone's gotta pay"
    st "So it doesn't matter even if I die?"
    isr "I'm afraid not kid, so you ready to die?"
    st "No, not until I know my family is safe, if I'm dying either way at least I want to die trying to save my family"
    isr "Good answer kid, your punishment has been nullified, besides I feel the initial beatdown was punishment enough for someone who's got intentions like you"
    st "B-but sir I fucked up"
    isr "Kid, you're looking out for your family to the very end despite death staring you at the face, I need more people like you here"
    isr "Tatsuki, help this man here get his family safe"
    st "T-thank you sir, I'll never forget this"
    "The man started bowing as tears build up in his eyes, but before the waterworks could burst he was led by Tatsuki outside of the office"
    ry "Didn't take you for the understanding kind"
    isr "I'm just taking care of my property, simple as that"
    ry "So was that part of the reason you're the one who texted the memo?"
    isr "It was a showcase of power and perks I guess, truth be told I trust you enough to be dealing with you hands on"
    isr "Well, with that done hand Samsara over"
    ry "As you wish sir"
    "I took Samsara off my neck and threw it to Isurugi, he caught it with ease and started peering into Samsara, and not long after he threw it back."
    ry "That was quite the quick one"
    isr "Well I don't have any major projects going on, so it was merely about maintenance, if you could even call it that "
    ry "I'll take my leave then sir"
    isr "Money will be transferred to your account as usual"
    ry "Appreciate it sir"
    isr "Word of advice kid, never betray me, your death would be painful and the other big 3 would consider it a favor having a rat removed"
    ry "As if today was not enough of an example, I'll be waiting our next appointment sir"
    isr "Heh, take care kid"

#[Streets]
    scene bg streets
    with fade
    "With that I left the building, and once again i found myself wandering the streets of Upper Shinjuku only to be disturbed by the sound of my stomach growling" 
    "I looked on my phone, the clock read 11:12 a.m still far from lunch time but considering I haven't had breakfast I think it's a fair time for the growling"
    #[Convenience store]
    scene bg conveniencestore
    with fade
    "I went to the nearest  convenience store to grab some cup ramen, as i was searching for the cup ramen i saw some bargain pocky sticks, somehow they remind me of Reimi"
    jump conveniencestorechoice

    menu conveniencestorechoice:
        "She's probably fine, besides I think I had enough excitement for one day with House Hirotsu, I'll just buy some cup ramen and go home":
            jump day3choiceA

        "I'd Go eat cup ramen with Reimi.":
            jump ramenpath


label ramenpath:
    if flag_1 == True:
        "Well eating with other people is always better the izakaya yesterday proved that, besides cup ramen ain't the healthiest, I'll buy some ingredients here and then drop by her place"


    else:
        "I wonder how Reimi's doing after her match yesterday? I guess I'll drop by her place after buying a couple of ingredients"

    "I put the cup ramen back and proceeded to grab some ingredients, nothing much really just some vegetables and some meat enough for a hotpot for 2 and went up to the cashier to pay. I gave her a tip for her troubles. "
    #[Streets]
    "Making my way to Reimi's place was nothing new to me, I've been there on several occasions, the new thing was dropping by unannounced, in my head I kept practicing on what to say to make this visit seem natural, try as I might I couldn't come up with something."
    "Finally I was at her front door, and after hesitating a couple of seconds I finally knocked."
    #[Door]
    "*Knock, Knock, Knock*"
    ry "Reimi?? it's me Ryohei, open up I bought some stuff"
    "A voice was heard from the room"
    r "Ah, Ryo-chan? Hold on I'll be right with you, you better not have bought cup ramen with you"
    ry "Hey, cup ramen is what I eat alone, I bought some ingredients for a hot pot"
    "The door opened revealing Reimi in casual clothes."
    r "Well come in"
    ry "Yeah thanks"
    #[Reimi's Apartment]
    r "I was surprised you visit Ryo-chan, this is a first you showing up uninvited"
    ry "Yeah,  I was in a convenience store nearby and the pocky they sell reminded me of you"
    ry "Ah. Where should I put this by the way"
    r "Just put in on the table, I'll prepare the pots"
    ry "Sure"
    "Reimi prepared the pot and stock for our hotpot while I was preparing the ingredients, mostly cutting the vegetables, and preparing the rice. The meat was packaged after they were fillet so it didn't need much prep work." 
    "As the stock simmered it's fragrance filled the room we quickly dropped in the vegetables and the meat, and I carried the pot to the table whilst Reimi was scooping the cooked rice into bowls for the both of us." 
    "We sat down and we ate our fill. After eating, we spoke about everything and nothing. I stayed at Reimi's for quite some time, and seeing that it had gotten dark outside I decided it was time to go home."  

    ry "Well, I better get going, thanks for having me Reimi"
    r "Hold up Ryo-chan, I got something for you"
    "Reimi went off to her room and rummaged around for a bit"
    r "Here you go, as thanks for dropping by"
    ry "A charm?"
    r "Not just any charm, it's a lucky charm"
    r "With your line of work I figured you could use the extra luck"
    ry "Thanks Reimi, I'll be sure to treasure this..."
    ry "Well, I'll be going for real now then… See you tomorrow"
    r "Sure, see you tomorrow"
    #[Outside Nighttime]
    "I went out the door and made my way home, the journey home was a silent one, I couldn't even think about anything. Today was so hectic, and all I want now is just to sleep"
    jump day3choiceA
    #[Ryohei's bedroom]
    #Choice A merger
label day3choiceA:
    "Before I knew it, I was at my doorstep. I went inside and started my hygiene routine before bed, after I showered I felt the munchies come, so I prepared some cup ramen."
    "Once finished I brushed my teeth and lay in bed." 
    "Today took a lot out of me, as I scrolled through my phone I could already feel the drowsiness taking over, and before I could realize I was closing my eyes and my consciousness started fading fast."
return
    #[Day 3 End] 
