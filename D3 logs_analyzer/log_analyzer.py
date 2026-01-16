with open("server.log", "r") as file:
    with open("error.txt", "a") as err_file:
        for log in file.readlines():
            if "ERROR" in log :
                err_file.write(log)
