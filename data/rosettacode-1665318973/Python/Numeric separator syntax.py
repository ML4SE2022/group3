 [ nextword
   [] swap witheach
     [ dup char , = iff
         drop else join ]
   swap join ]            builds n ( [ $ --> $ [ )