'''
Created on Aug 30, 2017

@author: erupeika
'''

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

if __name__ == '__main__':
    pass
