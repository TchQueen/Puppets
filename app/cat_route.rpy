define sounds = ['audio/A1.ogg']

init python:
    renpy.music.register_channel("drip", "sfx", loop=True)

init python:
    renpy.music.register_channel("other", "sfx", loop=False)

init python:
   def type_sound(event, interact = True, **kwargs):
      if not interact:
         return

      if event == "show": #if text's being written by character, spam typing sounds until the text ends
         renpy.sound.play(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))
         renpy.sound.queue(renpy.random.choice(sounds))

      elif event == "slow_done" or event == "end":
         renpy.sound.stop()

define bgnarr = Image("gui/textboxnarr.png", xalign = 0.1, yalign = 9.5, xsize = 0.8)
define r = Character("Rat", color = "#ffffff", outlines = [ (absolute(2), "#000", absolute(0), absolute(0)) ], callback=type_sound)
define c = Character("Cat", color = "#ffffff", outlines = [ (absolute(2), "#000", absolute(0), absolute(0)) ], callback=type_sound)
define u = Character("   ")
define n = Character(None, window_background = bgnarr, what_xpos = 0.1, what_ypos = -2.45, callback=type_sound)
define e = Character(None, window_background = None, what_xpos = 0.3, what_ypos = 0.2, callback=type_sound)


label cat_start:
    play drip "audio/Drip8.ogg" loop volume 0.4
    play music "audio/ChoicelessFinal.ogg" volume 0.5
    window hide
    scene alley bg
    with dissolve
    n "It's a dark night..."
    n "Quiet, save for the stirring of little creatures."
    n "The cat slinks through the darkness; the sound of movement is more than welcome."
    n "It tastes the air and... yes. There."
    n "It watches as a nose twitches out of a hole."
    n "It'll emerge soon, the cat knows, and so it takes careful steps towards its prey."
    show cat small at topright
    c "{i}It will be a perfect night{/i}"
    c "{i}Once I catch it.{/i}"
    n "But the rat stops. Its eyes swivel."
    u "Hail, o hunter!"
    c "..."
    show rat normal at left
    with dissolve
    show rat p2 at left
    r "I beg you not to insult me by pretending you're not there. You've been spotted, my dear nemesis."
    show rat normal
    hide cat small
    show cat normal at right
    with moveinright
    c "Hmph!"
    show cat narrow at right
    c "And I'll beg you not to insult me by speaking to me, rat."
    c "I can chase you down if I please, seen or not."
    show cat normal at right
    show rat p2 at left  
    r "Chase you may, but my home isn't far by any means."
    r "Then we shall both be left hungry and tired."
    r "A near perfect night thwarted."
    show rat normal at left
    show cat narrow at right
    c "Oh?"
    c "And if I let you go, what shall I have in return then? It seems to me I'll be left with nothing either way."
    show cat normal at right
    show rat smile at left
    r "And if I said I have a proposition for you? What then?"
    c "I'm not interested in whatever scraps you feed on, vermin!"
    r "Not scraps, no..."
    c "Go on."
    r "In that alley over there, lies a human child."
    r "You see, its toes have been providing me with quite a bit of nourishment for the past few nights."
    r "From my last foray, I suspect it's not long for this world."
    show cat angry at right
    stop music fadeout 3.0
    c "Spit it out. What are you suggesting?"
    r "Finish it off, cat."
    r "Put an end to its miserable existence."
    play other "audio/Hiss5.ogg" volume 0.5
    play music "audio/ChoicelessFinal.ogg" volume 0.5 fadein 1.5
    c "Have you taken leave of your senses?"
    show cat narrow at right
    c "Me, kill and feast on a human child?!"
    show rat mad at left
    r "Get off your high horse!"
    r "I know you've no problem feasting on humans. Or children for that matter, as I'm sure you've raided your fair share of nests for chicks."
    c "That's..."
    r "Different? Different how?"
    r "What makes the humans different?"
    r "What makes it so you would eat any of my pups with no hesitation, but a human is where you draw the line!?"
    c "Human are..."
    r "Humans are your self imposed masters."
    r "Heavens bear witness those who call themselves hunters, yet prostrate before their oppressors for a few licks of milk!"
    c "..."
    show rat smile at left
    r "It's barely even alive. It'll die on its own soon enough."
    r "But then, the bottom feeders will get the bulk of it."
    r "Will you take action now? Or will you starve in the name of a misguided mercy?"
    show rat normal at left
    c "Watch yourself."
    show cat normal at right
    n "The cat stares at the rat, absorbing every detail. Its beedy red eyes, the gleam of its coat."
    n "The cat remembers the baker who lays out milk every few days, and his impudent child from whom treats can be stolen."
    n "These are all things that keep the cat afloat..."
    n "But just barely."

    menu:
        "You're Correct":
            jump cat_ending1
        "Take Me to the Unfortunate Creature":
            jump cat_scene1
    

label cat_scene1:
    c "Take me to the unfortunate creature."
    n "And that was that."
    scene aza
    with fade
    n "The child lies alone, half hidden in a pile of human filth."
    show rat p2 at left
    r "Listen for yourself. It's barely breathing."
    show rat normal at left
    show cat narrow at right
    c "Enough platitudes. I'm carrying out the deed regardless."
    show cat normal at right
    hide rat normal
    with dissolve
    show cat angry at right
    n "Forgive me, child."
    jump cat_ending2


label cat_ending1:
    show cat narrow at right
    c "Your're correct."
    c "A cat {i}is{/i} a hunter."
    c "The heavens would laugh at me if I forsake my duty."
    hide cat narrow
    scene bg_choose
    play other "audio/NeckSnap.ogg" volume 0.6
    e "Quick as thought, the cat springs forward."
    e "The rat was also wrong;"
    e "It was caught before it could make it into its hole."
    e "The cat kills it in one swift bite."
    e "It will be a meal worthy of being respected."
    $ persistent.cat = True
    return

label cat_ending2:
    hide cat angry
    scene cat death
    e "In the corner of its eyes, it registers a small twitch of the child's hand."
    e "A blink later, and its hands are wrapped around its neck, squeezing."
    e "The cat watches the rat flee around the corner, and bares its teeth."
    play other "audio/NeckSnap.ogg" volume 0.6
    e "When the final crack echoes in its head, all it feels is relief."
    $ persistent.cat = True
    return
