class Solution : NEW_LINE INDENT def romanToInt ( self , s : str ) -> int : NEW_LINE INDENT ans = 0 NEW_LINE roman = { ' I ' : 1 , ' V ' : 5 , ' X ' : 10 , ' L ' : 50 , ' C ' : 100 , ' D ' : 500 , ' M ' : 1000 } NEW_LINE for a , b in zip ( s , s [ 1 : ] ) : NEW_LINE INDENT if roman [ a ] < roman [ b ] : NEW_LINE INDENT ans -= roman [ a ] NEW_LINE DEDENT else : NEW_LINE INDENT ans += roman [ a ] NEW_LINE DEDENT DEDENT return ans + roman [ s [ - 1 ] ] NEW_LINE DEDENT DEDENT