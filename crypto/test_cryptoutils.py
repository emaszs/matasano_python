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

import unittest

from .cryptoutils import hex_to_base64, hex_xor,\
    single_ascii_char_xor_bruteforce, hex_to_ascii, ascii_to_hex
from crypto.cryptoutils import get_english_score

class TestHexOperations(unittest.TestCase):
    def test_hex_to_b64_encoding(self):
        """
        Hex is encoded to Base64 with padding correctly.
        """
        input_str = 'adad'
        expected_output_str = 'ra0='
        self.assertEqual(hex_to_base64(input_str), expected_output_str)

        input_str = '3e3a43fe88a45e6199b3120706f69736f6e6f757120706f69736f6'\
                    'e6f7573e3a43fe88a45e6199b3120706'
        expected_output_str = 'PjpD/oikXmGZsxIHBvaXNvbm91cSBwb2lzb25vdXPjpD'\
                              '/oikXmGZsxIHBg=='
        self.assertEqual(hex_to_base64(input_str), expected_output_str)

        input_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206'\
                    '120706f69736f6e6f7573206d757368726f6f6d'
        expected_output_str = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29'\
                              'ub3VzIG11c2hyb29t'
        self.assertEqual(hex_to_base64(input_str), expected_output_str)

    def test_hex_xor(self):
        """
        Hex string XORED against variable length keys
        """
        input_str1 = 'adad'
        expected_output_str = '0000'
        self.assertEqual(hex_xor(input_str1, input_str1), expected_output_str)

        input_str1 = '1c0111001f010100061a024b53535009181c'
        input_str2 = '686974207468652062756c6c277320657965'
        expected_output_str = '746865206b696420646f6e277420706c6179'
        self.assertEqual(hex_xor(input_str1, input_str2), expected_output_str)

    def test_single_byte_xor_decipher(self):
        """
        The list of bruteforcing results contains the correctly deciphered
        entry.
        """

        input_str = '1b37373331363f78151b7f2b783431333d78397828372'\
                     'd363c78373e783a393b3736'
        expected_output_str = 'Cooking MC\'s like a pound of bacon'
        scores = single_ascii_char_xor_bruteforce(input_str)
        self.assertEqual(scores[6][0], expected_output_str)

    def test_hex_to_ascii(self):
        """
        Converting a Hex-encoded string to ASCII produces expected text.
        """
        input_str = '48656c6c6f'
        expected_output_str = 'Hello'
        self.assertEqual(hex_to_ascii(input_str), expected_output_str)

    def test_ascii_to_hex(self):
        """
        Converting ASCII text to hex produces the expected string.
        """
        input_str = 'Hello'
        expected_output_str = '48656c6c6f'
        self.assertEqual(ascii_to_hex(input_str), expected_output_str)

    def test_get_english_score(self):
        input_str = ''
        expected_score = 0
        self.assertEqual(get_english_score(input_str), expected_score)

        input_str1 = 'E'
        input_str2 = 'e'
        self.assertEqual(get_english_score(input_str1),
                         get_english_score(input_str2))
        expected_score = 12.702
        self.assertEqual(get_english_score(input_str1), expected_score)

        input_str = 'Cooking MC\'s like a pound of bacon'
        expected_score = 131.093
        self.assertEqual(get_english_score(input_str), 131.093)

    def test_decipher_single_byte_xor(self):
        input_str = '1b37373331363f78151b7f2b783431333d78397828372'\
                    'd363c78373e783a393b3736'
        scores = single_ascii_char_xor_bruteforce(input_str)
        expected_output_str = 'Cooking MC\'s like a pound of bacon'
        self.assertEqual(scores[6][0], expected_output_str)
