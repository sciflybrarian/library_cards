import sys
import xlsxwriter as xl
import datetime as dt

def getnum(prompt):
    '''
    Collects integer from user. Reprompts if input is invalid.
    Exits program if user enters no input.
    prompt = string value shown to user
    '''
    result = ""
    while not result.isnumeric():
        result = input(prompt)
        if result == "":
            sys.exit()
        if not result.isnumeric():
            print("Please enter numbers only.")
    return int(result)

def addcheckdig(num):
    '''
    Takes lib card number as integer, check digit omitted.
    Adds checksum digit using the Luhn algorithm.
    Returns card number as string with check digit added.
    '''
    num = str(num)
    #create list with integer for each digit in number
    diglist = [int(x) for x in num]
    #calculate check digit
    for i in range(len(diglist) - 1, -1, -2):
        diglist[i] *= 2
        if diglist[i] > 9:
            diglist[i] -= 9
    checkdig = (sum(diglist) * 9) % 10
    return(num + str(checkdig))

# User display
print()
print("LIBRARY CARD GENERATOR\n")
print("Please enter desired numbers.")
print("Leave blank to exit program.\n")

# User input
n = getnum("Generate how many cards? ")
last_card = int(getnum("Last card number: ") / 10) # Drops checksum digit

# Generate card numbers
cards = [addcheckdig(num) for num in range(last_card + 1, last_card + n + 1)]

# Export to spreadsheet
filepath = 'Library cards {}.xlsx'.format(dt.date.today())
with xl.Workbook(filepath) as workbook:
    worksheet = workbook.add_worksheet()
    for row, card in enumerate(cards):
        worksheet.write(row, 0, card)

# Display summary of results
print()
# Display card numbers, max 10
card_preview = cards if n <= 10 else cards[:5] + ['. . .'] + cards[-5:]
for line in card_preview:
    print(line)
print()
print('Generated {} library cards'.format(n))
print('Card numbers saved to "{}"'.format(filepath))
print()
