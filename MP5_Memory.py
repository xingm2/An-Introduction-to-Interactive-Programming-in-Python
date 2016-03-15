# implementation of card game - Memory

import simplegui
import random

deck = range(8)
deck.extend(range(8))
random.shuffle(deck)

exposed = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];



edex1 = 0
edex2 = 0

turns = 0

# helper function to initialize globals
def new_game():
    global state  
    state = 0
    global exposed
    exposed = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
    global turns
    turns = 0
    global  edex1, edex2
   
    edex1 = 0
    edex2 = 0
    random.shuffle(deck)
    label.set_text('Turns = 0')
     
# define event handlers
def mouseclick(pos):
    global turns
    
    
    # add game state logic here
    global state
    
  
    global edex1
    global edex2
    if exposed[pos[0] // 50] == 0:
        if state == 0:
            state = 1
            exposed[pos[0] // 50] = 1
            edex1 = pos[0] // 50
            
            
        elif state == 1:
            state = 2
            exposed[pos[0] // 50] = 1
            edex2 = pos[0] // 50
            
             
            print edex1, edex2
        else:
            if deck[edex1] != deck[edex2]:
                exposed[edex1] = 0
                exposed[edex2] = 0
            
            edex1 = pos[0] // 50
            state = 1
            exposed[pos[0] // 50] = 1
            turns += 1
            
        label.set_text('Turns = ' + str(turns))
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for card_index in range(len(deck)):
        card_pos = 50 * card_index + 20
        if exposed[card_index] == True:
            canvas.draw_text(str(deck[card_index]), (card_pos, 50), 20,'White')
        else:
            canvas.draw_polygon([(card_pos-20, 0), (card_pos-20+50, 0), (card_pos-20+50, 100),(card_pos-20,100)], 5,'Red','Green')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)


# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
