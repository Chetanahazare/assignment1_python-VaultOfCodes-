#code-1

def reverse_string(s):
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str

def main():
    input_string = "Hello, world!"
    reversed_string = reverse_string(input_string)
    print(f"Reversed string: {reversed_string}")

if __name__ == "__main__":
    main()

    #Explanation:
    #Given code appears to be mostly correct, but there's a small issue in the range function of the reverse_string function. The range function should include the start index (0) and exclude the end index (len(s)), so we should modify the range to be range(len(s) - 1, -1, -1)