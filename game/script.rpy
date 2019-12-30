# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Rosemarie")
image neutral = im.FactorScale("Rosemarie_Neutral.png",0.37)
image talking = im.FactorScale("Rosemarie_Talking.png",0.37)
image happy = im.FactorScale("Rosemarie_Happy.png",0.37)
image angry = im.FactorScale("Rosemarie_Angry.png",0.37)
image faceless = im.FactorScale("Rosemarie_Faceless.png",0.37)

image movie = Movie(fps=1, size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)
define audio.ambiance = "music/Ambiance.mp3"

# True if this is the first time through the tutorials.
default tutorials_first_time = True

init python:

    # A list of section and tutorial objects.
    tutorials = [ ]

    class Section(object):
        """
        Represents a section of the tutorial menu.

        `title`
            The title of the section. This should be a translatable string.
        """

        def __init__(self, title):
            self.kind = "section"
            self.title = title

            tutorials.append(self)


    class Tutorial(object):
        """
        Represents a label that we can jump to.
        """

        def __init__(self, label, title, move=True):
            self.kind = "tutorial"
            self.label = label
            self.title = title

            if move and (move != "after"):
                self.move_before = True
            else:
                self.move_before = False

            if move and (move != "before"):
                self.move_after = True
            else:
                self.move_after = False

            tutorials.append(self)


    Section(_("Main mechanics"))

    Tutorial("files", _("File Manipulation"))
    
    Tutorial("folders", _("Folder Tracing"))
    
    Tutorial ("fileplay", _("Rebuild Margo"))
    
    Section (_("Miscellaneous"))
    
    Tutorial("talk", _("Talk to Rosemarie"))
    
    Tutorial("credits", _("Credits and Sources"))

screen tutorials(adj):

    frame:
        xsize 640
        xalign .5
        ysize 485
        ypos 30

        has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
                for i in tutorials:

                    if i.kind == "tutorial":

                        textbutton i.title:
                            action Return(i)
                            left_padding 20
                            xfill True

                    else:

                        null height 10
                        text i.title alt ""
                        null height 5




        bar adjustment adj style "vscrollbar"

        textbutton _("That's enough for now."):
            xfill True
            action Return(False)
            top_margin 10


# This is used to preserve the state of the scrollbar on the selection
# screen.
default tutorials_adjustment = ui.adjustment()


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play movie "giphy.ogv" loop
    show movie with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    play music ambiance
    
    show neutral
    with dissolve
    
    # These display lines of dialogue.

    r "Greetings, IT 265. I'm glad this game is at least semi-functional."
    
    hide neutral
    show talking

    r "My name is Rosemarie. I will guide you through the Shattered Memories demonstration."
        
    r "Unfortunately, my creator was not gracious enough to finish this game, or even give me multiple sprites."
    
    hide talking
    show neutral
    
    r "Nonetheless, I will do my best to exemplify what makes Shattered Memories so wonderful."
    
label tutorials:

    show neutral at left
    with move

#interact = False is used to skip to the next line without the player clicking

    if tutorials_first_time:
        show talking at left
        $ r(_("Take a look...") )
    else:
        $ r(_("Anything else?"))

    hide talking
    $ tutorials_first_time = False
    $ renpy.choice_for_skipping()

    call screen tutorials(adj=tutorials_adjustment)

    $ tutorial = _return

    if not tutorial:
        jump end

    if tutorial.move_before:
        show neutral at center
        with move

    call expression tutorial.label from _call_expression

    if tutorial.move_after:
        hide example
        show neutral at left
        with move

    jump tutorials

label end:

    show neutral at center
    with move

    r "Over already... I'm surprised."
    
    hide neutral
    show angry
    
    r "Or are you simply testing to see if the quit button works?"
    
    hide angry
    show talking

    r "Bah. No matter the case, I hope you saw some of the light that Shattered Memories is trying to shine."
    
    hide talking
    show neutral

    r "Of course, this isn't perfect, by any means. It was made in a few hours for all I know."

    r "But..."
    
    hide neutral
    show happy
    
    r "I doubt you found everything that was placed in secret here..."

    hide happy
    show talking

    r "Do look next time. That's the main draw of the game after all..."
    
    r "Finding what's outside of the game as opposed to in."
    
    hide talking
    show neutral
    
    r "Goodbye."

    # This ends the game.

    return
