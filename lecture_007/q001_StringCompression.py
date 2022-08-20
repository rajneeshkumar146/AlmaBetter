# ch is character
def isLowerCase(ch):
    return ch >= 'a' and ch <= 'z'

# ch is character


def isUpperCase(ch):
    return ch >= 'A' and ch <= 'Z'


# ch is character
def isDigit(ch):
    return ch >= '0' and ch <= '9'


def convertSmallCharacterLarge(ch):
    return chr(ord(ch) - ord('a') + ord('A'))


def convertLargeCharacterSmall(ch):
    return chr(ord(ch) - ord('A') + ord('a'))

# T: O(N)


def upper(str):
    l = len(str)
    ans = ""

    for i in range(l):
        if isLowerCase(str[i]):
            ans += convertSmallCharacterLarge(str[i])
        else:
            ans += str[i]

    return ans


def lower(str):
    l = len(str)
    ans = ""

    for i in range(l):
        if isUpperCase(str[i]):
            ans += convertLargeCharacterSmall(str[i])
        else:
            ans += str[i]

    return ans


# akASD1543*&^ -> AKasd1543*&^
# small -> Large, Large -> small, rest will same
def toggleCharacters():
    l = len(str)
    ans = ""

    for i in range(l):
        if isUpperCase(str[i]):
            ans += convertLargeCharacterSmall(str[i])
        elif isLowerCase(str[i]):
            ans += convertSmallCharacterLarge(str[i])
        else:
            ans += str[i]

    return ans
