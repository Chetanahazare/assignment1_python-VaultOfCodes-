#code2

def get_age():
    age_str = input("Please enter your age: ")
    if age_str.isdigit() and int(age_str) >= 18:
        return int(age_str)
    else:
        return None

def main():
    age = get_age()
    if age is not None:
        print(f"You are {age} years old and eligible.")
    else:
        print("Invalid input. You must be at least 18 years old.")

if __name__ == "__main__":
    main()


#Explanation
#There are a couple of issues in given code. The input function returns a string, so when comparing age with an integer (18), you need to convert age to an integer first. Also, the isnumeric method checks if all characters in the string are numeric, but it doesn't handle negative numbers. It's better to use isdigit() instead.
