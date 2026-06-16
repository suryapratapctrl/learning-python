#this what i did
password=input("enter your password  ")
count=len(password)
if count<8:
  print("password too short") 
elif sum(il.islower() for il in password) < 1:
    print("there must be altleat one lower case alphabet")
elif sum(iu.isupper() for iu in password) < 1:
    print("there must be altleat one upper case alphabet")
elif sum(id.isdigit() for id in password) < 1:
    print("there must be altleat one number")
elif sum(not ispe.isalnum() for ispe in password) < 1:
    print("there must be altleat one special character")
else:
  print("your password is strong")

#this is what erik did 
def check_password(password):
    """Check the strength of your password.
    Checks:
    - Length (minimum 8 characters)
    - Contains at least one digit
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one special character
    - Contains no spaces

    Returns: True/False"""
    print('-'*50)
    print(f'Checking Password: {password}')

    #📦 Placeholders
    symbols      = '!@#$%^&*()_+-<>/{}|'
    check_length = False
    check_digit  = False
    check_lower  = False
    check_upper  = False
    check_symbol = False
    check_no_spaces = False

    # Security Checks
    # ✔️ Length (minimum 8 characters)
    if len(password) >= 8:
        check_length = True

    #✔️ Contains no spaces
    if ' ' not in password:
        check_no_spaces = True

    for char in password:
        #✔️ Contains at least one digit
        if char.isdigit():
            check_digit = True

        #✔️ Contains at least one uppercase letter
        elif char.isupper():
            check_upper = True

        #✔️ Contains at least one lowercase letter
        elif char.islower():
            check_lower = True

        #✔️ Contains at least one special character
        elif char in symbols:
            check_symbol = True

    # Display Results
    checks = [check_length,
                check_digit,
                check_lower,
                check_upper ,
                check_symbol,
                check_no_spaces ]

    if all(checks):
        print('✅ Account Created Successfully.')
        return True

    else:
        print('Password is not strong enough.')

        if not check_length:
            print('❌ - At least 8 characters')

        if not check_symbol:
            print(f'❌ - At least one symbol ({symbols})')

        if not check_digit:
            print('❌ - At least one digit.')

        if not check_upper:
            print('❌ - At least one uppercase letter.')

        if not check_lower:
            print('❌ - At least one lowercase letter.')

        if not check_no_spaces:
            print('❌ - Should not contain spaces.')

        return False

