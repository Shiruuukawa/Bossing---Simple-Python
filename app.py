import sys
import time

def display_message(message): # Text Animation for line 24
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(0.1)

# Yes or No input
def get_yes_or_no(prompt):
    while True:
        player = input(prompt).strip().lower()
        if player in ['yes', 'y', 'YES']:
            return True
        elif player in ['no', 'n', 'NO']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

# Start
if __name__ == "__main__": 
    message = "Hello! Are you ready?\n" 
    display_message(message) # Display Text (Animated from line 4)

# Yes or No response
    while True:
        response = get_yes_or_no("(yes/no): ")
        if response:
            print()
            break
        else:
            print("Omki, Have a nice day!") # If the Answer is NO
            sys.exit() # Will close the prompt

time.sleep(0.1) # Slight delay

def display_message(waitline): # Text Animation for line 47
    for char in waitline:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(0.1) # added another delay

if __name__ == "__main__":
    waitline = "Please wait...\n" # Just to make it realistic lol
    msg1 = ("Loading assets...\n") #    '   '   '   '   '   '   '
    msg2 = ("Loading library...\n") #    '   '   '   '   '   '   '
    display_message(waitline)
    time.sleep(1)
    display_message(msg1)
    time.sleep(1)
    display_message(msg2)
    time.sleep(1.4)

print() # White space lol

# get name
def display_message(greeting_message): # Text Animation for line 80
    for char in greeting_message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

def display_message(name1): # Text Animation for line 75
    for char in name1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

def get_user_name():
    name1 = input("Please enter your name: ")
    return name1

def main():
        user_name = get_user_name()
        greeting_message = f"Hello, {user_name}! Welcome."
        display_message(greeting_message)

if __name__ == "__main__":
        main()

print() # space for prompt
time.sleep(1.4) # time delay

def display_message(start): # Text Animation for line 98
    for char in start:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

def main():
    while True: # make it loop until 'G' is entered
        start = input("For confirmation, press 'G' to Start!: ").strip().upper()
        
        if start == 'G':
            display_message("Let's Go!")
            break
        else:
            print()
            display_message("KUPAL KA BA BOSS?")
            time.sleep(0.4) # short delay
            display_message("'G' lang hindi mo pa ma type!")
            print()
            
if __name__ == "__main__":
    main()


time.sleep(0.4) # slight delay
print() # White space lol
print() # White space lol

# Main Problem
txt1 = (
    "Gina left her house and walked to the church. "
    "Inside, she sat quietly, said a prayer, and felt peaceful. "
    "Afterward, she walked home feeling blessed and graceful."
)

def display_message(txt1): # Text Animation for line 119
    for char in txt1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(0.1)
sys.stdout.write('\n')

if __name__ == "__main__":
    display_message(txt1)

time.sleep(0.5)
print() # White space lol
print() # White space lol

direction = "Direction: Type the word of your answer" 

def display_message(direction): # Text Animation for line 140
    for char in direction:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

if __name__ == "__main__":
    display_message(direction)

time.sleep(2) # Delay
print() # White space lol

question1 = "Question: Where did Gina go?" # 1st Question

def display_message(question1): # Text Animation for line 155
    for char in question1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

if __name__ == "__main__":
    display_message(question1)

time.sleep(0.3) # short delay

def display_message(options):   # Text Animation for line 176
    for char in options:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

options = {         # options for the question in line 155
    "a": "church",
    "b": "mall",
    "c": "park",
    "d": "friend's house",
}

# Display options
for key, value in options.items():
    time.sleep(0.3)
    print(key, ".", value)

time.sleep(0.5) # short delay
print() # White space lol

while True:
    # Ask for the answer
    Answer = input("Answer: \n").strip().lower()
    
    if Answer in [opt.lower() for opt in options.values()]:
        if Answer == "church":
            while True:
                confirmation = input("Sure ka na? Oo o Hindi?: ").strip().lower()
                if confirmation in ["oo", "Oo"]:
                    print("Nadali mo boss!")
                    break
                elif confirmation in ["hindi", "Hindi"]:
                    print("Para ka namang hindi nag Grade 2 eh")
                    print()
                    
                else:
                    print("Invalid confirmation. Please enter 'Oo' or 'Hindi'.")
            break
        elif Answer == "mall":
            print("Try mo mag dasal sa mall kupal ka")
            print() # White space lol
            
        elif Answer == "park":
            print("Nandiyan ba si Lord?")
            print() # White space lol
            
        elif Answer == "friend's house":
            print("Nuyan by group mag pray?")
            print() # White space lol
            
    else:
        print("Invalid answer! Please try again.")
        print() # White space lol

time.sleep(2)
print()

question2 = "What was Gina doing inside the church?"    # 2nd Question

def display_message(question2): # Text Animation for line 228
    for char in question2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

if __name__ == "__main__":
    display_message(question2)

time.sleep(0.3) # short delay

def display_message(options): # Text Animation for line 249
    for char in options:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

options = {     # options for question in line 228
    "a": "She was doing a tiktok video",
    "b": "She cried",
    "c": "She was praying",
    "d": "She stole the altar",
}

# Display options
for key, value in options.items():
    time.sleep(0.3)
    print(key, ".", value)

time.sleep(0.5)
print() # White space lol

while True:
    # Ask for the answer
    Answer = input("Answer: \n").strip().lower()
    
    if Answer in [opt.lower() for opt in options.values()]:
        if Answer == "she was doing a tiktok video":
            print("Gago ka ba boss? HAHAHA")
            print()

        elif Answer == "she cried":
            print("Sabayan mo umiyak")
            print() # White space lol
            
        elif Answer == "she was praying":
            while True:
                confirmation = input("Sure ka na? Oo o Hindi?: ").strip().lower()
                if confirmation in ["oo", "Oo", "OO"]:
                    print("Nadali mo boss!")
                    break
                elif confirmation in ["hindi", "Hindi", "HINDI"]:
                    print("Bakit Hindi, kupal ka ba boss?")
                    print() # White space lol
                    
                else:
                    print("Invalid confirmation. Please enter 'Oo' or 'Hindi'.")
            break
            
        elif Answer == "she stole the altar":
            print("HAHAHAHA GAGO, siguro kawatan ka boss")
            print() # White space lol
            
    else:
        print("Invalid answer! Please try again.")
        print() # White space lol

time.sleep(2) # Delay
print() # White space lol

question3 = "Where did Gina go after praying at the church?" # 3rd Question

def display_message(question3): # Text Animation for line 302
    for char in question3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')  

if __name__ == "__main__":
    display_message(question3)

time.sleep(0.3)

def display_message(options):   # Text Animation for line 323
    for char in options:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

options = {     # options for question in line 302
    "a": "Mall",
    "b": "Home",
    "c": "Bar",
    "d": "She sold the altar",
}

# Display options
for key, value in options.items():
    time.sleep(0.3)
    print(key, ".", value)

time.sleep(0.5)
print() # White space lol

while True:
    # Ask for the answer
    Answer = input("Answer: \n").strip().lower()
    
    if Answer in [opt.lower() for opt in options.values()]:
        if Answer == "mall": #choice a.
            print("Pala gala ka sigurong kupal ka")
            print()

        elif Answer == "home": # choice b.
            while True:
                confirmation = input("Sure ka na? Oo o Hindi?: ").strip().lower()
                if confirmation in ["oo", "Oo", "OO"]:
                    print("Nadali mo boss!")
                    break
                elif confirmation in ["hindi", "Hindi", "HINDI"]:
                    print("ANO BAAAAAAA")
                    print()
                    
                else:
                    print("Invalid confirmation. Please enter 'Oo' or 'Hindi'.")
            break
            
        elif Answer == "bar": # choice c.
            print("Gaya mo pa siya sayo b1tch ka")
            print()
            
        elif Answer == "she sold the altar": # choice d.
            print("HAHAHAHA GAGO, kawatan talaga si boss")
            print() # White space lol
            
    else:
        print("Invalid answer! Please try again.")
        print() # White space lol

time.sleep(2) # delay
print() # White space lol

question4 = "What did Gina felt after she went home?" # 4th Question

def display_message(question4): # Text Animation for line 376
    for char in question4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

if __name__ == "__main__":
    display_message(question4)

time.sleep(0.3) # short delay

def display_message(options): # Text Animation for line 397
    for char in options:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

options = {     # options for question in line 376
    "a": "Horny",
    "b": "Sad",
    "c": "Happy since she sold the altar",
    "d": "Blessed and graceful",
}

# Display options
for key, value in options.items():
    time.sleep(0.3)
    print(key, ".", value)

time.sleep(0.5)
print() # White space lol

while True:
    # Ask for the answer
    Answer = input("Answer: \n").strip().lower()
    
    if Answer in [opt.lower() for opt in options.values()]:
        if Answer == "horny": #choice a.
            print("HAHAHA GAGO")
            print()

        elif Answer == "sad": # choice b.
            print("Sad girl ba si Gina?")
            print()
            
        elif Answer == "happy since she sold the altar": # choice c
            print("Kawatan na nga mukhang pera pa")
            print()
            
        elif Answer == "blessed and graceful": # choice d
            while True:
                confirmation = input("Sure ka na? Oo o Hindi?: ").strip().lower()
                if confirmation in ["oo", "Oo", "OO"]:
                    print("Nadali mo boss!")
                    break
                elif confirmation in ["hindi", "Hindi", "HINDI"]:
                    print("Kanina ka pang kupal ka")
                    print()
                    
                else:
                    print("Invalid confirmation. Please enter 'Oo' or 'Hindi'.")
            break
            
    else:
        print("Invalid answer! Please try again.")
        print() # White space lol

time.sleep(2) # Delay
print() # White space lol

thanking = "Thank you for participating!"   # Thank you message

def display_message(thangking):     # Text Animation for line 450
    """Displays a message with a typewriter effect."""
    for char in thanking:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

if __name__ == "__main__":
    display_message(thanking)

time.sleep(1) # 1 sec delay time

thanking2 = "Here is your cat as a token of reward!"
thanking3 = "See you soon!"

def display_message(thangking2):    # Text Animation for line 465
    """Displays a message with a typewriter effect."""
    for char in thanking2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

time.sleep(0.5) # short delay

if __name__ == "__main__":
    display_message(thanking2)

time.sleep(0.5)

def display_message(thangking3):    # Text Animation for line 466
    """Displays a message with a typewriter effect."""
    for char in thanking3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

time.sleep(0.5)

if __name__ == "__main__":
    display_message(thanking3)

time.sleep(1) # Delay

import turtle   
import colorsys
#Cute Cat uses turtle graphics
turtle.Screen().bgcolor("white")

t = turtle.Pen()

def go(x,y):
    t.penup()
    t.goto(x, y)
    t.pendown()


# Line 
go(-250,-100)

t.pensize(9)
t.forward(500)
t.backward(90)

t.seth(60)
t.pensize(5)
t.circle(180,240)

# Black dharia

t.fillcolor("#282929")
go(160,-100)
t.seth(60)
t.circle(180,55)

t.begin_fill()
t.seth(60)
t.forward(50)
t.circle(150,30)
t.circle(20,100)
t.circle(150,44)

t.seth(150)
t.circle(180,80)

t.seth(160)
t.forward(30)
t.circle(150,30)
t.circle(20,100)
t.circle(150,46)

t.seth(-95)
t.pensize(1)
t.circle(180,10)
t.seth(-15)
t.circle(120,80)

t.seth(-55)
t.circle(120,118)

t.end_fill()

# Left eye
go(-70,20)

t.fillcolor("black")
t.begin_fill()
t.circle(30)
t.end_fill()

go(-80,40)

t.fillcolor("white")
t.begin_fill()
t.circle(8)
t.end_fill()

# Right Eye
go(70,40)

t.fillcolor("black")
t.begin_fill()
t.circle(30)
t.end_fill()

go(60,60)

t.fillcolor("white")
t.begin_fill()
t.circle(8)
t.end_fill()

# Nose
go(-48,10)
t.pensize(5)
t.seth(-90)

t.fillcolor("black")

t.begin_fill()
t.circle(10,70)
t.circle(20,70)
t.circle(10,70)
t.circle(5,70)
t.forward(20)
t.circle(6,70)
t.end_fill()

# Mouth 
go(-30,0)
t.seth(-80)
t.forward(5)

t.fillcolor("#fa9393")
t.begin_fill()
t.circle(20,140)
t.circle(20,-140)
t.circle(-20,140)
t.circle(-20,-50)
t.seth(-80)
t.circle(20,180)
t.seth(190)
t.circle(-20,60)
t.end_fill()

# Left paw
go(-120,-95)
t.seth(-30)
t.fillcolor("white")
t.begin_fill()
t.circle(20,150)
t.circle(50,80)
t.circle(30,70)
t.forward(22)
t.end_fill()

go(-160,-90)
t.begin_fill()
t.circle(15,200)
t.end_fill()

t.seth(70)
t.begin_fill()
t.circle(-10,-220)
t.end_fill()

# Right paw
go(180,-97)
t.seth(75)
t.begin_fill()
t.circle(120,30)
t.seth(80)
t.circle(120,10)
t.circle(30,40)
t.seth(90)
t.circle(10,120)
t.seth(100)
t.circle(10,120)
t.seth(120)
t.circle(15,120)
t.seth(150)
t.circle(15,150)
t.seth(-120)
t.circle(40,50)
t.circle(-60,30)
t.circle(80,21)
t.end_fill()

go(130,-40)
t.seth(5)

t.pensize(1)
t.pencolor("#fa9393")
t.fillcolor("#fa9393")

t.begin_fill()
t.forward(20)
t.circle(8,90)
t.circle(20,170)
t.circle(10,105)
t.end_fill()

go(165,-15)
t.begin_fill()
t.circle(6)
t.end_fill()

go(150,-2)
t.begin_fill()
t.circle(7)
t.end_fill()

go(130,0)
t.begin_fill()
t.circle(7)
t.end_fill()

go(110,-15)
t.begin_fill()
t.circle(9)
t.end_fill()

# Ear red
go(160,100)
t.seth(45)
t.begin_fill()
t.circle(80,50)
t.circle(10,90)
t.circle(80,50)
t.seth(-25)
t.circle(-120,28)
t.end_fill()

go(-150,90)
t.seth(150)
t.begin_fill()
t.circle(80,50)
t.circle(10,90)
t.circle(80,50)
t.seth(80)
t.circle(-120,28)
t.end_fill()

t.hideturtle() # hide the turtle (cursor)

time.sleep(5) # delay to view the output

turtle.bye() # closes the turtle graphics window

time.sleep(1) # short delay for code to breathe

def countdown_timer(seconds): # timer
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds")
        time.sleep(1)  
        seconds -= 1  
    sys.exit() # Closes the prompt

# End