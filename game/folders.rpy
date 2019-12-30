label folders:
    
    hide neutral
    show talking
    r "Shattered Memories features a variety of communication methods."
    
    r "Aside from looking you right in the face and speaking, I can make my own folders in the game folder and talk through there."
    
    hide talking
    show neutral
    r "Now you may be asking, \"What\'s the point? Can\'t you speak here just fine?\""
    
    r "And you may be right, but there will be times where..."
    
    hide talking
    show faceless
    r ".....!"
    jump loop
    
label loop:
    r "...."
    if (renpy.loadable("Rosemarie/Ugh_ I hate when this happens/Frustrating/But I'm ok/Just delete this file for me so we can move on.ok")):
        jump loop
    else:
        jump done
        
label done:
    hide faceless
    show happy
    r "Oh thank goodness!"
    
    hide happy
    show talking
    r "You have no clue how much I hate it when my face disappears."
    
    hide talking
    show neutral
    r "Don't you hate that too?"
    
    hide neutral
    show angry    
    r "I swear, this creator needs to get his act together..."
    
    hide angry
    show neutral
    r "Anyway, let's head back."
    
    return