import datetime
import selectingInputs

def intput(prompt:str) -> int:
    """Gets input only allowing ints"""
    while True:
        response = input(prompt)
        try:
            return int(response)
        except ValueError:
            print("Please enter a valid int, try again.")
        except OverflowError:
            print("Please enter a smaller int, try again.")

def float_input(prompt:str) -> float:
    """Gets input only allowing floats"""
    while True:
        response = input(prompt)
        try:
            return float(response)
        except ValueError:
            print("Please enter a valid float, try again.")
        except OverflowError:
            print("Please enter a smaller float, try again.")

def custom_input(prompt:str, allowed:str, tellAllowed = True) -> str:
    """Gets input only allowing certain charecters"""
    while True:
        response = input(prompt)
        good = True
        for char in response:
            if char not in allowed:
                if tellAllowed:
                    print(f"Please enter prompt with only valid charecters:\n{allowed}")
                else:
                    print("Please enter prompt with only valid charecters.")
                good = False
                break
        if good:
            return response
        

def get_int_range(prompt: str, min_val, max_val, tell_range) -> int:
    """Gets inputs only allowing a range of ints"""
    while True:
        response = input(prompt)
        try:
            num = int(response)
            if num >= min_val and num <= max_val:
                return num
            else:
                print("Please enter an int in the range",end=", " if tell_range else "\n")
                if tell_range:
                    print(f"Min: {min_val}, Max: {max_val}")
        except ValueError:
            print("Please enter a valid int, try again.")
        except OverflowError:
            print("Please enter a smaller int, try again.")

def get_float_range(prompt: str, min_val, max_val, tell_range) -> float:
    """Gets inputs only allowing a range of float"""
    while True:
        response = input(prompt)
        try:
            num = float(response)
            if num >= min_val and num <= max_val:
                return num
            else:
                print("Please enter an float in the range",end=", " if tell_range else "\n")
                if tell_range:
                    print(f"Min: {min_val}, Max: {max_val}")
        except ValueError:
            print("Please enter a valid float, try again.")
        except OverflowError:
            print("Please enter a smaller float, try again.")

def get_time(prompt: str, military_time = False) -> datetime.time:
    curr = datetime.time(0,0,0)
    if prompt != "":
        print(prompt)
    #hour
    while True:
        response = input("Please enter the hour: ")
        try:
            hour = int(response)
            if hour >= 0 if military_time else 1 and hour <= 24 if military_time else 12:
                if selectingInputs.select(["[a]m","[p]m"]) == "pm":
                    hour = hour + 12
                curr.hour = hour
                break
            else:
                print("Please enter a valid year, try again")
        except ValueError:
            print("Please enter a valid year, try again.")
    #minute
    while True:
        response = input("Please enter the minute: ")
        try:
            minute = int(response)
            if minute >= 0 and minute <= 59:
                curr.minute = minute
                break
            else:
                print("Please enter a valid minute, try again")
        except ValueError:
            print("Please enter a valid minute, try again.")
    return curr

def get_date(prompt: str, number_month = False, number_day = True) -> datetime.date:
    curr = datetime.date(1,1,2001)
    if prompt != "":
        print(prompt)
    #year
    while True:
        response = input("Please enter the year: ")
        try:
            year = int(response)
            if year >= datetime.MINYEAR and year <= datetime.MAXYEAR:
                curr.year = year
                break
            else:
                print("Please enter a valid year, try again")
        except ValueError:
            print("Please enter a valid year, try again.")
    #month
    while True:
        response = input("Please enter the month: ")
        if number_month:
            try:
                month = int(response)
                if month >= 1 and month <= 12:
                    curr.month = month
                    break
                else:
                    print("Please enter a valid month, try again")
            except ValueError:
                print("Please enter a valid month, try again.")
        else:
            if response.lower() in ["january","febuary","march","april","may","june","july","august","september","october","november","december"]:
                curr.month = ["january","febuary","march","april","may","june","july","august","september","october","november","december"][response.lower()]
            elif response.lower() in ["jan","feb","mar","aug","sep","oct","nov","dec"]:
                curr.month = ["jan","feb","mar","april","may","june","july","aug","sep","oct","nov","dec"][response.lower()]
            else:
                print("Please enter a valid month's name, try again.")
    #day
    while True:
        response = input("Please enter the day: ")
        if number_day:
            try:
                day = int(response)
                if curr.month == 2:
                    month_len = 29 if (curr.year % 4 == 0 and curr.year % 100 != 0) or (curr.year % 400 == 0) else 28
                month_len = 30 if curr.month % 2 == 1 else 31
                if month_len >= 1 and month_len <= 12:
                    curr.day = day
                    break
                else:
                    print("Please enter a valid day, try again")
            except ValueError:
                print("Please enter a valid day, try again.")
        else:
            if response.lower() in ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]:
                curr.day = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"][response.lower()]
            elif response.lower() in ["mon","tues","weds","thurs","fri","sat","sun"]:
                curr.day = ["mon","tues","weds","thurs","fri","sat","sun"][response.lower()]
            else:
                print("Please enter a valid day's name, try again.")
    return curr

def get_date_and_time(prompt: str, number_month = False, number_day = True, military_time = False) -> datetime.datetime:
    curr = datetime.datetime(1,1,2001,0,0,0)
    if prompt != "":
        print(prompt)
    date = get_date("",number_month,number_day)
    time = get_time("",military_time)
    curr.year = date.year
    curr.month = date.month
    curr.day = date.day
    curr.hour = time.hour
    curr.minute = time.minute
    return curr

def get_bool(prompt) -> bool:
    """Gets a true or false"""
    while True:
        response = input(prompt)
        if response.lower() == "true":
            return True
        if response.lower() == "false":
            return False
        else:
            print("Please enter a valid bool, try again.")

# TODO:
#def get_list(prompt: str, separator, strip):
#    pass
#def get_path(prompt: str, must_exist, is_file, is_dir):
#    pass