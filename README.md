Conlay - Console Layout
=======================

[![PyPi version][shields-pypi_version]][url-pypi_version]
[![Github Issues][shields-issues]][url-issues]
[![Github License][shields-license]][url-license]

Create visually pleasing console layouts with this easy-to-use Python library. 


Installing
----------

Install using <a href="https://pip.pypa.io/en/stable/">pip</a>

```bash
pip install conlay
```

or install it from <a href="https://pypi.org/project/conlay/#files">PyPi</a>


Example
-------

```python
from conlay import *

layout = Conlay()

blank_box = BoldBox(0, 0, 30, 5)
layout.add(blank_box)

label = ThinLabel(0, 0, "this is a test")
blank_box.add(label)

layout.print()
``` 

Console output:

```bash
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃╭──────────────╮            ┃
┃│this is a test│            ┃
┃╰──────────────╯            ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


>
```


Summary
-------
- <a href="https://github.com/Salliii/conlay#Conlay">Conlay</a>
  - <a href="https://github.com/Salliii/conlay#Conlay.add()">_add()_</a>
  - <a href="https://github.com/Salliii/conlay#Conlay.print()">_print()_</a>

- <a href="https://github.com/Salliii/conlay#LayoutElement">LayoutElement</a>
- <a href="https://github.com/Salliii/conlay#Box">Box</a>
- <a href="https://github.com/Salliii/conlay#ThinBox">ThinBox</a>
- <a href="https://github.com/Salliii/conlay#BoldBox">BoldBox</a>
- <a href="https://github.com/Salliii/conlay#Label">Label</a>
- <a href="https://github.com/Salliii/conlay#ThinLabel">ThinLabel</a>
- <a href="https://github.com/Salliii/conlay#BoldLabel">BoldLabel</a>

- <a href="https://github.com/Salliii/conlay#Cursor">Cursor</a>
  - <a href="https://github.com/Salliii/conlay#Cursor.setPosition()">_setPosition()_</a>
  - <a href="https://github.com/Salliii/conlay#Cursor.shiftHorizontal()">_shiftHorizontal()_</a>
  - <a href="https://github.com/Salliii/conlay#Cursor.shiftVertical()">_shiftVertical()_</a>
  - <a href="https://github.com/Salliii/conlay#Cursor.hide()">_hide()_</a>
  - <a href="https://github.com/Salliii/conlay#Cursor.show()">_show()_</a>

- <a href="https://github.com/Salliii/conlay#Console">Console</a>
  - <a href="https://github.com/Salliii/conlay#Console.reset()">_reset()_</a>
  - <a href="https://github.com/Salliii/conlay#Console.clear()">_clear()_</a>
  - <a href="https://github.com/Salliii/conlay#Console.eraseLineToEnd()">_eraseLineToEnd()_</a>
  - <a href="https://github.com/Salliii/conlay#Console.eraseLineFromStart()">_eraseLineFromStart()_</a>
  - <a href="https://github.com/Salliii/conlay#Console.eraseLine()">_eraseLine()_</a>

- <a href="https://github.com/Salliii/conlay#Color">Color</a>
  - <a href="https://github.com/Salliii/conlay#Color.Bg">Bg</a>
    - <a href="https://github.com/Salliii/conlay#Color.Bg.rgb()">_rgb()_</a>
  - <a href="https://github.com/Salliii/conlay#Color.Fg">Fg</a>
    - <a href="https://github.com/Salliii/conlay#Color.Fg.rgb()">_rgb()_</a>

- <a href="https://github.com/Salliii/conlay#Border">Border</a>
- <a href="https://github.com/Salliii/conlay#Bold">Bold</a>
- <a href="https://github.com/Salliii/conlay#Thin">Thin</a>


License
-------
Licensed under the <a href="https://github.com/Salliii/conlay/blob/main/LICENSE">MIT License</a>.




<!-- shields -->
[shields-pypi_version]: https://img.shields.io/pypi/v/conlay?label=PyPi%20Version&style=for-the-badge
[shields-issues]: https://img.shields.io/github/issues/Salliii/conlay?style=for-the-badge
[shields-license]: https://img.shields.io/github/license/Salliii/conlay?style=for-the-badge

<!-- url -->
[url-pypi_version]: https://pypi.org/project/conlay/
[url-issues]: https://github.com/Salliii/conlay/issues
[url-license]: https://github.com/Salliii/conlay/blob/main/LICENSE