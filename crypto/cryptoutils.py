"""
This file is part of crypto, a collection of tools useful in cryptography.

Copyright (C) 2017 Emilis Rupeika

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 2 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Contact: emilis.rupeika@gmail.com
"""

from binascii import b2a_base64

def hex_to_base64(input_str):
    """
    Takes an even-length hex-encoded data string, decodes it into bytes,
    and returns those bytes encoded in bas64.

    Since two hex chars make up one byte, and we are operating on
    bytes (not bits) to make the conversion, our input length has to be even.

    Args:
        input_str (str): Hex-encoded data string, even length.

    Returns:
        str: Input data encoded in Base64
    """
    input_bytes = bytes.fromhex(input_str)
    base64_bytes = b2a_base64(input_bytes, newline=False)

    return base64_bytes.decode('ascii')

def hex_xor(str1, str2):
    """
    Takes two hex-encoded strings, XOR's them and returns the result, encoded
    in hex.

    If the input lengths are not equal, the function will loop over str2
    input string (while XOR'ing against str1) until it reaches the end of the
    first input string str1.

    Args:
        str1 (str): The first hex-encoded data string to be XOR'ed
        str2 (str): The second hex-encoded data string to be XOR'ed

    Returns:
        str: Hex-encoded XOR result between the two input strings, same length
                as input str1.
    """

    res = ""
    for i in range(len(str1)):
        str2_index = i % len(str2)
        res += hex(int(str1[i], 16) ^ int(str2[str2_index], 16))[2:]
    return res

if __name__ == '__main__':
    pass
