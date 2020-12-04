import unittest
from p4 import *

class TestP4(unittest.TestCase):        
    def test_p4_example(self):
        validPassPorts = ['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm',
                          'hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm']
        self.assertEqual( p4('example.txt'), (2,validPassPorts) )
        
    def test_p4_2_validPassports(self):
        result, validPassPorts = p4('validPassportsForPart2.txt')
        newValidPassPorts = ['pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f',
                            'eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm',
                            'hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022',
                            'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719']
        self.assertEqual( p4_2('validPassportsForPart2.txt', validPassPorts), (4,newValidPassPorts) )    
    
    def test_p4_2_invalidPassports(self):
        result, validPassPorts = p4('invalidPassportsForPart2.txt')
        self.assertEqual( p4_2('invalidPassportsForPart2.txt', validPassPorts), (0,[]) )      
        
if __name__ == '__main__':
    unittest.main()
