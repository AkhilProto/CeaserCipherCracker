def caesar(text):
    for i in range(26):
        result = ""
        for char in text:
            if char.isalpha():
                if char.isupper():
                    result += chr((ord(char) - 65 + i) % 26 + 65)
                else:
                    result += chr((ord(char) - 97 + i) % 26 + 97)
            else:
                result += char
        print("Shift pattern " + str(i) + ": " + result)
        print("")
        print("")
text = input("Enter the encrypted Ceaser Code: ")
caesar(text)
