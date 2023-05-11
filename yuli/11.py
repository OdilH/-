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


def parse(buf, offs, ty, order='<'):
    pattern = FMT[ty]
    size = calcsize(pattern)
    value = unpack_from(order + pattern, buf, offs)[0]
    return value, offs + size


def parse_f(buf, offs):
    f1, offs = parse(buf, offs, 'uint32')
    f2, offs = parse(buf, offs, 'double')
    f3, offs = parse(buf, offs, 'float')
    return dict(F1=f1, F2=f2, F3=f3), offs


def parse_e(buf, offs):
    e1, offs = parse(buf, offs, 'int8')
    e2, offs = parse(buf, offs, 'float')
    e3 = []
    for _ in range(3):
        val, offs = parse(buf, offs, 'uint8')
        e3.append(val)
    e4, offs = parse(buf, offs, 'uint16')
    e5, offs = parse(buf, offs, 'uint64')
    e6, offs = parse(buf, offs, 'uint8')
    return dict(E1=e1, E2=e2, E3=e3, E4=e4, E5=e5, E6=e6), offs


def parse_d(buf, offs):
    d1, offs = parse(buf, offs, 'uint8')
    d2 = []
    for _ in range(3):
        val, offs = parse(buf, offs, 'uint32')
        d2.append(val)
    return dict(D1=d1, D2=d2), offs


def parse_c(buf, offs):
    c1, offs = parse(buf, offs, 'double')
    c2, offs = parse(buf, offs, 'int16')
    c3, offs = parse(buf, offs, 'int32')
    c4, offs = parse(buf, offs, 'uint16')
    c5, offs = parse(buf, offs, 'uint32')
    d_offset, offs = parse(buf, offs, 'uint32')
    c6, _ = parse_d(buf, d_offset)
    return dict(C1=c1, C2=c2, C3=c3, C4=c4, C5=c5, C6=c6), offs


def parse_b(buf, offs):
    b1, offs = parse(buf, offs, 'uint16')
    b2, offs = parse(buf, offs, 'int64')
    b3, offs = parse(buf, offs, 'uint8')
    b4_size, offs = parse(buf, offs, 'uint32')
    b4_offset, offs = parse(buf, offs, 'uint16')
    b4 = ""
    for _ in range(b4_size):
        val, b4_offset = parse(buf, b4_offset, 'char')
        b4 += val.decode()  # Decode the byte to a string and concatenate

    b5, offs = parse(buf, offs, 'int32')
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5), offs


def parse_a(buf, offs):
    a1, offs = parse(buf, offs, 'int8')

    b_offset, offs = parse(buf, offs, 'uint16')
    a2, _ = parse_b(buf, b_offset)

    a3 = []

    for _ in range(3):
        c_offs, offs = parse(buf, offs, 'uint16')
        val, _ = parse_c(buf, c_offs)
        a3.append(val)
    e_offset, offs = parse(buf, offs, 'uint32')

    a4, _ = parse_e(buf, e_offset)
    a5, offs = parse_f(buf, offs)

    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5), offs


def main(stream):
    return parse_a(stream, 5)[0]
