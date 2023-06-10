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
You can use `add()` to add <a href="https://github.com/Salliii/conlay#LayoutElement()">LayoutElements</a> to other <a href="https://github.com/Salliii/conlay#LayoutElement()">LayoutElements</a>.

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




## Cursor
The `Cursor` class provides a few functions for simple <a href="https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797">Ansi Escape</a> cursor actions.


### Cursor.setPosition()
Set the cursor to a specific position. The <a href="https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797">Ansi Escape Sequence</a> used for this command is `\x1b[<y>;<x>H`.

Syntax:

```python
Cursor.setPosition(x, y)
```

Example:

```python
Cursor.setPosition(10, 5)
```


### Cursor.shiftHorizontal()
Move the cursor along the X axis. The <a href="https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797">Ansi Escape Sequence</a> used for this command is `\x1b[<x>D` and `\x1b[<x>C`.

Syntax:

```python
Cursor.shiftHorizontal(x)
```

Example:

```python
# move the cursor 10 collumns to the right
Cursor.shiftHorizontal(10)

# move the cursor 5 collumns to the left
Cursor.shiftHorizontal(-5)
```


### Cursor.shiftVertical()
Move the cursor along the Y axis. The <a href="https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797">Ansi Escape Sequence</a> used for this command is `\x1b[<y>A` and `\x1b[<y>B`.

Syntax:

```python
Cursor.shiftVertical(y)
```

Example:

```python
# move the cursor 10 collumns down
Cursor.shiftVertical(10)

# move the cursor 5 collumns up
Cursor.shiftVertical(-5)
```


### Cursor.hide()
Hides the cursor. The <a href="https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797">Ansi Escape Sequence</a> used for this command is `\x1b[?25l`.

Syntax:

```python
Cursor.hide()
```


### Cursor.show()
Shows the cursor. The <a href="https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797">Ansi Escape Sequence</a> used for this command is `\x1b[?25h`.

Syntax:

```python
Cursor.show()
```




## Console
The `Console` class provides a few functions for simple <a href="https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797">Ansi Escape</a> console actions.


### Console.reset()
This Function resets the console. The <a href="https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797">Ansi Escape Sequence</a> used for this command is `\x1bc`.

Syntax:

```python
Console.reset()
```


### Console.clear()
This Function clears the console. The <a href="https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797">Ansi Escape Sequence</a> used for this command is `\x1b[3J`.

Syntax:

```python
Console.clear()
```


### Console.eraseLineToEnd()
Erase the line from the cursor position to the end. The <a href="https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797">Ansi Escape Sequence</a> used for this command is `\x1b[0K`.

Syntax:

```python
Console.eraseLineToEnd()
```


### Console.eraseLineFromStart()
Erase the line from start to the cursor position. The <a href="https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797">Ansi Escape Sequence</a> used for this command is `\x1b[1K`.

Syntax:

```python
Console.eraseLineFromStart()
```


### Console.eraseLine()
Erase the line. The <a href="https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797">Ansi Escape Sequence</a> used for this command is `\x1b[2K`.

Syntax:

```python
Console.eraseLine()
```




## Color
The `Color` class allows you to set the foreground and background color using the <a href="https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797#color-codes">Ansi Escape Color Codes</a>.


### Color.Bg
The `Color.Bg` class provides a few predefined background <a href="https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797#color-codes">Ansi Escape Color Codes</a>.

| Variable Name   | rgb values    | ansi escape sequence     |
| :------------   | :---------    | :-------------------     |
| Color.Bg.black  |   0,   0,   0 | `\x1b[48;2;0;0;0m`       |
| Color.Bg.white  | 255, 255, 255 | `\x1b[48;2;255;255;255m` |
| Color.Bg.red    | 205,  49,  49 | `\x1b[48;2;205;49;49m`   |
| Color.Bg.green  |  13, 188, 121 | `\x1b[48;2;13;188;121m`  |
| Color.Bg.blue   |  36, 114, 200 | `\x1b[48;2;36;114;200m`  |
| Color.Bg.yellow | 229, 229,  16 | `\x1b[48;2;229;229;16m`  |
| Color.Bg.purple | 188,  63, 188 | `\x1b[48;2;188;63;188m`  |
| Color.Bg.cyan   |  17, 168, 205 | `\x1b[48;2;17;168;205m`  |


### Color.Bg.rgb()
This function takes three arguments `r, g, b` and returns a customized background <a href="https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797#color-codes">Ansi Escape Color Code</a>

Syntax:

```python
Color.Bg.rgb(r, g, b)
```

Example:

```python
>>> Color.Bg.rgb(255, 0, 100)
'\x1b[48;2;255;0;100m'
```


### Color.Fg
The `Color.Fg` class provides a few predefined foreground <a href="https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797#color-codes">Ansi Escape Color Codes</a>.

| Variable Name   | rgb values    | ansi escape sequence     |
| :------------   | :---------    | :-------------------     |
| Color.Fg.black  |   0,   0,   0 | `\x1b[38;2;0;0;0m`       |
| Color.Fg.white  | 255, 255, 255 | `\x1b[38;2;255;255;255m` |
| Color.Fg.red    | 205,  49,  49 | `\x1b[38;2;205;49;49m`   |
| Color.Fg.green  |  13, 188, 121 | `\x1b[38;2;13;188;121m`  |
| Color.Fg.blue   |  36, 114, 200 | `\x1b[38;2;36;114;200m`  |
| Color.Fg.yellow | 229, 229,  16 | `\x1b[38;2;229;229;16m`  |
| Color.Fg.purple | 188,  63, 188 | `\x1b[38;2;188;63;188m`  |
| Color.Fg.cyan   |  17, 168, 205 | `\x1b[38;2;17;168;205m`  |


### Color.Fg.rgb()
This function takes three arguments `r, g, b` and returns a customized foreground <a href="https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797#color-codes">Ansi Escape Color Code</a>

Syntax:

```python
Color.Fg.rgb(r, g, b)
```

Example:

```python
>>> Color.Fg.rgb(255, 0, 100)
'\x1b[38;2;255;0;100m'
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