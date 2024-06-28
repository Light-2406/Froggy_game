#This is a Frog leap game.... 
# Few Observations : 1) Cconsider 'G'- Green Frogs
#2) Consider 'B'- Brown Frogs
# 3) Consider '-'- Empty Stone


def display_game(pos):
    print("[0 , 1, 2, 3, 4, 5, 6]")
    print(pos)
def main():
    pos=['G', 'G', 'G', '-', 'B', 'B', 'B']
    while True:
        display_game(pos)
        move = input("Click 'q' to quit else \n Enter the position where frog should jump: ")
        
        if move== 'q':
            print("quitting the game....")
            break
        
        try:
            move=int(move)
        except ValueError:
            print("Not a valid Move")
            continue
        if move < 0 or move >6:
            print('Not a valid Move')
            continue
        if pos[move]=='-':
            print("Not a valid Move")
            continue
        
        post2 = 0
        if pos[move]== "G":
            if move + 1 <=6 and pos[move + 1] == '-':
                post2 = move+1
            elif move + 2<=6 and pos[move + 2] == '-' and pos[move + 1 ]== 'B':
                post2= move +2 
            else:
                print("Not a valid Move")
                continue
        elif pos[move]== 'B':
            if move -1 >=0 and pos[move - 1]=='-':
                post2=move -1
            elif move - 2 >=0 and pos[move - 2]=='-' and pos[move - 1]=='G':
                post2=move - 2
            else:
                print("Not a valid Move")
                continue
        pos[move],pos[post2]= pos[post2],pos[move]
        
        if pos ==  ['B', 'B', 'B', '-', 'G', 'G', 'G']:
            display_game(pos)
            print(" Hurray ! You placed them right")
            break
        valid_moves_exist = False
        for i in range(len(pos)):
            if pos[i] == 'G' and i + 1 <= 6 and pos[i + 1] == '-':
                valid_moves_exist = True
                break
            elif pos[i] == 'G' and i + 2 <= 6 and pos[i + 2] == '-' and pos[i + 1] == 'B':
                valid_moves_exist = True
                break
            elif pos[i] == 'B' and i - 1 >= 0 and pos[i - 1] == '-':
                valid_moves_exist = True
                break
            elif pos[i] == 'B' and i - 2 >= 0 and pos[i - 2] == '-' and pos[i - 1] == 'G':
                valid_moves_exist = True
                break

        if not valid_moves_exist:
            display_game(pos)
            print("You messed up no more valid moves ")
            break

if __name__ == "__main__":
    main()
    