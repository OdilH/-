import struct


def parse_binary_data(data):
    signature = b'WSMV\xc5'
    if not data.startswith(signature):
        raise ValueError('Invalid data signature')

    offset = len(signature)
    result = {}

    # Parse structure A
    a1, a2, a3_0, a3_1, a3_2, a4, a5_1, a5_2, a5_3 = struct.unpack_from('<bHHHHHIdd', data, offset)
    result['A1'] = a1
    offset += struct.calcsize('<bHHHHHIdd')

    # Parse structure B
    b1, b2, b3, b4_size, b4_offset, b5 = struct.unpack_from('<HQBBHi', data, a2)
    result['A2'] = {
        'B1': b1,
        'B2': b2,
        'B3': b3,
        'B4': data[b4_offset:b4_offset + b4_size].decode(),
        'B5': b5
    }

    # Parse structures C
    result['A3'] = []
    for c_offset in [a3_0, a3_1, a3_2]:
        c1, c2, c3, c4, c5, c6 = struct.unpack_from('<dhiIHI', data, c_offset)

        # Parse structure D
        d1, d2_0, d2_1, d2_2 = struct.unpack_from('<BIII', data, c6)
        result['A3'].append({
            'C1': c1,
            'C2': c2,
            'C3': c3,
            'C4': c4,
            'C5': c5,
            'C6': {
                'D1': d1,
                'D2': [d2_0, d2_1, d2_2]
            }
        })

    # Parse structure E
    e1, e2, e3_0, e3_1, e3_2, e4, e5, e6 = struct.unpack_from('<bfbBBHIQb', data, a4)
    result['A4'] = {
        'E1': e1,
        'E2': e2,
        'E3': [e3_0, e3_1, e3_2],
        'E4': e4,
        'E5': e5,
        'E6': e6
    }

    # Structure F is already parsed during structure A parsing
    result['A5'] = {
        'F1': a5_1,
        'F2': a5_2,
        'F3': a5_3
    }

    return result

x = (
    b'WSMV\xc5\xe9$\x00F\x00k\x00\x90\x00\xa8\x00\x00\x00\xf7\x95\xe6:\x92-' b"\x90\x8cS\r\xec\xbf\xf4']>ze\xe8\x84\x01\x97y\x12\xcds\xdaAR\x02"  b'\x00\x00\x00"\x00\x82\x9f{U\xae2k\xad\xf2\x0f\xfb*\xf8\xee\xec\xa4x\xb2\xd0'b'\xb6\x7f\x9b\x11\xe8\xbf\xc8\x0bUQ\x0c\x1e\xe6\xb2\xd2@CF9\x00\x00\x001C'  b')\xfd\xf6$\x84,\x87\xa7\x161\x8f \x1f<\x10\x89%\xa7?LXG.+\xf9\x1b\xee\x85'  b'\xbd\xc0*^\x00\x00\x009wQ\xcd\x05\xdc%\x9d\xb9S\x91%\xff\xd0O\xceW'  b'\xb6d\xe3\xbf\xf7\xb8i\xdc\x02y\x95ELEuo\x83\x00\x00\x00\xe7\xb6s\x06' b'?\xb3\xd0\t\xb2K\xd6\xebTQ9\xf0\x9d\xc0\x13')
print(parse_binary_data(x))