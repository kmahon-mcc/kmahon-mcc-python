"""
Write the program "99 Bottles of Beer on the Wall" using a while 
loop. Be mindful to change the word 'bottles' to 'bottle' when 
down to the last one. You must do the full 99 bottles; the sample 
shows the last 3 verses.
"""
bottle_count = 99
while bottle_count > 0:
    if bottle_count > 2:
        print(str(bottle_count), " bottles of beer on the wall,")
        print(str(bottle_count), " bottles of beer!\nTake one down, pass it around,")
        bottle_count -= 1
        print(str(bottle_count), " bottles of beer on the wall!\n")
    elif bottle_count == 2:
        print(str(bottle_count), " bottles of beer on the wall,")
        print(str(bottle_count), " bottles of beer!\nTake one down, pass it around,")
        bottle_count -= 1
        print("1 bottle of beer on the wall!\n")
    else:
        print("1 bottle of beer on the wall,\n1 bottle of beer!\nTake one down, pass it around,\nNo bottles of beer on the wall!")
        bottle_count -= 1