# Extra Input
A simple helper lib with a few extra ways to get input from the user

## How to use:
``` python
import extra_input

option = extra_input.selector(["Option [1]","Option [2]"])

print(f"you selected {option}")
```

## Functions:
 * `select(options:list[str], squareBrackets = True) -> str`
   Selects from a list of items, by defualt uses the items in the first square brackets of the list
 * `numbered_select(options:list[str], use_parens = False, roman_numerals = False) -> str`
   Selects from a list of items, selecting by using numbers not needed in the list
   Can use 1) or roman numerals
 * `intput(text:str) -> int`
   Gets input and only allows ints
 * `float_input(text:str) -> float`
   Gets input and only allows floats
 * `custom_input(text:str, allowed:str, tellAllowed = True) -> str`
   Gets input only allowing the charecters in allowed
 * `get_int_range(prompt: str, min_val, max_val, tell_range) -> int`
   Gets an int in a certain range
 * `get_float_range(prompt: str, min_val, max_val, tell_range) -> float`
   Gets a float in a certain range
 * `get_time(prompt: str, military_time = False) -> datetime.time`
   Gets a datetime time
 * `get_date(prompt: str, number_month = False, number_day = True) -> datetime.date`
   Gets a datetime date
 * `get_date_and_time(prompt: str, number_month = False, number_day = True, military_time = False) -> datetime.datetime`
   Gets a datetime datetime
 * `get_bool(prompt) -> bool`
   Gets a boolean value

## Ideas, Errors, or Helping
If you want to do any of the three please use the github linked below

## Github
You can see the github here: [extra-input github](https://github.com/lpow100/extra-input)

## Changelog:
 * 1.1.0:
    - Added range based functions
    - Added date and time functions
    - Made sure to update the changelog
    - Pretty sure I used correct grammar
 * 1.0.6:
    - Updated the readme
 * 1.0.5:
    - Fixed a bug where PyPI didn't show this whole readme
 * 1.0.4:
    - Fixed some misc bugs
    - Fixed selector using the wrong index
    - Fixed selector using its own charecter making it more error prone
 * 1.0.0 - 1.0.3:
    - Firguring out how to make this work