def multiply(x, y):
    def digit_count(z):
        return len(str(z))

    len_x = digit_count(x)
    len_y = digit_count(y)
    if len_x == 1 or len_y == 1:
        return x * y

    m = int(max(len_x, len_y))
    m_half = int(m / 2)
    a = x // 10 ** m_half
    b = x % 10 ** m_half
    c = y // 10 ** m_half
    d = y % 10 ** m_half

    ac = multiply(a, c)
    bd = multiply(b, d)
    ad_cd = multiply((a + b), (c + d))
    ad_plus_bc = ad_cd - ac - bd

    return (10 ** m) * ac + ((10 ** m_half) * ad_plus_bc) + bd
