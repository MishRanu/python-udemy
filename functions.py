#working on how functions work and how we can create them for ourselves
#function is a block of code so def has to be followed by a colon

def python_food():
    width=80
    text="spam and eggs"
    left_margin = (width-len(text))//2
    print(" "*left_margin,text)


def center_text(text):
    text=str(text)
    left_margin= (80-len(text))//2
    print(" "*left_margin, text)

#call the function
python_food()
center_text(12)
center_text("spam, spam and eggs")
center_text("spam, spam and spam and spam")
