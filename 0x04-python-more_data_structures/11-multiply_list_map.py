#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}

    num = 0
    last_rom = 0

    for ch in roman_string:
        for r_num in rom_n.keys():
            if r_num == ch:
                if rom_n.get(ch) <= last_rom:
                    num += rom_n.get(ch)
                else:
                    num += rom_n.get(ch) - last_rom * 2

                last_rom = rom_n.get(ch)

    return (num)
