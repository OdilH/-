from struct import *

FMT = dict(
    char='c',
    int8='b',
    uint8='B',
    int16='h',
    uint16='H',
    int32='i',
    uint32='I',
    int64='q',
    uint64='Q',
    float='f',
    double='d'
)


def parse(buf, offs, ty, order='>'):
    print(buf)
    pattern = FMT[ty]
    size = calcsize(pattern)
    value = unpack_from(order + pattern, buf, offs)[0]
    return value, offs + size


def parse_e(buf, offs):
    e1, offs = parse(buf, offs, 'uint8')
    e2_size, offs = parse(buf, offs, 'uint32')
    e2_offs, offs = parse(buf, offs, 'uint16')
    e2 = []
    for _ in range(e2_size):
        val, e2_offs = parse(buf, e2_offs, 'int8')
        e2.append(val)
    e3, offs = parse(buf, offs, 'uint32')
    e4, offs = parse(buf, offs, 'uint8')
    e5, offs = parse(buf, offs, 'uint8')
    e6, offs = parse(buf, offs, 'int64')
    e7, offs = parse(buf, offs, 'int32')
    e8, offs = parse(buf, offs, 'uint64')
    return dict(E1=e1, E2=e2, E3=e3, E4=e4, E5=e5, E6=e6, E7=e7, E8=e8), offs


def parse_d(buf, offs):
    d1, offs = parse(buf, offs, 'float')
    d2, offs = parse(buf, offs, 'uint16')
    return dict(D1=d1, D2=d2), offs


def parse_c(buf, offs):
    c1, offs = parse(buf, offs, 'int8')
    c2, offs = parse(buf, offs, 'uint32')
    c3 = []
    for _ in range(5):
        val, offs = parse(buf, offs, 'char')
        c3.append(val)
    c3 = b''.join(c3).decode('utf-8')
    c4, offs = parse(buf, offs, 'double')
    c5, offs = parse(buf, offs, 'int16')
    return dict(C1=c1, C2=c2, C3=c3, C4=c4, C5=c5), offs


def parse_b(buf, offs):
    c_offset, offs = parse(buf, offs, 'uint16')
    b1, _ = parse_c(buf, c_offset)
    b2, offs = parse(buf, offs, 'int32')
    b3 = []
    for _ in range(3):
        d_offs, offs = parse(buf, offs, 'uint16')
        val, _ = parse_d(buf, d_offs)
        b3.append(val)
    b4_size, offs = parse(buf, offs, 'uint32')
    b4_offset, offs = parse(buf, offs, 'uint16')
    b4 = []
    for _ in range(b4_size):
        val, b4_offset = parse(buf, b4_offset, 'uint16')
        b4.append(val)
    b5, offs = parse(buf, offs, 'double')
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5), offs


def parse_a(buf, offs):
    a1, offs = parse(buf, offs, 'int8')
    a2, offs = parse_b(buf, offs)
    a3 = []
    for _ in range(7):
        val, offs = parse(buf, offs, 'uint8')
        a3.append(val)
    a4, offs = parse(buf, offs, 'float')
    a5, offs = parse(buf, offs, 'float')
    a6, offs = parse(buf, offs, 'int16')
    a7, offs = parse(buf, offs, 'uint64')
    a8, offs = parse_e(buf, offs)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7, A8=a8), offs


def main(stream):
    return parse_a(stream, 4)[0]


s = (b'VWOD\x08\x00Y\x06\\\x08\x10\x00m\x00s\x00y\x00\x00\x00\x04\x00\x7f\xbf'
     b'\xe6\xcd\xb7AF\xbeLrEt \x01@3?E\xa2p>\xc8=\x04\x02P#$\xb8\x06w\xdbh\x87'
     b"O\x00\x00\x00\x04\x00\x87#\xc2\x82=\xb1\xab'L\xd9I\xda\xc9^F\t{\xe1"
     b'\x82\x01]D\x12#\x82\xb1t\xd9\xd3\x7fm\x15mlare\xbf\xe9\xa8\x1a\xb9\xc8/l\xbf'
     b'\xdd\xbf\x18\xf4\xe3\xef\x83\xbf*\xcda.>?O^\xdb%\xdb\x914w\xdeo'
     b'\xe6\x1a\x16\xd4\xe3\xfbq')
print(main(s))
