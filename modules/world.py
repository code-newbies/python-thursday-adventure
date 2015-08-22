# world.py
"""This module contains game content that is not in a specific level"""

def initial_narration():
    """Returns the beginning narration of the game"""
    text = """
Once a very very long time ago an intrepid hero dared to stand up
against the low-sodium cartel.  Our hero knew that the shortage of
pork belly could only have been caused by their brand of devious
evil.

The low-sodium cartel had reportedly been hoarding pork belly in
their underground lair.  There could only be one reason for this,
they wanted to cause a bacon shortage.

Now you must go and enter the dark and moss covered room filled
with evil in order to rescue the big pile of bacon.

It is dark and you light a torch...
        """
    return text

def final_narration_win():
    text = """
After exploring all the rooms and levels of the low-sodium cartel's secret
underground lair, our hero emerges victorious. The planned shortage of delicious 
pork belly has been thwarted, and our hero even leaves with the spoils of her
courageous quest.

With sword in hand, gold in pocket, and a heap of giant cockroach carcasses in
the corner, our hero departs for home and breakfast, bacon in hand.

TL;DR She brought home the bacon. Congratulations!
        """
    return text

def final_narration_lose():
    text = """
After exploring all the rooms and levels of the low-sodium cartel's secret
underground lair, our hero emerges slightly worn, but with morale high.
The planned shortage of delicious pork belly has been thwarted, but no where
during the quest did our hero stumble upon the stash of wonderful wood-smoked,
salty bacon.

With sword in hand, gold in pocket, and a heap of giant cockroach carcasses in
the corner, our hero departs for home and breakfast, dreaming of bacon to come.
        """
    return text
    
