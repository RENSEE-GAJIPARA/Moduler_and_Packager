import random, uuid, math, datetime, time
import geometric_shaps as gs

def current_time():
    """Display the current date and time."""
    
    now = datetime.datetime.now()
    print(f"Current Date & Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

def difference():
    """Calculate the difference between two user-input dates."""
    
    print("Enter first date:")
    y1 = int(input("Year: "))
    m1 = int(input("Mounth: "))
    d1 = int(input("Day: "))
    d1 = datetime.datetime(y1,m1,d1)

    print("Enter second date:")
    y2 = int(input("Year: "))
    m2 = int(input("Mounth: "))
    d2 = int(input("Day: "))
    d2 = datetime.datetime(y2,m2,d2)

    if d2 > d1 :
        gap = d2 - d1
        print(f"Difference between two given dates: {gap}")
    else:
        gap = d1 - d2
        print(f"Difference between two given dates: {gap}")
        
def format_date():
    """Format today's date into a custom DD-MM-YYYY format."""
    
    now = datetime.datetime.now()
    formated = datetime.datetime.strftime(now, "%d-%m-%Y")
    print(f"Formated date: {formated}")

def stopwatch():
    """A simple stopwatch with start, stop/pause, reset, and quit options."""
    
    running = False
    start_time = 0
    elapsed = 0

    print("\n--------- Stop Watch ---------")
    while True:
        print("1. Start | 2. Stop/Pause | 3. Reset | 4. Quit")
        command = int(input("\nEnter command: "))

        match command:
            case 1:
                if not running:
                    start_time = time.time() - elapsed
                    running = True
                    print("Stopwatch started...")
                    print("Press ctrl + C to interrupt.")

                    try:
                        while running:
                            elapsed = time.time() - start_time
                            hours = int(elapsed // 3600)
                            minutes = int((elapsed % 3600) // 60)
                            seconds = int(elapsed % 60)

                            print(f"\r{hours:02}:{minutes:02}:{seconds:02}", end="", flush=True)
                            time.sleep(0.01)
                        
                    except KeyboardInterrupt:
                        running = False
                        print("\nStopwatch Interrupted")
                else:
                    print("Already running!") 
            
            case 2:
                if running:
                    running = False
                    elapsed = time.time() - start_time
                    hours = int(elapsed // 3600)
                    minutes = int((elapsed % 3600) // 60)
                    seconds = int(elapsed % 60)
                    print(f"\nPaused at: {hours:02}:{minutes:02}:{seconds:02}")
                else:
                    print("Stopwatch is not running.")

            case 3:
                running = False
                elapsed = 0
                start_time = 0
                print("Reset! Time: 00:00:00")

            case 4:
                print("Exiting stopwatch.")
                break

            case _:
                print("Invalid command.")
                
def countdown():
    """Countdown from a user-specified number of seconds."""
    
    seconds = int(input("Enter number of seconds to countdown: "))

    for i in range(seconds, 0, -1):
        print(f"Time remaining: {i} seconds", end="\r")
        time.sleep(1)

    print("\nTime is up!")

def fact():
    """Calculate the factorial of a number."""
    
    n = int(input("Enter Number you want factorial of: "))
    fact = 1
    if n <= 0 or n == 1:
        return 1
    else:
        for i in range(1, n+1):
            fact *= i
        print(f"Factorial of given number: {fact}")
        
def compound():
    """Calculate compound interest."""
    
    p = float(input("Enter your Principal amount: "))
    r = float(input("Enter Interest Rate %: "))
    t = int(input("Enter Time (years): "))
    
    for i in range(t):
        p += p * r / 100
    print(f"Compound Interest: {p}")
    
def trigonometric():
    """Calculate sin, cos, tan for a given angle."""
    
    angle = float(input("Enter angle in degrees: "))
    rad = math.radians(angle)

    print("Sin:", math.sin(rad))
    print("Cos:", math.cos(rad))
    print("Tan:", math.tan(rad))
    
def Shapes():
    """Calculate area of a selected geometric shape using the custom package."""
    
    print("Select shape: ")
    print("1.Circle \n2.Rectangle \n3.Triangle")
                        
    op = int(input("Enter Your choice: "))
                        
    match op:
        case 1:
            r = float(input("Enter radius of circle: "))
            gs.circle.c_area(r)
                                
        case 2:
            l = float(input("Enter length of the rectangle: "))
            w = float(input("Enter width of the rectangle: "))
            gs.rectangle.r_area(l, w)
                                
        case 3:
            b = float(input("Enter Base of triangle: "))
            h = float(input("Enter Height of the triangle: "))
            gs.triangle.t_area(b, h)
                                
        case _:
            print("Invalid Input!!")
            
def password():
    """Generate a random password of user-specified length."""
    
    l = int(input("Enter Length of the password: "))
    
    letter = "abcdefghijklmnopqrstuvwxyz"
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digit = "0123456789"
    symbol = "#@$!_%"
    
    all_char  = letter + char + digit + symbol
    Password = ""
    for _ in range(l):
        Password += random.choice(all_char)
        
    print(f"\nGenerated Password: {Password}")
    
def otp():
    """Generate a 6-digit random OTP."""
    
    otp = random.randint(100000, 999999)
    print(f"\nGenerated OTP: {otp}")
    
def write_file():
    """Write multiple lines to an existing file."""
    
    filename = input("Enter file name to write to: ")
    n = int(input("How many lines do you want to write? "))
    
    with open(filename, "a") as f:
        for i in range(n):
            content = input(f"Enter line {i + 1}: ")
            f.write(f"Line {i + 1}: {content}\n")
            
    print("Data written successfully!")
    
def read_file():
    """Read and display the contents of a file."""
    
    filename = input("Enter file name to read: ")
    try:
        with open(filename, "r") as f:
            content = f.read()
        print(f"\nFile Content:\n{content}")
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        

def append_file():
    """Append text to the end of an existing file."""
    
    filename = input("Enter file name to append to: ")
    content = input("Enter Content to append: ")
    
    try:
        with open(filename, "a") as f:
            f.write(content + "\n")
        print("Content appended successfully!")
        
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        
if __name__ == "__main__":
    """MAIN MENU — only runs when this script is executed directly"""
    
    print('='*50)
    print("Welcomr to Multi-Utility ToolKit")
    print('='*50)


    while True:
        print("Choose an option: ")
        print("1.Datetime and Time Operation.")
        print("2.Mathematical Operation.")
        print("3.Random Data Generation.")
        print("4.Generate Unique Identifiers (UUID).")
        print("5.File operations (Custom Moduls).")
        print("6.Explore Module Attributes (dir()).")
        print("7.Exit.")
        print('='*50)
        
        choice = int(input("\nEnter your choice: "))
        
        match choice:
            case 1:
                while True:
                    print("\nDatetime and Time Operations:")
                    print("1.Display current date and time.")
                    print("2.Calculate difference between two dates/times.")
                    print("3.Formate date into custom format.")
                    print("4.Stopwatch.")
                    print("5.Coundown Timer.")
                    print("6.Back to main menu.")
                    print('='*50)
                    
                    option1 = int(input("\nEnter your option: "))
                    
                    match option1:
                        case 1:
                            current_time()
                            
                        case 2: 
                            difference()
                            
                        case 3:
                            format_date()
                            
                        case 4:
                            stopwatch()
                        
                        case 5:
                            countdown()
                                                
                        case 6:
                            print("Returned to main menu...")
                            break
                        
                        case _:
                            print("Invalid Input!!")
                            
            case 2:
                while True:
                    print("Mathematical Operations:")
                    print("1.Calculate Factorial.")
                    print("2.Solve Compound Interest.")
                    print("3.Trigonometric Calculations.")
                    print("4.Area of Geometric Shapes.")
                    print("5.Back to main menu.")
                    print('='*50)
                    
                    option2 = int(input("Enter your option: "))
                    
                    match option2:
                        case 1:
                            fact()
                            
                        case 2:
                            compound()
                            
                        case 3:
                            trigonometric()
                            
                        case 4:
                            Shapes()
                        
                        case 5:
                            print("Returned to main menu...")
                            break
                        
                        case _:
                            print("Invalid Input!!")
                            
            case 3:
                while True:
                    print("Random Data Generation:")
                    print("1.Generate Random Number.")
                    print("2.Generate random list.")
                    print("3.Create Random Password.")
                    print("4.generate Random OTP.")
                    print("5.Back to main menu.")
                    print('='*50)
                    
                    option3 = int(input("Enter your option: "))
                    
                    match option3:
                        case 1:
                            num = random.random()
                            print(f"\nRandomly Generated number: {num}")
                        
                        case 2:
                            gen = []
                            for i in range(10):
                                gen.append((random.randint(1, 100)))
                            print(f"\nRandom number list from 1 to 100: {gen}")
                            
                        case 3:
                            password()
                        
                        case 4:
                            otp()
                        
                        case 5:
                            print("Returned to main menu...")
                            break
                        
                        case _:
                            print("Invalid Input!!")
                            
            case 4:
                print("\nGenerate Unique Identifier:")
                uid = uuid.uuid4()
                print(f"\nGenerated Unique Id: {uid}")
                print('='*50)
            
            case 5:
                while True:
                    print("File Operations:")
                    print("1.Create a new file.")
                    print("2.Write to a file.")
                    print("3.Read from a file.")
                    print("4.Append to a file.")
                    print("5.Back to main menu.")
                    print('='*50)
                    
                    option4 = int(input("Enter your option: "))
                    
                    match option4:
                        case 1:
                            with open("First.txt", "w") as f:
                                f.write("New File Created...\n")
                            print("\nNew file created successfully...")
                        
                        case 2:
                            write_file()
                                    
                        case 3:
                            read_file()
                                
                        case 4:
                            append_file()
                        
                        case 5:
                            print("Returned to main menu...")
                            break
                        
                        case _:
                            print("Invalid Input!!")
                            
            case 6:
                print("\nExplore module attribute:")
                name = input("Enter module name to explore: ")
                print(f"\nAvailable Attributes in {name} module: \n{dir(name)}")
                print('='*50)
                
            case 7:
                print('='*50)
                print("Thank you for using the Multi-Utility ToolKit!")
                print('='*50)
                break
            
            case _:
                print("Invalid Input!!")