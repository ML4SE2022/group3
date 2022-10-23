I have two lists:
<code>a = [1, 2, 3, 4, 5]
b = [2, 4, 1, 3, 5]
</code>
I want to sort <code>a</code> based on the order of <code>b</code>.
The result should be:
<code>a = [2, 4, 1, 3, 5]
</code>
How can I do this?


A:

You can use <code>sorted</code> with a custom key function:
<code>&gt;&gt;&gt; a = [1, 2, 3, 4, 5]
&gt;&gt;&gt; b = [2, 4, 1, 3, 5]
&gt;&gt;&gt; sorted(a, key=b.index)
[2, 4, 1, 3, 5]
</code>