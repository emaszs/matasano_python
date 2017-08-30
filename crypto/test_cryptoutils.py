import unittest

from .cryptoutils import hex_to_base64

class TestHexOperations(unittest.TestCase):
    def test_hex_to_b64_encoding(self):
        input_str = 'adad'
        output_expected_str = 'ra0='
        output_str =hex_to_base64(input_str)
        self.assertEqual(output_str, output_expected_str)

        input_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206'\
                    '120706f69736f6e6f7573206d757368726f6f6d'
        output_expected_str = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29'\
                              'ub3VzIG11c2hyb29t'
        output_str = hex_to_base64(input_str)
        self.assertEqual(output_str, output_expected_str)
