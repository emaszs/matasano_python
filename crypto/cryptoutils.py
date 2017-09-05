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

import codecs

from binascii import b2a_base64, unhexlify


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

def ascii_chars():
    """
    Gets all of the 128 ASCII chars sequentially.

    Returns:
        list: 0-127 ASCII character list
    """
    res = []
    for i in range(128):
        res += chr(i)

    return res

def ascii_to_hex(ascii_str):
    """
    Return the Hex representation of ASCII-encoded input data.

    Args:
        ascii_str: ASCII-encoded input data.

    Returns:
        str: Hex-encoded input data.

    """

    bytes_input = bytes(ascii_str, 'ascii')
    return codecs.encode(bytes_input, 'hex').decode('ascii')

def hex_to_ascii(hex_str):
    """
    Return the ASCII representation of Hex-encoded input data.

    Args:
        hex_str: Hex-encoded data to be converted into ASCII, even length.

    Returns:
        str: ASCII-encoded input data.
    """

    return codecs.decode(hex_str, 'hex').decode('ascii')

def get_english_score(text):
    """
    Give a piece of text a score based on how likely it is to be English
    language.

    The score is calculated by taking predefined scores for some of the
    most common English alphabet letters (etaoinshrdlcumwf) and calculating the
    total sum score of the piece of text provided. The more 'English' characters
    the text has, the higher it's score will be.

    Less common letters (not part of the list 'etaoinshrdlcumwf') are ignored.
    Of course the rest of the letters can be added with their corresponding
    scores, but I don't feel like it, at least not until we're dealing with
    much bigger amounts of data.

    Args:
        text (str): Input text to evaluate.

    Returns:
        float: Text's English-likeness score, the higher the better.
    """

    english_char_score = {'E': 12.702, 'T': 9.056, 'A': 8.167, 'O': 7.507,
                          'I': 6.966, 'N': 6.749, 'S': 6.327, 'H': 6.094,
                          'R': 5.987, 'D': 4.253, 'L': 4.025, 'C': 2.782,
                          'U': 2.758, 'M': 2.406, 'W':2.360, 'F': 2.228}

    res = 0
    for char in text:
        res += english_char_score.get(char.upper(), 0)

    return res

def single_ascii_char_xor_bruteforce(text):
    """
    Bruteforce the decryption of input text with all of the 128 ASCII chars
    using the single byte xor method.

    The ASCII characters to try are provided by ascii_chars(). This function
    takes each of them and applies the hex_xor() decryption using the character
    as the key. In order to not have to go through all of the results manually,
    measuring success is done by get_english_score(). The results are returned
    as a list of tuples containing the XOR'ed text, the key that was used and
    the resulting score sorted from the best to the worst result.

    Args:
        text (str): ASCII data that is suspected to have been XOR'ed against a
        single ASCII char.

    Returns:
        list: A list of (xored_text, xor_key, english_score_with_the_key) tuples
            sorted by the score in descending order.
    """
    scores = []
    for char in ascii_chars():
        # Get the Hex value of the character so that it can be used in the Hex
        # XOR function.
        hex_char = ascii_to_hex(char)
        # XOR the data, convert the Hex information into bytes and finally,
        # decode the bytes as ASCII data.
        deciphered_text = unhexlify(hex_xor(text, hex_char)).decode('ascii')

        score = get_english_score(deciphered_text)
        scores.append((deciphered_text, hex_char, score))
    scores.sort(key=lambda tup: tup[2], reverse=True)

    return scores
