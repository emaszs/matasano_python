"""
This file is part of crypto, a collection of tools useful in cryptography.

Copyright 2017 Emilis Rupeika <emilis.rupeika@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from crypto.cryptoutils import hex_to_base64, hex_xor,\
    single_ascii_char_xor_bruteforce

def set1_challenge1():
    input_str = '3e3a43fe88a45e6199b3120706f69736f6e6f757120706f69736f6'\
                'e6f7573e3a43fe88a45e6199b3120706'
    print(hex_to_base64(input_str))

def set1_challenge2():
    input_str1 = '1c0111001f010100061a024b53535009181c'
    input_str2 = '686974207468652062756c6c277320657965'
    print(hex_xor(input_str1, input_str2))

def set1_challenge3():
    input_text = '1b37373331363f78151b7f2b783431333d78397828372'\
                 'd363c78373e783a393b3736'
    scores = single_ascii_char_xor_bruteforce(input_text)
    print(scores[6])

def main():
    set1_challenge1()
    set1_challenge2()
    set1_challenge3()

if __name__ == '__main__':
    main()
