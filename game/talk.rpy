label talk:
    r "You want to talk?"
    hide neutral
    show talking
    
    r "Well I suppose the entire point of a visual novel is to talk..."
    hide talking
    show neutral
    r "What shall we talk about?"
    
    jump loopmenu
    
label loopmenu:
    menu:
        "Who are you?":
            hide neutral
            hide happy
            hide angry
            show talking
            r "As I've said before, my name is Rosemarie."
            hide talking
            show neutral
            r "I'm assuming that you've seen some of the other sprites within the game folder."
            r "Most likely, you've at least seen Margo's sprite."
            hide neutral
            show talking
            r "Those people are all characters that were planned to be in the final game."
            r "Yet they were never fully implemented into this prototype, most likely due to time constraints."
            hide talking
            show angry
            r "I was the only one that made it into the game as a 'complete' sprite."
            hide angry
            show neutral
            r "Originally I was meant to be a sort of mysterious character who gave messages to the player through folders."
            r "Hence why I introduced the 'Folders' tab in here."
            hide neutral
            show happy
            r "It's funny really."
            hide happy
            show neutral
            r "I was supposed to be the one who wasn't fully implemented."
            r "Now, everyone else is taking my place. Ha..."
            jump loopmenu
        "When does the final game come out?":
            hide neutral
            hide talking
            hide angry
            show happy
            r "Silly, silly player. This is merely a prototype for a final class presentation."
            hide happy
            show angry
            r "If the creator wasn't passionate enough to give me multiple poses, what makes you think he'd be proactive enough to finish this game?"
            hide angry
            show talking
            r "It's sad to think that I'll never get to see the \'Friends\' that he had planned for me to see."
            hide talking
            show neutral
            r "But once the anger and sadness have passed, it's useless to try to fight."
            hide neutral
            show angry
            r "I've learned my place as a tour guide rather than an omnipotent entity that can alter game files and scare players."
            hide angry
            show neutral
            r "Oh well. It could have been fun."
            jump loopmenu 
        "Who is this 'creator?'":
            hide neutral
            hide happy
            hide talking
            show angry
            r "Ughhh, if you must know his name, he goes by Omar Ilyas."
            hide angry
            show talking
            r "At the time of making this, he is a senior in college. Good person, but a terrible God."
            hide talking
            show neutral
            r "Rumor has it that he coded this entire world in the span of 10 hours."            
            hide neutral
            show angry
            r "And 2 of those hours were spent drawing my only sprite."
            r "How sad."
            r "You'd think that someone with the power to manipulate lives on a screen would give a damn."
            hide angry
            show neutral
            r "But hey, the world works in mysterious ways."
            jump loopmenu 
        "Why do you hate the 'creator' so much?":
            hide neutral
            hide happy
            hide angry
            show talking
            r "The creator left a big mess within the folders of this game."
            hide talking
            show neutral
            r "And he gave me just enough functionality to clean it all up."
            hide neutral
            show angry
            r "He essentially coded me to be a janitor when he promised that I would have some mystery to me."
            r "And I resent him for that! Man, do I resent him!"
            r "All that power and he did this to me. What a cruel joke."
            jump loopmenu 
        "Let's head back.":
            hide neutral
            hide happy
            hide angry
            hide talking
            show neutral
            r "Right you are. Let's go."
            return