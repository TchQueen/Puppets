screen choose_route:
    add "bg/bg_route.png"
    # This button will delete any persistent variable
    button:
        text "Clear History": 
            idle_color "#fff"
            hover_color "#c0c0c0"
        action Function(renpy.game.persistent._clear)

    # horizontal box containing the 5 image buttons
    hbox:
        xalign 0.5
        yalign 0.5
        yoffset 30  
        spacing 20

        imagebutton:
            auto "choices/rat_%s.png"
            action Jump("rat_start")
        imagebutton:
            auto "choices/cat_%s.png"
            action Jump("cat_start")
        imagebutton:
            auto "choices/human_%s.png"
            action Jump("human_start")
            sensitive persistent.rat == True or persistent.cat == True