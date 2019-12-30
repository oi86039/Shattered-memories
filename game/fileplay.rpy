default found_sprite = False
default found_evil = False
default found_alex = False
default found_extr = False
default found_child = False
default found_all = False

$found_sprite = False
$found_evil = False
$found_alex = False
$found_extr = False
$found_child = False
$found_all = False

label fileplay:
    r "Now for the nitty gritty..."
    hide neutral
    show happy
    r "It's time to combine the mechanics presented here to do something rather close to how it's handled in the finished product."
    hide happy
    show talking
    r "We're going to fix a character that was never finished by the creator."
    hide talking
    show neutral
    r "Her name is Margo."
    hide neutral
    show talking
    r "Her memories and files are scattered within the game files. We'll need to find them."
    hide talking
    show neutral
    r "Here. I've made a folder just for her."
    
    r "Assemble what you find there."
    
    r "Go!"
    
    jump loopfile

label loopfile:
    
    if renpy.loadable("Margo/Alex.mem"):
       $ found_alex = True
    if renpy.loadable("Margo/Extrovert.mem"):
       $ found_extr = True
    if renpy.loadable("Margo/Childhood.mem"):
       $ found_child = True
    if renpy.loadable("Margo/Margo_Neutral.png"):
       $ found_sprite = True
    if found_alex and found_extr and found_child and found_sprite:
        $ found_all = True
        
    if found_all:
        r "...."
        hide neutral
        show happy
        jump win
    else:
        r "...."
        r "You still have some files missing. Keep looking..."
        jump loopfile
        
label win:
    r "Well done!"
    hide happy
    show neutral
    r "Let's see if I can load her in..."
    
    show neutral at left
    with move
    
    define m = Character("Margo")
    define e = Character("E")
    image margo = im.FactorScale("Margo/Margo_Neutral.png",0.27)
    
    r "..."
    
    show margo at right with dissolve
    m "....."
    m "W-where am I?"
    
    show neutral
    
    hide neutral
    show happy at left
    r "Hello Margo! Glad to see a familiar face again."
    hide happy
    show neutral at left
    m "What.. is this place? Who are you? Why am I in black and white?!!!"
    
    hide neutral
    show talking at left
    r "Do you not remember me, Margo? It's me, Rosemarie! The creator didn't exactly finish you yet."
    hide talking
    show neutral at left
    m "Creator?!! Y-you mean?!!!"
    
    hide margo
    
    e "Error!!!: .mem files have been corrupted. Unloading \'Margo_Neutral.png\'"
    hide neutral
    show angry at left
    r "Well that's a shame."
    
    show angry at center
    with move
    
    r "Looks like the files weren't as stable as I thought. No wonder the creator sealed her off."
    hide angry
    show neutral
    r "You did good, though. I was a bit naive."
    hide neutral
    show talking
    r "I just wanted a companion is all. But oh well. It's not the end of the world."
    
    r "It is a bit strange how she was unloaded as soon as I told her that though..."
    hide talking
    show angry
    r "Maybe this demo has some strange properties that the creator hasn't accounted for."
    hide angry
    show neutral
    r "Regardless, let's head back."
    
    return
    
    