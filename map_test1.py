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

map_seq = select(root, 'item/map{ "foo" : data(foo) }', parser=XPath3Parser)

print(map_seq)

map_seq = select(root, 'item!map:merge(*!map:entry(local-name(), data()))', parser=XPath3Parser)

print(map_seq)

for map in map_seq:
    print(map.source)

for map in map_seq:
    print(map)

for map in map_seq:
    print(map.__repr__())