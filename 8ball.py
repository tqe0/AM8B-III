import pyautogui
import keyboard as kb
import time as t
import random as r

# configs
spacetime = 0.25
enteringchat = '/'
exitchat = 'Return'
typespeed = 0.01
iconic_catchphrase = 'Shaking 8ball...'

# responses can be edited in txt files
response1 = []

with open("positiveresponses.txt", "r") as file:
    for line in file:
        response1.append(line.strip())

response2 = []

with open("negativeresponses.txt", "r") as file:
    for line in file:
        response2.append(line.strip())

response3 = []

with open("uncertainresponses.txt", "r") as file:
    for line in file:
        response3.append(line.strip())


def main():

    allresponses = r.choice([response1,response2,response3])
    chosenresponse = r.choice(allresponses)

    kb.press_and_release(enteringchat)
    t.sleep(spacetime)
    pyautogui.typewrite(iconic_catchphrase)
    t.sleep(spacetime)
    kb.press_and_release(exitchat)
    t.sleep(spacetime)
    kb.press_and_release(enteringchat)
    t.sleep(spacetime)
    pyautogui.typewrite((chosenresponse), interval=typespeed)
    t.sleep(spacetime)
    kb.press_and_release(exitchat)

if __name__ == '__main__':
    print("""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$@@@$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$@WbrxrfffjrrjrLMB@$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$@LvjffffjffjrJQ@@@@@$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$@BmczzzXXzzzzzcrjrjjL%@$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$@@$$$$%Qmqqq0XzzzzzzzzzzccvcvJ8$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$Mpbm#8LMMMMMMWMqXzzzzzzzzzzx@kvY@$$$$$$$$$$$$$$$$$$
$$$$$$$$@OkbkkZbWWWMMMMMMWoQzzzzzzzzzz*$8o$$$$$$$$$$$$$$$$$$
$$$$$$$@@dkkkkkbUuuvXaWWWMWWWqzzzzzzzzv>,`.$$$$$$$$$$$$$$$$$
$$$$$$$$@mkQkkkkkkkkkkpUUw*qxYwLzzzzzzzv>..f$$$$$$$$$$$$$$$$
$$$$$$$$$OkkZkkkkkkkkkkr!lir*[':~jnczzzzct`+$$$$$$$$$$$$$$$$
$$$$$$$$$#qkpwkqJf^.;(||\||\;|>.^`...I/jjj(jmQw%$$$$$$$$$$$$
$$$$$$$$$@abkd~......^l\||||!,:.-j ...`1\|)~bkbm@$$$$$$$$$$$
$$$$$$$$$$@(............<|||,...}kq:....:<~qwbkbM$$$$$$$$$$$
$$$$$$$$@UI....')x!.......~||1i.{bbkqwwjcqbkbkkb0$$$$$$$$$$$
$$$$$$@|.. -tYubbbk<....... (|+;bbbbZbbM0bkkkkkkka@$$$$$$$$$
$$$$$$$a...@0zXvYbkkq_.......?ObbbbmdbbB8qbkkkkkkk@$$$$$$$$$
$$$$$$$$$X0$bruXXzrwbkkkkbkkkkkkkkkkL@@$$@qkkkkkkpM@$$$$$$$$
$$$$$$$$$$$$@JrnzYXXXuxUmkkkkbkdmObB$$$$$$@wbkkkkbm@$$$$$$$$
$$$$$$$$$$$$$$xxxnXXvCbkkkkbbbdbkQ@$$$$$$$$@kbkkkkkO$$$$$$$$
$$$$$$$$$$$$$@OrxrrxzYuYbkkkkkkkkkL@$$$@@MZkbkkkkkpq$$$$$$$$
$$$$$$$$$$$$$$$fjrrrrrxcvdkkkkkkkkbh@@kbdkkkkkbkkwB$$$$$$$$$
$$$$$$$$$$$$$$$b(]jrrrrrrrqkkkkkkkkmpkkkkkkkkbqq@$$$$$$$$$$$
$$$$$$$$$$$$&q&aQ\]{rrxnrrvpkkkkkkbkQbkkkkk0bM$$$$$$$$$$$$$$
$$$$$$$$$$$@okbLpw|][trLUnr0kkkkkkkkbJZpB@@$$$$$$$$$$$$$$$$$
$$$$$$$$$@hwOqkd0bQ\]]/vQbCvbkkbbkkkkdb@$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$@mkdqkkk0kZ/]]nOCkJbkkbqkkkkkw8$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$8Zbkpkm0ZOJ(]uCQbbkkkbqdkkkkm&$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$@B0kb0pkkbkCnqkkpmbkkkpmkkkkd8$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$WwCkkkkkkCLkbkqObkkkkwmkkbq8$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$BJmkkkkkbbkkkO0bkkkkkqmkbmZQk@$$$$$$$$$$$$$$$$$
$$$$$$$$$$@@bpkbZOwwwwqmQbkpOkkkkkbZpbQZmmmh@$$$$$$$$$$$$$$$
$$$$$$$$$$@*pkkkkkkkbkkkkkkkUbkkkkkbQ0ZmmmmZo$$$$$$$$$$$$$$$
$$$$$$$$$$@Jbkkkkkkkkkkkkkkkk0kkkkkkkLmmmmmmwB$$$$$$$$$$$$$$
""") # u can remove this i just think it looks kewl
    while True:

        trigger = "A"
        triggerinpt = input(f"enter {trigger} ").upper()

        if triggerinpt == trigger:
            t.sleep(1)
            main()
        elif triggerinpt == "Q":
            break
        else:
            print(f"please enter {trigger}")
        