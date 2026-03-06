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

define bgnarr = Image("gui/textboxnarr3.png", xalign = 0.2, yalign = 9.5, xsize = 0.8)
define r = Character("Rat", color = "#ffffff", outlines = [ (absolute(2), "#000", absolute(0), absolute(0)) ], callback=type_sound)
define c = Character("Cat", color = "#ffffff", outlines = [ (absolute(2), "#000", absolute(0), absolute(0)) ], callback=type_sound)
define u = Character("   ")
define n = Character(None, window_background = bgnarr, what_xpos = 0.2, what_ypos = -2.45, callback=type_sound)
define e = Character(None, window_background = None, what_xpos = 0.3, what_ypos = 0.15, callback=type_sound)

label rat_start:
    play drip "audio/Drip8.ogg" loop volume 0.4
    play music "audio/ChoicelessFinal.ogg" volume 0.5
    window hide
    scene alley bg
    with dissolve
    n "It's a dark night..."
    n "Quiet, save for the stirring of little creatures."
    n "The mouse pokes its nose out of its hole, sniffing."
    n "Encouraged, it emerges from its hiding place."

    show rat normal at left
    with dissolve
    r "{i}It will be a perfect night{/i}"
    r "{i}Once I make it back.{/i}"
    n "It takes a few tentative steps, preparing to dash across the street."

    menu:
        "Run":
            jump rat_ending1
        "Wait":
            jump rat_scene1
    

label rat_scene1:
    show rat p2 at left
    r "Hail, o hunter!"
    show rat normal at left
    u "..."
    show rat p2 at left
    r "I beg you not to insult me by pretending you're not there. You've been spotted, my dear nemesis."
    show rat normal at left
    show cat normal at right
    with dissolve
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
    c "Me, kill and feast on a human child?!"
    show rat mad at left
    r "Get off your high horse."
    r "I know you've no problem feasting on humans. Or children for that matter, as I'm sure you've raided your fair share of nests for chicks."
    show cat normal at right
    c "That's—"
    r "Different? Different how? What makes the humans different?"
    r "What makes it so you would eat any of my pups with no hesitation, but a human is where you draw the line!?"
    c "Human are..."
    r "Humans are your self imposed masters!"
    r "Heavens bear witness to he who calls himself a hunter, yet prostrates himself before his oppressors for a few drops of supper!"
    c "..."
    show rat smile at left
    r "It's barely even alive. It'll die on its own soon enough."
    r "But then, the bottom feeders will get the bulk of it."
    r "Will you take action now? Or will you starve in the name of a misguided mercy?"
    show rat normal at left
    show cat narrow at right
    c "Watch yourself."
    show cat normal at right
    r "..."
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

    menu:
        "Take a Bite of the Toes":
            jump rat_ending2
        "Take a Bite at the Neck":
            jump rat_ending3

label rat_ending1:
    play sound "audio/NeckSnap.ogg" volume 0.6
    scene bg_dead
    pause 1.0
    return

label rat_ending2:
    hide rat normal
    hide cat normal
    show bg_choose
    play other "audio/NeckSnap.ogg" volume 0.6
    e "The rat bends its head as soon as it hears the crunch of the claws tearing into flesh."
    e "With a jerk of its head, it rips off the toe it had been taking small bites off."
    play drip "audio/Scamper1.ogg" loop volume 1.0
    e "It runs, dragging its prize back to its  dubious home."
    e "There are mouths at home to feed."
    $ persistent.rat = True
    return

label rat_ending3:
    hide cat normal
    r "{i}I deserve a more juicy reward tonight, don't I?{/i}"
    hide rat normal
    show bg_dead
    e "Then—"
    e "A twitch of the hand."
    e "Before the rat can recoil, the hand closes,"
    e "squeezing"
    e "lifting"
    e "The world swims; air is gone."
    e "Through the blur, the last thing it sees is the cat’s tail, vanishing into the dark."
    e "A grim humor settles in its mind as the child’s mouth closes over its head."
    play other "audio/NeckSnap.ogg" volume 0.6
    e "It has no regrets."

    $ persistent.rat = True
    return


