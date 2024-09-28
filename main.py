import random

class passwordGenerator:
    Numbers = 3
    Specials = 4
    Capitals = 3
    Letters = 10

    SpecialCharacters = ['#', '%', '!', '?', '$']

    @classmethod
    def generate( cls ):
        keyword = ""
        for i in range( cls.Specials ):
            keyword += cls.SpecialCharacters[ random.randint( 0, len(cls.SpecialCharacters)-1 ) ]

        for i in range( cls.Numbers ):
            keyword += chr( random.randint( 48, 57 ) )

        for i in range( cls.Capitals ):
            keyword += chr( random.randint( 65, 90 ) )

        for i in range( cls.Letters ):
            keyword += chr( random.randint( 97, 122 ) )

    
        result = "".join( random.sample( keyword, len( keyword ) ) )

        return result

