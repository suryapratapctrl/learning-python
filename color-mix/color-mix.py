#this is what i did 
color1 = input("enter the first color  ")
color2 = input("enter the second color  ")

if (color1 == "red" or color2 == "red") and (color2 =="yellow" or color1 == "yellow"):
    print("orange")
elif (color1 =="red"or color2=="red") and (color2 =="blue"or color1=="blue"):
    print("purple")
elif (color1 =="yellow"or color2=="yellow") and(color1 =="blue"or color2=="blue"):
    print("green")   
else:
    print("enter only red yellow blue")

#this is what erik did
# 🧑‍🎨Let's Mix Up Some Colors! 🎨🖌️
#🙋‍♂️ User Input
# color1 = input('Enter First Color (red, blue, yellow): ').lower()
# color2 = input('Enter Second Color (red, blue, yellow): ').lower()
# colors = [color1, color2]

# print('-'*50)
# print(f"🥼 Let's Mix {color1} + {color2}\n")

# #🎨 Calculate New Color
# if color1 == color2:
#     emoji = None
#     if color1 == 'red':
#         emoji = '❤️'
#     elif color1 == 'blue':
#         emoji = '💙'
#     elif color1 == 'yellow':
#         emoji = '💛'

#     print("🎨 You're mixing the same color!")
#     print(f'🧪{color1} + 🧪{color2} = {color1} {emoji}.')

# elif 'red' in colors and 'blue' in colors:
#     print(f'🧪{color1} + 🧪{color2} = Purple 💜.')

# elif 'red' in colors and 'yellow' in colors:
#     print(f'🧪{color1} + 🧪{color2} = Orange 🧡.')

# elif 'blue' in colors and 'yellow' in colors:
#     print(f'🧪{color1} + 🧪{color2} = Green 💚.')

# else:
#     print('❌ Invalid Color Combination. \nPlease use Red, Blue or Yellow.')