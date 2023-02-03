from lxml import etree

from elementpath import select

from elementpath.xpath3 import XPath3Parser

result = select(etree.fromstring('<root><![CDATA[This is <b>important</b>.]]></root>'), 'parse-xml-fragment(.)!serialize(.)', parser=XPath3Parser)

print(result)