class Solution : NEW_LINE INDENT def maxArea ( self , height ) : NEW_LINE INDENT ans = 0 NEW_LINE l = 0 NEW_LINE r = len ( height ) - 1 NEW_LINE while l < r : NEW_LINE INDENT minHeight = min ( height [ l ] , height [ r ] ) NEW_LINE ans = max ( ans , minHeight * ( r - l ) ) NEW_LINE if height [ l ] < height [ r ] : NEW_LINE INDENT l += 1 NEW_LINE DEDENT else : NEW_LINE INDENT r -= 1 NEW_LINE DEDENT DEDENT return ans NEW_LINE DEDENT DEDENT
class Solution : NEW_LINE INDENT def intToRoman ( self , num ) : NEW_LINE INDENT valueSymbols = [ ( 1000 , ' M ' ) , ( 900 , ' CM ' ) , ( 500 , ' D ' ) , ( 400 , ' CD ' ) , ( 100 , ' C ' ) , ( 90 , ' XC ' ) , ( 50 , ' L ' ) , ( 40 , ' XL ' ) , ( 10 , ' X ' ) , ( 9 , ' IX ' ) , ( 5 , ' V ' ) , ( 4 , ' IV ' ) , ( 1 , ' I ' ) ] NEW_LINE ans = [ ] NEW_LINE for value , symbol in valueSymbols : NEW_LINE INDENT if num == 0 : NEW_LINE INDENT break NEW_LINE DEDENT count , num = divmod ( num , value ) NEW_LINE ans . append ( symbol * count ) NEW_LINE DEDENT return ' ' . join ( ans ) NEW_LINE DEDENT DEDENT
class Solution : NEW_LINE INDENT def romanToInt ( self , s ) : NEW_LINE INDENT ans = 0 NEW_LINE roman = { ' I ' : 1 , ' V ' : 5 , ' X ' : 10 , ' L ' : 50 , ' C ' : 100 , ' D ' : 500 , ' M ' : 1000 } NEW_LINE for a , b in zip ( s , s [ 1 : ] ) : NEW_LINE INDENT if roman [ a ] < roman [ b ] : NEW_LINE INDENT ans -= roman [ a ] NEW_LINE DEDENT else : NEW_LINE INDENT ans += roman [ a ] NEW_LINE DEDENT DEDENT return ans + roman [ s [ - 1 ] ] NEW_LINE DEDENT DEDENT
class Solution : NEW_LINE INDENT def longestCommonPrefix ( self , strs ) : NEW_LINE INDENT if not strs : NEW_LINE INDENT return ' ' NEW_LINE DEDENT for i in range ( len ( strs [ 0 ] ) ) : NEW_LINE INDENT for j in range ( 1 , len ( strs ) ) : NEW_LINE INDENT if i == len ( strs [ j ] ) or strs [ j ] [ i ] != strs [ 0 ] [ i ] : NEW_LINE INDENT return strs [ 0 ] [ : i ] NEW_LINE DEDENT DEDENT DEDENT return strs [ 0 ] NEW_LINE DEDENT DEDENT
class Solution : NEW_LINE INDENT def threeSum ( self , nums ) : NEW_LINE INDENT if len ( nums ) < 3 : NEW_LINE INDENT return [ ] NEW_LINE DEDENT ans = [ ] NEW_LINE nums . sort ( ) NEW_LINE for i in range ( len ( nums ) - 2 ) : NEW_LINE INDENT if i > 0 and nums [ i ] == nums [ i - 1 ] : NEW_LINE INDENT continue NEW_LINE DEDENT l = i + 1 NEW_LINE r = len ( nums ) - 1 NEW_LINE while l < r : NEW_LINE INDENT summ = nums [ i ] + nums [ l ] + nums [ r ] NEW_LINE if summ == 0 : NEW_LINE INDENT ans . append ( ( nums [ i ] , nums [ l ] , nums [ r ] ) ) NEW_LINE l += 1 NEW_LINE r -= 1 NEW_LINE while nums [ l ] == nums [ l - 1 ] and l < r : NEW_LINE INDENT l += 1 NEW_LINE DEDENT while nums [ r ] == nums [ r + 1 ] and l < r : NEW_LINE INDENT r -= 1 NEW_LINE DEDENT DEDENT elif summ < 0 : NEW_LINE INDENT l += 1 NEW_LINE DEDENT else : NEW_LINE INDENT r -= 1 NEW_LINE DEDENT DEDENT DEDENT return ans NEW_LINE DEDENT DEDENT
class Solution : NEW_LINE INDENT def threeSumClosest ( self , nums , target ) : NEW_LINE INDENT ans = nums [ 0 ] + nums [ 1 ] + nums [ 2 ] NEW_LINE nums . sort ( ) NEW_LINE for i in range ( len ( nums ) - 2 ) : NEW_LINE INDENT if i > 0 and nums [ i ] == nums [ i - 1 ] : NEW_LINE INDENT continue NEW_LINE DEDENT l = i + 1 NEW_LINE r = len ( nums ) - 1 NEW_LINE while l < r : NEW_LINE INDENT summ = nums [ i ] + nums [ l ] + nums [ r ] NEW_LINE if summ == target : NEW_LINE INDENT return summ NEW_LINE DEDENT if abs ( summ - target ) < abs ( ans - target ) : NEW_LINE INDENT ans = summ NEW_LINE DEDENT if summ < target : NEW_LINE INDENT l += 1 NEW_LINE DEDENT else : NEW_LINE INDENT r -= 1 NEW_LINE DEDENT DEDENT DEDENT return ans NEW_LINE DEDENT DEDENT
class Solution : NEW_LINE INDENT def letterCombinations ( self , digits ) : NEW_LINE INDENT if not digits : NEW_LINE INDENT return [ ] NEW_LINE DEDENT digitToLetters = [ ' ' , ' ' , ' abc ' , ' def ' , ' ghi ' , ' jkl ' , ' mno ' , ' pqrs ' , ' tuv ' , ' wxyz ' ] NEW_LINE ans = [ ] NEW_LINE def dfs ( i : int , path ) : NEW_LINE INDENT if i == len ( digits ) : NEW_LINE INDENT ans . append ( ' ' . join ( path ) ) NEW_LINE return NEW_LINE DEDENT for letter in digitToLetters [ ord ( digits [ i ] ) - ord ( '0' ) ] : NEW_LINE INDENT path . append ( letter ) NEW_LINE dfs ( i + 1 , path ) NEW_LINE path . pop ( ) NEW_LINE DEDENT DEDENT dfs ( 0 , [ ] ) NEW_LINE return ans NEW_LINE DEDENT DEDENT
class Solution : NEW_LINE INDENT def fourSum ( self , nums , target ) : NEW_LINE INDENT ans = [ ] NEW_LINE def nSum ( l : int , r : int , target : int , n : int , path , ans ) -> None : NEW_LINE INDENT if r - l + 1 < n or n < 2 or target < nums [ l ] * n or target > nums [ r ] * n : NEW_LINE INDENT return NEW_LINE DEDENT if n == 2 : NEW_LINE INDENT while l < r : NEW_LINE INDENT summ = nums [ l ] + nums [ r ] NEW_LINE if summ == target : NEW_LINE INDENT ans . append ( path + [ nums [ l ] , nums [ r ] ] ) NEW_LINE l += 1 NEW_LINE while nums [ l ] == nums [ l - 1 ] and l < r : NEW_LINE INDENT l += 1 NEW_LINE DEDENT DEDENT elif summ < target : NEW_LINE INDENT l += 1 NEW_LINE DEDENT else : NEW_LINE INDENT r -= 1 NEW_LINE DEDENT DEDENT return NEW_LINE DEDENT for i in range ( l , r + 1 ) : NEW_LINE INDENT if i > l and nums [ i ] == nums [ i - 1 ] : NEW_LINE INDENT continue NEW_LINE DEDENT nSum ( i + 1 , r , target - nums [ i ] , n - 1 , path + [ nums [ i ] ] , ans ) NEW_LINE DEDENT DEDENT nums . sort ( ) NEW_LINE nSum ( 0 , len ( nums ) - 1 , target , 4 , [ ] , ans ) NEW_LINE return ans NEW_LINE DEDENT DEDENT
class Solution : NEW_LINE INDENT def removeNthFromEnd ( self , head , n ) : NEW_LINE INDENT slow = head NEW_LINE fast = head NEW_LINE for _ in range ( n ) : NEW_LINE INDENT fast = fast . next NEW_LINE DEDENT if not fast : NEW_LINE INDENT return head . next NEW_LINE DEDENT while fast . next : NEW_LINE INDENT slow = slow . next NEW_LINE fast = fast . next NEW_LINE DEDENT slow . next = slow . next . next NEW_LINE return head NEW_LINE DEDENT DEDENT
class Solution : NEW_LINE INDENT def isValid ( self , s ) : NEW_LINE INDENT stack = [ ] NEW_LINE for c in s : NEW_LINE INDENT if c == ' ( ' : NEW_LINE INDENT stack . append ( ' ) ' ) NEW_LINE DEDENT elif c == ' { ' : NEW_LINE INDENT stack . append ( ' } ' ) NEW_LINE DEDENT elif c == ' [ ' : NEW_LINE INDENT stack . append ( ' ] ' ) NEW_LINE DEDENT elif not stack or stack . pop ( ) != c : NEW_LINE INDENT return False NEW_LINE DEDENT DEDENT return not stack NEW_LINE DEDENT DEDENT
