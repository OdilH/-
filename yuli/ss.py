import struct


def parse_struct_B(data, offset):
    B_format = "<HqBIHl"

    B_values = struct.unpack_from(B_format, data, offset)
    print(B_values[0])
    print(B_values[1])
    print(B_values[2])
    print(B_values[3])
    print(B_values[4])
    #print(data[offset + struct.calcsize(B_format): offset + struct.calcsize(B_format) + B_values[3]].decode())


    B = {
        "B1": B_values[0],
        "B2": B_values[1],
        "B3": B_values[2],
        "B4": data[3],
        "B5": B_values[4]
    }
    print(B)

    return B


def parse_struct_C(data, offset):
    C_format = "<dhiIH"
    C_values = struct.unpack_from(C_format, data, offset)
    C = {
        "C1": C_values[0],
        "C2": C_values[1],
        "C3": C_values[2],
        "C4": C_values[3],
        "C5": C_values[4],
        "C6": parse_struct_D(data, offset + struct.calcsize(C_format))
    }
    return C


def parse_struct_D(data, offset):
    D_format = "<B"
    D_values = struct.unpack_from(D_format, data, offset)
    D = {
        "D1": D_values[0],
        "D2": list(struct.unpack_from("<3I", data, offset + 1))
    }
    return D


def parse_struct_E(data, offset):
    E_format = "<bB3BHQ"
    E_values = struct.unpack_from(E_format, data, offset)
    E = {
        "E1": E_values[0],
        "E2": E_values[1],
        "E3": list(E_values[2:5]),
        "E4": E_values[5],
        "E5": E_values[6],
        "E6": E_values[7]
    }
    return E


def parse_struct_F(data, offset):
    F_format = "<Idf"
    F_values = struct.unpack_from(F_format, data, offset)
    F = {
        "F1": F_values[0],
        "F2": F_values[1],
        "F3": F_values[2]
    }
    return F


def main(data):
    signature = b"WSMV\xc5"
    if data[:5] != signature:
        raise ValueError("Invalid signature")

    A_format = "<bH"
    A_values = struct.unpack_from(A_format, data, 5)

    A = {
        "A1": A_values[0],
        "A2": parse_struct_B(data, A_values[1]),
        "A3": [parse_struct_C(data, struct.unpack_from("<H", data, 7 + i * 2)[0]) for i in range(3)],
        "A4": parse_struct_E(data, struct.unpack_from("<I", data, 13)[0]),
        "A5": parse_struct_F(data, 17)
    }
    return A


x = (b'WSMV\xc5\x86(\x00J\x00o\x00\x94\x00\xac\x00\x00\x00R\x8fQLX\x9e\x0b\xee\x9d,'
     b'\xe9\xbf\x0e(\x9c>nzxaknSUX7O\x01\xaf\xaa\xe4\x9a`\x06\x00\x00\x00"'
     b'\x00X\x8d\xcf\xf9\xf4\x91\x01\xd79L\x02:<\x14\x1eu\xdd\x02\xfd\xcd\x11\t\xc5'
     b'\xe3\xbfeY\xcbHS\x91\x89*\x0fj\xb9\xac=\x00\x00\x00`h!\x96\x01w\xb4}J\x8d'
     b'\x92\x1c\xa5\x80\xeeW\xff7\xa1\xa3\xbf\xb0d1\xa2\x01\xfa\xd2\xf8H'
     b'\xe7\xcb\x1ab\x00\x00\x00N\xc5\xf2\xcb:+\xa7\xef\x1cc\xa1\x02\x18@\xe5q\x83'
     b'\x11\xc4\xc1?\xe8\xd3A)b\x7fz\xe1\xcei\x01*\x87\x00\x00\x009\x96D\xab'
     b'\xbd$\x0bb\xbf1\xff\xd3\xfc\r\x11x\xa1D\xb7')
print(main(x))
