"""
The given program asks the user what time it is
and prints the times for the next three buses, based of the entered time.
"""
def main():
    """
    stores bus schedule in the structure and prints the times for next three
    buses according to the time entered
    """
    schedule1=[630,1015,1415,1620,1720,2000]
    ask=int(input("Enter the time (as an integer): "))
    if ask<schedule1[0] or ask>schedule1[5]:
        print("The next buses leave: ")
        schedule11=[630,1015,1415]
        for i in schedule11:
            print(i)
    elif ask>=schedule1[0] and ask<=schedule1[1]:
        print("The next buses leave: ")
        schedule12 = [1015, 1415, 1620]
        for i in schedule12:
            print(i)
    elif ask>schedule1[1] and ask<=schedule1[2]:
        print("The next buses leave: ")
        schedule13 = [1415, 1620, 1720]
        for i in schedule13:
            print(i)
    elif ask>schedule1[2] and ask<=schedule1[3]:
        print("The next buses leave: ")
        schedule14 = [1620, 1720, 2000]
        for i in schedule14:
            print(i)
    elif ask>schedule1[3] and ask<=schedule1[4]:
        print("The next buses leave: ")
        schedule14 = [1720, 2000, 630]
        for i in schedule14:
            print(i)
    else:
        print("The next buses leave: ")
        schedule14 = [2000,630,1015]
        for i in schedule14:
            print(i)

if __name__ == "__main__":
    main()