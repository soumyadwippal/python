num=input("Enter your  passworld:")
pro=str(num)
match pro:
    case pro if pro=="admin123":
        print("wlcome admin")
    # case user:
    #     print("wlcome user")
    case _:
        print("invalid passworld")
        