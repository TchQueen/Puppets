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
define h = Character("Child", color = "#ffffff", outlines = [ (absolute(2), "#000", absolute(0), absolute(0)) ], callback=type_sound, what_italic=True)
define s = Character("   ", callback=type_sound)
define n = Character(None, window_background = bgnarr, what_xpos = 0.1, what_ypos = -2.45, callback=type_sound)
define e = Character(None, window_background = None, what_xpos = 0.3, what_ypos = 0.15, callback=type_sound)


label human_start:
   play drip "audio/Whipser2.ogg" loop volume 0.03
   play music "audio/ChoicelessFinal.ogg" volume 0.5
   window hide
   scene aza
   with dissolve
   n "The child can't see the skies, but it assumes the night must have come again."
   n "It licks its lips, not that it makes any difference."
   n "There is no saliva to wet it."
   n "There is only this: the oppressive dark swimming in and out of focus."
   n "The skittering of little creatures."
   n "The soft growl of a cat."
   n "The faint sound of the child's ever-stuttering breath."
   n "It tries to remember its name. The word slips away."
   n "Perhaps it never had one. Perhaps nothing does."
   n "The child becomes aware of movement at the mouth of the alley."
   n "The shadows stretch and morph into the unknowable."
   n "It seems to the child that the shadows watch it."
   s "Look! They've come to kill this unfortunate thing."
   show creature at midright
   with dissolve
   s "How fortunate, to have it put it out of its misery."
   show creature p2 at midright
   s "Tell me, child"
   show creature at midright
   s "Do you want to die?"
   show creature p2 at midright
   n "The child has long since lost the ability to speak, but it answers with the strength of its soul."
   h "No."
   show creature at midright
   s "And why not? Your existence has been nothing but misery."
   show creature p2 at midright
   s "You're already standing at Death's door."
   show creature at midright
   h "..."
   show creature p2 at midright
   s "Is it fear, young thing? Do you fear Death?"
   show creature at midright
   h "Yes."
   show creature p2 at midright
   s "And if I told you there was nothing to fear?"
   show creature at midright
   s "And if I told you Death cares for its charges?"
   show creature p2 at midright
   s "What if I said you would find hope, and warmth if you let it take you?"
   show creature at midright
   n "The child can feel pressure on its body. It barely registers the soft breath of vermin as they crawl over it."
   n "It struggles to remember what warmth feels like. It thinks it must be nice."
   h "And what is hope?"
   s "..."
   show creature p2 at midright
   s "It is the thing you most need."
   hide creature p2
   with dissolve
   n "It feels the soft brush of fur on its feet. Sees the glint of something sharp over its head."

   menu:
      "Fight":
         jump human_ending1
      "Close your eyes":
         jump human_ending2

label human_ending1:
   h "No."
   n "For the first time in days, the child is flooded with strength."
   h "I will find my own hope."
   stop drip fadeout 3.0
   stop music fadeout 3.0
   play music "audio/ChoicelessOutro.ogg" volume 0.5
   scene bg_choose
   with dissolve
   play other "audio/NeckSnap.ogg" volume 0.6
   e "The child reaches out, quicker than the space between seconds, and grabs hold of the first thing it touches."
   play drip "audio/Gulp1.ogg" loop volume 0.03
   e "There's a feeble struggle, but the child pays it no mind as it raises the squirming thing to its mouth."
   h "Ah, yes. This is hope."
   return

label human_ending2:
   stop drip fadeout 3.0
   stop music fadeout 3.0
   play music "audio/ChoicelessOutro.ogg" volume 0.5
   scene bg_dead
   with dissolve
   e "The claw rushes towards the child's neck, and it closes its eyes."
   play other "audio/NeckSnap.ogg" volume 0.6
   e "There's no hope yet, but it finally understands warmth."
   return



