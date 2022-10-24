import lxml.html

html = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

selector = lxml.html.fromstring(html)

# 所有的li标签
result = selector.xpath('//li')
print(result)

# 所有class为item-0的li标签
result = selector.xpath('//li[@class="item-0"]')
print(result)

# 所有a标签的href属性
result = selector.xpath('//li/a/@href')
print(result)

# 所有a标签的href属性，并且class为item-0的li标签
result = selector.xpath('//li[@class="item-0"]/a/@href')
print(result)

# 所有a标签的href属性，并且class为item-0或者item-1的li标签
result = selector.xpath('//li[@class="item-0" or @class="item-1"]/a/@href')
print(result)

# 所有a标签的href属性，并且class为item-0或者item-1的li标签，