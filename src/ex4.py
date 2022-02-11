# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

def is_passport_valid(passport):
    if 'byr:' not in passport:
        return False
    ix = passport.find('byr')
    yr = int(passport[ix + 4:ix + 8])
    if yr < 1920 or yr > 2002:
        return False
    if 'iyr:' not in passport:
        return False
    ix = passport.find('iyr')
    yr = int(passport[ix + 4:ix + 8])
    if yr < 2010 or yr > 2020:
        return False
    if 'eyr:' not in passport:
        return False
    ix = passport.find('eyr')
    yr = int(passport[ix + 4:ix + 8])
    if yr < 2020 or yr > 2030:
        return False
    if 'hgt:' not in passport:
        return False
    ix = passport.find('hgt')
    hgt = passport[ix + 4:ix + 7]
    unit = passport[ix + 7:ix + 9]
    if unit == 'cm':
        # print(passport)
        unit = 'cm'
        if int(hgt) < 150 or int(hgt) > 193:
            return False
    elif passport[ix + 6:ix + 8] == 'in':
        unit = 'in'
        hgt = passport[ix + 4:ix + 6]
        if int(hgt) < 59 or int(hgt) > 76:
            return False
    else:
        return False
    if 'hcl:' not in passport:
        return False
    ix = passport.find('hcl')
    if passport[ix + 4] != '#':
        # print('no #: ' +  passport[ix+4])
        # print(passport)
        return False
    hcl = passport[ix + 5:ix + 11]
    try:
        ecl_int = int(hcl, 16)
    except ValueError as err:
        print('not hex: ' + hcl)
        return False
    if hcl[-1] == ' ':
        return False
    if 'ecl:' not in passport:
        return False

    ix = passport.find('ecl')
    ecl = passport[ix + 4:ix + 7]
    if ecl != 'amb' and \
            ecl != 'blu' and \
            ecl != 'brn' and \
            ecl != 'gry' and \
            ecl != 'grn' and \
            ecl != 'hzl' and \
            ecl != 'oth':
        return False
    if 'pid:' not in passport:
        return False
    ix = passport.find('pid')
    pid = passport[ix + 4:ix + 13]
    if not pid.isnumeric():
        return False
    if(passport[ix + 13].isnumeric()):
        print(passport)
        print(passport[ix + 13])
        return False
    cnt = passport.count(':')
    if cnt < 8 and 'cid' in passport:
        print('not enough properties')
        return False
    return True


file = open('../data/ex4.txt', 'r')
lines = file.readlines()
totalString = ''
validPassports = 0
npt = 0
for line in lines:
    totalString += (' ' + line)
    if line == '\n' or line == lines[-1]:
        npt += 1
        if(npt == 124):
            print(totalString)
        if is_passport_valid(totalString):
            validPassports += 1
            print(str(npt) +  ' is valid')
            # print(totalString)
        totalString = ''

print('valid passports: ' + str(validPassports))
