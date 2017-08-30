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

import unittest

from .cryptoutils import hex_to_base64

class TestHexOperations(unittest.TestCase):
    def test_hex_to_b64_encoding(self):
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
