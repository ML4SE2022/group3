I have a html file that I am parsing with BeautifulSoup. I want to get the context of a search. For example, if I search for "hello", I want to get the context of the search.

For example, if I have the following html:

<code>&lt;html&gt;
&lt;body&gt;
&lt;p&gt;hello world&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;
</code>

I want to get the context of the search "hello". I want to get the following:

<code>&lt;p&gt;hello world&lt;/p&gt;
</code>

I have tried the following:

<code>from bs4 import BeautifulSoup

html = """
&lt;html&gt;
&lt;body&gt;
&lt;p&gt;hello world&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;
"""

soup = BeautifulSoup(html, 'html.parser')

print(soup.find('hello'))
</code>

But I get the following error:

<code>Traceback (most recent call last):
  File "test.py", line 12, in &lt;module&gt;
    print(soup.find('hello'))
TypeError: 'NoneType' object is not callable
</code>

How can I get the context of a search in BeautifulSoup?


A:

You can use <code>find_all</code> with <code>string</code> argument:
<code>from bs4 import BeautifulSoup

html = """
&lt;html&gt;
&lt;body&gt;
&lt;p&gt;hello world&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;
"""

soup = BeautifulSoup(html, 'html.parser')

print(soup.find_all(string='hello'))
</code>