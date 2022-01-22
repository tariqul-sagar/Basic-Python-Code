x = ""
while x.lower() != 'quit':
    x = input("""
    Start       Stop        Help: """).lower()
    if x == "start":
        print("     Car Started...")
        print("     Ready to go...")
    elif x == "stop":
        print("     Car Stopped.")
        break
    elif x == "help":
        print("""
        Start -> To start the car.
        Stop  -> To stop the car.
        Help  -> To know the function.
        """)
    else:
        print("Invalid Command.")