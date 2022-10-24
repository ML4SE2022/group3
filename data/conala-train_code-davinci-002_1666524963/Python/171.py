def commas(N):
    digits = str(N)
    assert(digits.isdigit())
    result = ''
    while digits:
        digits, last3 = digits[:-3], digits[-3:]
        result = (last3 + ',' + result) if result else last3
    return result

if __name__ == '__main__':
    print commas(1)
    print commas(12)
    print commas(123)
    print commas(1234)
    print commas(12345)
    print commas(123456)
    print commas(1234567)
    print commas(12345678)
    print commas(123456789)
    print commas(1234567890)
    print commas(12345678901)
    print commas(123456789012)
    print commas(1234567890123)
    print commas(12345678901234)
    print commas(123456789012345)
    print commas(1234567890123456)
    print commas(12345678901234567)
    print commas(123456789012345678)
    print commas(1234567890123456789)
    print commas(12345678901234567890)
    print commas(123456789012345678901)
    print commas(1234567890123456789012)
    print commas(12345678901234567890123)
    print commas(123456789012345678901234)
    print commas(1234567890123456789012345)
    print commas(12345678901234567890123456)
    print commas(123456789012345678901234567)
    print commas(1234567890123456789012345678)
    print commas(12345678901234567890123456789)
    print commas(123456789