from lxml import etree

from elementpath import select

from elementpath.xpath3 import XPath3Parser

result = select(etree.fromstring('<root>This is <b>important</b>.</root>'), 'serialize(.)', parser=XPath3Parser)

print(result)

result = select(etree.fromstring('<root>This is <b>important</b>.</root>'), 'serialize(node())', parser=XPath3Parser)

print(result)