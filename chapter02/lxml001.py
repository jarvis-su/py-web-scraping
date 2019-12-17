import lxml.html


def lxmDemo01():
    broken_html = '<ul class=country> <li>Area<li>Population</ul>'
    tree = lxml.html.fromstring(broken_html)
    fixed_html = lxml.html.tostring(tree, pretty_print=True)
    print('')
    print(fixed_html)


if __name__ == '__main__':
    lxmDemo01()
