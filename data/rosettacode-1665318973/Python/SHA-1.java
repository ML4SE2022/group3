/* SHA-1 hash in Jsish */
var str = 'Rosetta code';
puts(Util.hash(str, {type:'sha1'}));

/*
=!EXPECTSTART!=
b18c883f4da750164b5af362ea9b9f27f90904b4
=!EXPECTEND!=
*/