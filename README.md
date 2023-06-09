# Conlay - Console Layout

[![PyPi version][shields-pypi_version]][url-pypi_version]
[![Github Issues][shields-issues]][url-issues]
[![Github License][shields-license]][url-license]

Create visually pleasing console layouts with this easy-to-use Python library. 


## Installing

Install using <a href="https://pip.pypa.io/en/stable/">pip</a>

```bash
pip install conlay
```

or install it from <a href="https://pypi.org/project/conlay/#files">PyPi</a>


## Example

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

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃╭──────────────╮            ┃
┃│this is a test│            ┃
┃╰──────────────╯            ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


>
```


## Conlay()

`Conlay()` is the core class within the library. It generates and prints out the layout.

```python
layout = Conlay()
```


### Conlay.add()
You can use `add()` to assign <a href="https://github.com/Salliii/conlay#LayoutElement()">LayoutElements</a> to other <a href="https://github.com/Salliii/conlay#LayoutElement()">LayoutElements</a>.

Syntax:
```python
parent.add(child)
```

Example:
```python
# add a LayoutElement to the main layout 
layout = Conlay()
layout.add(ThinBox(...))

# add a LayoutElement to another LayoutElement
BoldBox(...).add(ThinLabel(...))
```


### Conlay.print()
You have to call `print()` to generate and print out the layout.

Syntax:
```python
layout.print()
```

Example:
```python
layout = Conlay()
...
layout.print()
```


## Summary

- <a href="https://github.com/Salliii/conlay#conlay">Conlay()</a>
  - <a href="https://github.com/Salliii/conlay#conlayadd">_add()_</a>
  - <a href="https://github.com/Salliii/conlay#conlayprint">_print()_</a>

##### Elements
- <a href="https://github.com/Salliii/conlay#layoutelement">LayoutElement()</a>
- <a href="https://github.com/Salliii/conlay#box">Box()</a>
- <a href="https://github.com/Salliii/conlay#thinbox">ThinBox()</a>
- <a href="https://github.com/Salliii/conlay#boldbox">BoldBox()</a>
- <a href="https://github.com/Salliii/conlay#label">Label()</a>
- <a href="https://github.com/Salliii/conlay#thinlabel">ThinLabel()</a>
- <a href="https://github.com/Salliii/conlay#boldlabel">BoldLabel()</a>

##### Cursor & Console
- <a href="https://github.com/Salliii/conlay#cursor">Cursor</a>
  - <a href="https://github.com/Salliii/conlay#cursorsetposition">_setPosition()_</a>
  - <a href="https://github.com/Salliii/conlay#cursorshifthorizontal">_shiftHorizontal()_</a>
  - <a href="https://github.com/Salliii/conlay#cursorshiftvertical">_shiftVertical()_</a>
  - <a href="https://github.com/Salliii/conlay#cursorhide">_hide()_</a>
  - <a href="https://github.com/Salliii/conlay#cursorshow">_show()_</a>

- <a href="https://github.com/Salliii/conlay#console">Console</a>
  - <a href="https://github.com/Salliii/conlay#consolereset">_reset()_</a>
  - <a href="https://github.com/Salliii/conlay#consoleclear">_clear()_</a>
  - <a href="https://github.com/Salliii/conlay#consoleeraselinetoend">_eraseLineToEnd()_</a>
  - <a href="https://github.com/Salliii/conlay#consoleeraselinefromstart">_eraseLineFromStart()_</a>
  - <a href="https://github.com/Salliii/conlay#consoleeraseline">_eraseLine()_</a>

##### Coloring
- <a href="https://github.com/Salliii/conlay#color">Color</a>
  - <a href="https://github.com/Salliii/conlay#colorbg">Bg</a>
    - <a href="https://github.com/Salliii/conlay#colorbgrgb">_rgb()_</a>
  - <a href="https://github.com/Salliii/conlay#colorfg">Fg</a>
    - <a href="https://github.com/Salliii/conlay#colorfgrgb">_rgb()_</a>

##### Border & Border Types
- <a href="https://github.com/Salliii/conlay#border">Border</a>
- <a href="https://github.com/Salliii/conlay#bold">Bold</a>
- <a href="https://github.com/Salliii/conlay#thin">Thin</a>


## License

Licensed under the <a href="https://github.com/Salliii/conlay/blob/main/LICENSE">MIT License</a>.




<!-- shields -->
[shields-pypi_version]: https://img.shields.io/pypi/v/conlay?label=PyPi%20Version&style=for-the-badge
[shields-issues]: https://img.shields.io/github/issues/Salliii/conlay?style=for-the-badge
[shields-license]: https://img.shields.io/github/license/Salliii/conlay?style=for-the-badge

<!-- url -->
[url-pypi_version]: https://pypi.org/project/conlay/
[url-issues]: https://github.com/Salliii/conlay/issues
[url-license]: https://github.com/Salliii/conlay/blob/main/LICENSE