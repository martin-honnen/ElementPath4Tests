from lxml import etree

from elementpath import select

from elementpath.xpath3 import XPath3Parser

root = etree.fromstring('''<root>
  <item>
    <foo>foo 1</foo>
    <bar>bar 1</bar>
  </item>
  <item>
    <foo>foo 2</foo>
    <bar>bar 2</bar>
  </item>
</root>''')

print(root)

array_seq = select(root, 'item/array{ data(*) }', parser=XPath3Parser)

print(array_seq)

for array_item in array_seq:
    print(array_item)

print(array_seq)

for array_item in array_seq:
    print(array_item.source)

array_seq = select(root, 'item/array{ * ! string() }', parser=XPath3Parser)

print(array_seq)

for array_item in array_seq:
    print(array_item)

print(array_seq)

for array_item in array_seq:
    print(array_item.source)