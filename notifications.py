def yell(text):
    text = text.upper()
    number_of_char = len(text)
    result = text + "!" * number_of_char 
    print(result)

yell("You are doing great")
yell("Don't forget to ask for help")


