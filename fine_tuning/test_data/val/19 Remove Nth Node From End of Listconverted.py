class Solution : NEW_LINE INDENT def removeNthFromEnd ( self , head , n ) : NEW_LINE INDENT slow = head NEW_LINE fast = head NEW_LINE for _ in range ( n ) : NEW_LINE INDENT fast = fast . next NEW_LINE DEDENT if not fast : NEW_LINE INDENT return head . next NEW_LINE DEDENT while fast . next : NEW_LINE INDENT slow = slow . next NEW_LINE fast = fast . next NEW_LINE DEDENT slow . next = slow . next . next NEW_LINE return head NEW_LINE DEDENT DEDENT