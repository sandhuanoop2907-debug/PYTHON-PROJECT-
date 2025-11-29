def check_palindrome(text):
    text = str(text).replace(" ", "").lower()
    rev = text[::-1]
    if text == rev:
        return True
    else:
        return False

def main():
    while True:
        print("\n------ PALINDROME VALIDATOR ------")
        print("1. Check a String")
        print("2. Check a Number")
        print("3. Exit")

        ch = input("Enter your choice: ")

        if ch == '1':
            s = input("Enter any string: ")
            if check_palindrome(s):
                print("Yes, it is a palindrome!")
            else:
                print("No, it is not a palindrome.")
        
        elif ch == '2':
            n = input("Enter any number: ")
            if check_palindrome(n):
                print("Yes, it is a palindrome number!")
            else:
                print("No, it is not a palindrome number.")
        
        elif ch == '3':
            print("Thank you for using the program.")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
