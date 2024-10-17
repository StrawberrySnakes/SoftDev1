import candy_land_card
def create_board():
    board = ["Start"]
    for position in range(1, 134):
        if position == 9:
            board.append("CC")
        elif position == 20:
            board.append("IC")
        elif position == 42:
            board.append("JJ")
        elif position == 69:
            board.append("GP")
        elif position == 92:
            board.append("LL")
        elif position == 102:
            board.append("PS")
        elif position == 117:
            board.append("BB")
        elif position == 133:
            board.append("MC")
        elif position == 4:
            board.append("BS60")
        elif position == 29:
            board.append("BS41")
        elif position == 45 or position == 76:
            board.append("GL")
        else:
            colors = ["R", "P", "Y", "B", "O", "G"]
            color_index = (position - 1) % len(colors)
            board.append(colors[color_index])

    return board
#player tuple=(color, current loc)
def move_player(player, card, board):
    current = player[1]
    
    if card[2] == 'SD':
        target_color = card[2:]
        if card[1] == 'D':
            player = (player[0], player[1] + 2)
    else:
        target_color = card[1:]

    while current < len(board):
        space = board[current]
        if space[:len(target_color)] == target_color:
            return (player[0], current)
        current += 1

    return player[1]
    

def take_turns(player, board, deck):
    card = candy_land_card.draw(deck)
    text = card[0]
    player_color = player[0]
    
    print("Player " ,player_color," drew a ",text,"." ,end="")
    
    if card[0] == 'S':
        print("Player",player_color,"took a shortcut!")
    
    new_position = move_player(player, card, board)
    
    return new_position

def play_game(num_players):
    player_colors = ["Red", "Yellow", "Blue", "Green"][:num_players]
    players = [(color, 0) for color in player_colors]
    deck = candy_land_card.make_deck()
    board = create_board()
    candy_land_card.suffle(deck)
    while True:
        for player in players:
            final = take_turns(player, board, deck)
            print("Player ",player[0]," landed on ",board[final - 1], final)
            
            if board[final - 1] == "MC":
                print("Player " ,player[0], " wins!")
                return
            
            if board[final - 1] == "GL":
                print("Player ",player[0], " lost a turn.")
            
            # Check if the deck is empty and shuffle a new one
            if len(deck) == 0:
                deck = candy_land_card.make_deck()
                candy_land_card.suffle(deck)


def main():
    players = int(input("How many players will play candyland: "))
    play_game(players)

if __name__ == "__main__":
    main()