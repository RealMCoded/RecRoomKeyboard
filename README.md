# Rec Room CV2 Keyboard (Hexadecimal data transmitor using Rec Room HUD elements)

This is a keyboard that I designed to work in Rec Room that can interface with your real life computer. It works by converting the button pressed into [Hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal) data, which is read by a Python Script to convert it back into the ASCII character.

[Copyable Room with the Keyboard and CV2](https://rec.net/room/RecRoomKeyboard)

[Character to Hexadecimal Invention](https://rec.net/invention/3690354562335029960)

[Python Script](#python)

## Usage

You are free to use this project for whatever you want. However, it is under the [GPLv3 license](https://github.com/RealMCoded/RecRoomKeyboard/blob/main/LICENSE), so if you do make changes and use it in a commercial way, you must make your changes public.

Although not required, I would appreciate it if you credited me somehow. Some ways you can do this is by linking:

- This Repo (https://github.com/RealMCoded/RecRoomKeyboard)
- This video (https://youtu.be/6WDgR726RJk)
- My YouTube channel (https://youtube.com/@stuarttmcoded)
- My RecNet profilet (https://rec.net/user/stuartt)

## CV2 Schematics

> todo: improve these!

![buttons schema](https://raw.githubusercontent.com/RealMCoded/RecRoomKeyboard/main/schemas/schem_buttons.png)

![char2hex schema](https://raw.githubusercontent.com/RealMCoded/RecRoomKeyboard/main/schemas/schem_char2hex.png)

## Python

The source code for the Python script can be found [here](https://github.com/RealMCoded/RecRoomKeyboard/blob/main/RecRoomColorToHex.py)

The only requirements that you need to install are `pynput` and `pyautogui`.

You will need to adjust the `region` variable on line 51 to have the position of the room HUD element on your display. I used [Meazure](https://github.com/cthing/meazure/releases/tag/4.0.0) to get mine.