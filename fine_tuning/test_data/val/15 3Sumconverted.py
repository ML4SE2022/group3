class Solution : NEW_LINE INDENT def threeSum ( self , nums : List [ int ] ) -> List [ List [ int ] ] : NEW_LINE INDENT if len ( nums ) < 3 : NEW_LINE INDENT return [ ] NEW_LINE DEDENT ans = [ ] NEW_LINE nums . sort ( ) NEW_LINE for i in range ( len ( nums ) - 2 ) : NEW_LINE INDENT if i > 0 and nums [ i ] == nums [ i - 1 ] : NEW_LINE INDENT continue NEW_LINE DEDENT l = i + 1 NEW_LINE r = len ( nums ) - 1 NEW_LINE while l < r : NEW_LINE INDENT summ = nums [ i ] + nums [ l ] + nums [ r ] NEW_LINE if summ == 0 : NEW_LINE INDENT ans . append ( ( nums [ i ] , nums [ l ] , nums [ r ] ) ) NEW_LINE l += 1 NEW_LINE r -= 1 NEW_LINE while nums [ l ] == nums [ l - 1 ] and l < r : NEW_LINE INDENT l += 1 NEW_LINE DEDENT while nums [ r ] == nums [ r + 1 ] and l < r : NEW_LINE INDENT r -= 1 NEW_LINE DEDENT DEDENT elif summ < 0 : NEW_LINE INDENT l += 1 NEW_LINE DEDENT else : NEW_LINE INDENT r -= 1 NEW_LINE DEDENT DEDENT DEDENT return ans NEW_LINE DEDENT DEDENT