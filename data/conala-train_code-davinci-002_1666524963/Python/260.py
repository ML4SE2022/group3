def split_string(string):
    """
    Split string into strings of repeating elements
    """
    result = []
    current = string[0]
    count = 0
    for char in string:
        if char == current:
            count += 1
        else:
            result.append(current * count)
            current = char
            count = 1
    result.append(current * count)
    return result

print(split_string('aabbccdd'))
print(split_string('aabbccdde'))
print(split_string('aabbccddee'))
print(split_string('aabbccddeeff'))
print(split_string('aabbccddeeffgg'))
print(split_string('aabbccddeeffgghh'))
print(split_string('aabbccddeeffgghhii'))
print(split_string('aabbccddeeffgghhiijj'))
print(split_string('aabbccddeeffgghhiijjkk'))
print(split_string('aabbccddeeffgghhiijjkkll'))
print(split_string('aabbccddeeffgghhiijjkkllmm'))
print(split_string('aabbccddeeffgghhiijjkkllmmnn'))
print(split_string('aabbccddeeffgghhiijjkkllmmnnoo'))
print(split_string('aabbccddeeffgghhiijjkkllmmnnoopp'))
print(split_string('aabbccddeeffgghhiijjkkllmmnnooppqq'))
print(split_string('aabbccddeeffgghhiijjkkllmmnnooppqqrr'))
print(split_string('aabbccddeeffgghhiijjkkllmmnnooppqqrrsstt'))
print(split_string('aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuu'))
print(split_string('aabbccddee