class Solution { public int maxArea ( int [ ] height ) { int ans = 0 ; int l = 0 ; int r = height . length - 1 ; while ( l < r ) { final int minHeight = Math . min ( height [ l ] , height [ r ] ) ; ans = Math . max ( ans , minHeight * ( r - l ) ) ; if ( height [ l ] < height [ r ] ) ++ l ; else -- r ; } return ans ; } } class Solution { public String intToRoman ( int num ) { final int [ ] values = { 1000 , 900 , 500 , 400 , 100 , 90 , 50 , 40 , 10 , 9 , 5 , 4 , 1 } ; final String [ ] symbols = { " ▁ M ▁ " , " ▁ CM ▁ " , " ▁ D ▁ " , " ▁ CD ▁ " , " ▁ C ▁ " , " ▁ XC ▁ " , " ▁ L ▁ " , " ▁ XL ▁ " , " ▁ X ▁ " , " ▁ IX ▁ " , " ▁ V ▁ " , " ▁ IV ▁ " , " ▁ I ▁ " } ; StringBuilder sb = new StringBuilder ( ) ; for ( int i = 0 ; i < values . length ; ++ i ) { if ( num == 0 ) break ; while ( num >= values [ i ] ) { num -= values [ i ] ; sb . append ( symbols [ i ] ) ; } } return sb . toString ( ) ; } } class Solution { public int romanToInt ( String s ) { int ans = 0 ; int [ ] roman = new int [ 128 ] ; roman [ ' ▁ I ▁ ' ] = 1 ; roman [ ' ▁ V ▁ ' ] = 5 ; roman [ ' ▁ X ▁ ' ] = 10 ; roman [ ' ▁ L ▁ ' ] = 50 ; roman [ ' ▁ C ▁ ' ] = 100 ; roman [ ' ▁ D ▁ ' ] = 500 ; roman [ ' ▁ M ▁ ' ] = 1000 ; for ( int i = 0 ; i + 1 < s . length ( ) ; ++ i ) if ( roman [ s . charAt ( i ) ] < roman [ s . charAt ( i + 1 ) ] ) ans -= roman [ s . charAt ( i ) ] ; else ans += roman [ s . charAt ( i ) ] ; return ans + roman [ s . charAt ( s . length ( ) - 1 ) ] ; } } class Solution { public String longestCommonPrefix ( String [ ] strs ) { if ( strs . length == 0 ) return " ▁ " ; for ( int i = 0 ; i < strs [ 0 ] . length ( ) ; ++ i ) for ( int j = 1 ; j < strs . length ; ++ j ) if ( i == strs [ j ] . length ( ) || strs [ j ] . charAt ( i ) != strs [ 0 ] . charAt ( i ) ) return strs [ 0 ] . substring ( 0 , i ) ; return strs [ 0 ] ; } } class Solution { public List < List < Integer > > threeSum ( int [ ] nums ) { if ( nums . length < 3 ) return new ArrayList < > ( ) ; List < List < Integer > > ans = new ArrayList < > ( ) ; Arrays . sort ( nums ) ; for ( int i = 0 ; i + 2 < nums . length ; ++ i ) { if ( i > 0 && nums [ i ] == nums [ i - 1 ] ) continue ; int l = i + 1 ; int r = nums . length - 1 ; while ( l < r ) { final int sum = nums [ i ] + nums [ l ] + nums [ r ] ; if ( sum == 0 ) { ans . add ( Arrays . asList ( nums [ i ] , nums [ l ++ ] , nums [ r -- ] ) ) ; while ( l < r && nums [ l ] == nums [ l - 1 ] ) ++ l ; while ( l < r && nums [ r ] == nums [ r + 1 ] ) -- r ; } else if ( sum < 0 ) { ++ l ; } else { -- r ; } } } return ans ; } } class Solution { public int threeSumClosest ( int [ ] nums , int target ) { int ans = nums [ 0 ] + nums [ 1 ] + nums [ 2 ] ; Arrays . sort ( nums ) ; for ( int i = 0 ; i + 2 < nums . length ; ++ i ) { if ( i > 0 && nums [ i ] == nums [ i - 1 ] ) continue ; int l = i + 1 ; int r = nums . length - 1 ; while ( l < r ) { final int sum = nums [ i ] + nums [ l ] + nums [ r ] ; if ( sum == target ) return sum ; if ( Math . abs ( sum - target ) < Math . abs ( ans - target ) ) ans = sum ; if ( sum < target ) ++ l ; else -- r ; } } return ans ; } } class Solution { public List < String > letterCombinations ( String digits ) { if ( digits . isEmpty ( ) ) return new ArrayList < > ( ) ; List < String > ans = new ArrayList < > ( ) ; dfs ( digits , 0 , new StringBuilder ( ) , ans ) ; return ans ; } private static final String [ ] digitToLetters = { " ▁ " , " ▁ " , " ▁ abc ▁ " , " ▁ def ▁ " , " ▁ ghi ▁ " , " ▁ jkl ▁ " , " ▁ mno ▁ " , " ▁ pqrs ▁ " , " ▁ tuv ▁ " , " ▁ wxyz ▁ " } ; private void dfs ( String digits , int i , StringBuilder sb , List < String > ans ) { if ( i == digits . length ( ) ) { ans . add ( sb . toString ( ) ) ; return ; } for ( final char c : digitToLetters [ digits . charAt ( i ) - '0' ] . toCharArray ( ) ) { sb . append ( c ) ; dfs ( digits , i + 1 , sb , ans ) ; sb . deleteCharAt ( sb . length ( ) - 1 ) ; } } } class Solution { public List < List < Integer > > fourSum ( int [ ] nums , int target ) { List < List < Integer > > ans = new ArrayList < > ( ) ; Arrays . sort ( nums ) ; nSum ( nums , 4 , target , 0 , nums . length - 1 , new ArrayList < > ( ) , ans ) ; return ans ; } private void nSum ( int [ ] nums , long n , long target , int l , int r , List < Integer > path , List < List < Integer > > ans ) { if ( r - l + 1 < n || target < nums [ l ] * n || target > nums [ r ] * n ) return ; if ( n == 2 ) { while ( l < r ) { final int sum = nums [ l ] + nums [ r ] ; if ( sum == target ) { path . add ( nums [ l ] ) ; path . add ( nums [ r ] ) ; ans . add ( new ArrayList < > ( path ) ) ; path . remove ( path . size ( ) - 1 ) ; path . remove ( path . size ( ) - 1 ) ; ++ l ; -- r ; while ( l < r && nums [ l ] == nums [ l - 1 ] ) ++ l ; while ( l < r && nums [ r ] == nums [ r + 1 ] ) -- r ; } else if ( sum < target ) { ++ l ; } else { -- r ; } } return ; } for ( int i = l ; i <= r ; ++ i ) { if ( i > l && nums [ i ] == nums [ i - 1 ] ) continue ; path . add ( nums [ i ] ) ; nSum ( nums , n - 1 , target - nums [ i ] , i + 1 , r , path , ans ) ; path . remove ( path . size ( ) - 1 ) ; } } } class Solution { public ListNode removeNthFromEnd ( ListNode head , int n ) { ListNode slow = head ; ListNode fast = head ; while ( n -- > 0 ) fast = fast . next ; if ( fast == null ) return head . next ; while ( fast . next != null ) { slow = slow . next ; fast = fast . next ; } slow . next = slow . next . next ; return head ; } } class Solution { public boolean isValid ( String s ) { Deque < Character > stack = new ArrayDeque < > ( ) ; for ( final char c : s . toCharArray ( ) ) if ( c == ' ▁ ( ▁ ' ) stack . push ( ' ▁ ) ▁ ' ) ; else if ( c == ' ▁ { ▁ ' ) stack . push ( ' ▁ } ▁ ' ) ; else if ( c == ' ▁ [ ▁ ' ) stack . push ( ' ▁ ] ▁ ' ) ; else if ( stack . isEmpty ( ) || stack . pop ( ) != c ) return false ; return stack . isEmpty ( ) ; } }