def callInputNumeric(tupleEntries):
    count = 0
    for x in tupleEntries:
        count += 1
        print(f"{str(count)}) {x}")
    while True:
        try:
            response = int(input(("Please make your selection (Numeric): ")))
            if response > count or response <= 0:
                raise Exception
            break
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except:
            print("That is not a valid input!")
    return response
