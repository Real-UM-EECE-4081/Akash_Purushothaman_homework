#8
def TowerOfHanoi(discs, pole1, pole2, pole3):
    
    if discs == 0:
        return
    
    else: 
        TowerOfHanoi(discs-1, pole1, pole3, pole2)
        print("Move disc", discs, "from pole", pole1, "to pole", pole2)
        TowerOfHanoi(discs-1, pole3, pole2, pole1)

 

discs = int(input("Enter amount of discs:"))
TowerOfHanoi(rings, '1', '3', '2')
