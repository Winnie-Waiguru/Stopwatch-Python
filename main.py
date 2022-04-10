import os, time

start= input("Press Enter to start timer:  ")        
print("The timer has started.")
hours= minutes =seconds= 0
while True:
    
    print(f"{hours:0>2}:{minutes:0>2}:{seconds:0>2}")
    time.sleep(1)
    seconds+=1
    if seconds==60:
        seconds=0
        minutes+=1
        
    if minutes==60:
        minutes=0
        hours+=1
    
    

        