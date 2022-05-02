

def main():
    playerX = get_names('X')
    playerO = get_names('O')
    
    print(playerX)
    print(playerO)   
    
    
def get_names(number):
    name = input(f"Player {number} name: ")
    return name
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    main()