from token import excute

if __name__ == "__main__":
    print("Welcome to the toy compile! \nPlease, select modes: \n1. Type codes. \n2. Load a script. \n3. Exit.")
    mode = input("Enter the number of modes: ")
    print("Choose the {} mode".format(mode))
    while mode != "3":
        if mode == "1":
            scrips = []
            # print("Please, type codes you want to run: ")
            while True:
                code = input(">: ")
                # print(code)
                if code == "":
                    break
                if code == "ChangeMode":
                    mode = "4"
                    break
                if code == "Exit":
                    quit()
                scrips.append(code)
            if mode == "1" and scrips != []:
                excute(scrips)

        elif mode == "2":
            scrips = []
            filename = input(
                "Please, Enter the file name, please name sure the file under the scription folder ./scriptions/ : ").strip()
            if filename == "ChangeMode":
                mode = "4"
                continue
            if filename == "Exit":
                quit()
            if "." not in filename:
                print("Please, make sure a file as txt format")
                continue
            if filename.split(".")[-1] != "txt":
                print("Please, make sure a file as txt format")
                continue
            try:
                file = open("./scriptions/{}".format(filename), "r")
                for line in file.readlines():
                    if line != "":
                        scrips.append(line)
                file.close()
                excute(scrips)
            except FileNotFoundError as identifier:
                print("File does not exist!!")

        elif mode == "3":
            print("Exit the program, thank you try me. \n Exit ...")
            quit()

        else:
            print(
                "Mode was wrong! \nPlease, select modes: \n1. Type codes. \n2. Load a script. \n3. Exit.")
            mode = input("Enter the number of modes: ")

    # for line in scrips:
    #     excute(line)

    print("Exit ...")
    quit()
