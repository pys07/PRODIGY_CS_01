# Caesar Cipher Implementation in Python

print("Welcome to the Caesar Cipher Program!")
# Define the message
msgstr = input("Enter your message: ")

# Key used to shift characters
try:
    keycode = int(input("Enter the shift key (integer): "))
except ValueError:
    print("That's not an integer! Please enter a valid integer for the key.")
    exit()

# Set it to encrypt or decrypt
modetype = input("Encrypt or Decrypt? (e/d): ").strip().lower()
if modetype == 'e':
    modetype = 'encrypt'
elif modetype == 'd':
    modetype = 'decrypt'
else:
    print("Invalid mode selected. Choose 'e' or 'd'")
    exit()

# constant set of allowed symbols (case sensitive)
SYMBOLSTYPE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !?.;,'

# ENCRYPTED/DECRYPTED STRING
translatedstr = ''

# loop through every symbol in the message
for sym in msgstr:
    if sym in SYMBOLSTYPE:
        symindex = SYMBOLSTYPE.find(sym)  # find() -> retrieves index of sym from SYMBOLSTYPE [case sensitive| first instance]

        if modetype == 'encrypt':
            translatedidx = symindex + keycode

        elif modetype == 'decrypt':
            translatedidx = symindex - keycode

        # handle wrap-around if index goes beyond SYMBOLSTYPE range
        if translatedidx >= len(SYMBOLSTYPE):
            translatedidx = translatedidx - len(SYMBOLSTYPE)
        elif translatedidx < 0:
            translatedidx = translatedidx + len(SYMBOLSTYPE)

        translatedstr += SYMBOLSTYPE[translatedidx]  # add the shifted symbol to final string

    else:
        translatedstr += sym  # if symbol not in SYMBOLSTYPE, leave it unchanged

# print final output
print(f"\nResult ({modetype}ed message):\n{translatedstr}")


