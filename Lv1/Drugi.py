try:
    try:
        x= float(input('Unesi broj od 0 do 1:'))
    except:
        raise Exception("Number is not given")
    if x < 0 or x > 1:
        raise Exception("Number is out of boundry")

    if x >= 0.9 :
        print("A")
    elif x >= 0.8:
        print("B")
    elif x >= 0.7:
        print("C")
    elif x >= 0.6:
        print("D")
    else: print("F")


except Exception as e:
    print(e)