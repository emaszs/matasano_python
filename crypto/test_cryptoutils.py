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

from .cryptoutils import hex_to_base64, hex_xor, decipher_single_byte_xor

class TestHexOperations(unittest.TestCase):
    def test_hex_to_b64_encoding(self):
        """
        Hex is encoded to Base64 with padding correctly.
        """
        input_str = 'adad'
        output_expected_str = 'ra0='
        self.assertEqual(hex_to_base64(input_str), output_expected_str)

        input_str = '3e3a43fe88a45e6199b3120706f69736f6e6f757120706f69736f6'\
                    'e6f7573e3a43fe88a45e6199b3120706'
        output_expected_str = 'PjpD/oikXmGZsxIHBvaXNvbm91cSBwb2lzb25vdXPjpD'\
                              '/oikXmGZsxIHBg=='
        self.assertEqual(hex_to_base64(input_str), output_expected_str)

        input_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206'\
                    '120706f69736f6e6f7573206d757368726f6f6d'
        output_expected_str = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29'\
                              'ub3VzIG11c2hyb29t'
        self.assertEqual(hex_to_base64(input_str), output_expected_str)

    def test_hex_xor(self):
        """
        Hex string XORED against variable length keys
        """
        input_str1 = 'adad'
        output_expected_str = '0000'
        self.assertEqual(hex_xor(input_str1, input_str1), output_expected_str)

        input_str1 = '1c0111001f010100061a024b53535009181c'
        input_str2 = '686974207468652062756c6c277320657965'
        output_expected_str = '746865206b696420646f6e277420706c6179'
        self.assertEqual(hex_xor(input_str1, input_str2), output_expected_str)

    def test_single_byte_xor_decipher(self):

        input_text = '1b37373331363f78151b7f2b783431333d78397828372'\
                     'd363c78373e783a393b3736'
        decipher_single_byte_xor(input_text)

    def test_hex_to_ascii(self):
        pass

    def test_ascii_to_hex(self):
        pass

    def test_get_english_score(self):
        pass

    def test_decipher_single_byte_xor(self):
        pass

