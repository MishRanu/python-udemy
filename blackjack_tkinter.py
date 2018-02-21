try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

import random



def load_cards():
    pack = []
    face_cards = ["king", "queen", "jack"]
    suits = ["club", "diamond", "spade", "heart"]
    extension="png"

    for suit in suits:
        for i in range(1, 11):
            name = "cards/{}_{}.{}".format(str(i), suit, extension)
            image = tkinter.PhotoImage(file=name)
            pack.append((i, image,))

        for face_card in face_cards:
            name = "cards/{}_{}.{}".format(str(i), suit, extension)
            image = tkinter.PhotoImage(file=name)
            pack.append((10, image, ))

    return pack


def dealer_draw_card():
    card = deck.pop(0)
    tkinter.Label(dealer_frame, image=card[1], relief="raised").pack(side="left")
    return card

def player_draw_card():
    card = deck.pop(0)
    tkinter.Label(player_frame, image=card[1], relief="raised").pack(side="left")
    return card


mainWindow = tkinter.Tk()
mainWindow.title("Black jack game")
mainWindow.geometry("640x480")

game_result = tkinter.StringVar(value="No one wins")
tkinter.Label(mainWindow, textvariable=game_result).grid(row=0, column=0, columnspan=3, sticky="ew")

card_frame = tkinter.Frame(mainWindow, background="green", relief="sunken")
card_frame.grid(row=1, column=0, rowspan=2, columnspan=3, sticky='ew')

tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
dealer_score = tkinter.IntVar(0)
tkinter.Label(card_frame, textvariable=dealer_score, background="green", fg="white").grid(row=1, column=0)

tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
player_score = tkinter.IntVar(0)
tkinter.Label(card_frame, textvariable=player_score, background="green", fg="white").grid(row=3, column=0)

dealer_frame = tkinter.Frame(card_frame, background="green", relief="sunken")
dealer_frame.grid(row=0, column=1, rowspan=2, sticky='ew')

player_frame = tkinter.Frame(card_frame, background="green", relief="sunken")
player_frame.grid(row=2, column=1, rowspan=2, sticky='ew')

action_frame = tkinter.Frame(mainWindow, background="black")
action_frame.grid(row=5, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(action_frame, text="Dealer", command=dealer_draw_card)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(action_frame, text="Player", command=player_draw_card)
player_button.grid(row=0, column=1)

pack = load_cards()

deck = list(pack)

cardFrame = tkinter.Frame(mainWindow, background="green")
cardFrame.grid(row=6, column=0, sticky="nsew", columnspan=3)

# for card in deck:
#     tkinter.Label(cardFrame, image=card[1], relief="raised").pack(side="left")

random.shuffle(deck)

mainWindow.mainloop()