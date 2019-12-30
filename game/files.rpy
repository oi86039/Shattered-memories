label file_found:
    show happy
    r "Very good. Simple right?"
    hide happy
    show talking
    r "Use files to access different story paths. Simple enough, but it can be used for some real fun!"
    hide talking
    show happy
    r "We'll access a more hands on example further down the list."
    hide happy
    show neutral
    r "Let's head back."
    
    return

label files:
    hide neutral
    show talking
    r "File manipulation is the heart of Shattered Memories. However, it is not mandatory."
    hide talking
    show neutral
    r "You can play the entire game through without touching anything in the game folder."
    hide neutral
    show happy
    r "But where's the fun in that?"
    hide happy
    show talking
    r "To set this game apart from other Visual Novels, certain files within the game folder will be movable and changable."
    
    r "This way, the player can feel as if he/she has unique control over the game in ways that don't seem \"intended\"."
    hide talking
    show neutral
    r "Let me illustrate this."
    hide neutral
    show talking
    r "Inside the game folder, you will find a memory with my name on it."
    hide talking
    show neutral
    r "Give it to me please."
        
    if renpy.loadable("Rosemarie/Rosemarie_Childhood.me"):
        hide neutral
        jump file_found
    
    r "..."
    
    if renpy.loadable("Rosemarie/Rosemarie_Childhood.me"):
        hide neutral
        jump file_found
        
    r ".."
    
    if renpy.loadable("Rosemarie/Rosemarie_Childhood.me"):
        hide neutral
        jump file_found
        
    hide neutral
    show angry
    r "."
    
    if renpy.loadable("Rosemarie/Rosemarie_Childhood.me"):
        hide angry
        jump file_found
        
    r "You didn't give me my file...."
    
    r "Were you not listening? Or were you testing to see if it was required to move the file?"
    hide angry
    show neutral
    r "Ughhh. Forget it. Let's jump back to the rest of the demo."
    
    return
