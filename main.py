print("hello")

print("enter your user name")

name = input()

print(f"hi {name} you are welcome to our page!")

print("how many days our you caculating")

def Days(day):
    HOU = 24
    MUN = (HOU*60)
    SEC = (MUN*60)

    print(f"we have {day*HOU} second in {day}")
    
Days(int(input()))