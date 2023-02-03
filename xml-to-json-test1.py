from lxml import etree

from elementpath import select

from elementpath.xpath3 import XPath3Parser

root = etree.fromstring('''<map xmlns="http://www.w3.org/2005/xpath-functions">
  <string key="foo">foo 1</string>
  <number key="value">42</number>
</map>''')

result = select(root, 'xml-to-json(.)', parser=XPath3Parser)

print(result)

result = select(root, '. => xml-to-json() => parse-json()', parser=XPath3Parser)

print(result)