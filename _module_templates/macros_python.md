<!--

author:   DART Team
email:    dart@chop.edu
version:  2.0.1
current_version_description: Added Pyodide macros and lesson prep; make liascript link(s) point to first page
language: en
narrator: UK English Female
title: Python Module Macros
comment:  This is placeholder module to save macros used in other modules.

@version_history 

Previous versions: 
- [1.1.0](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/3fba6b6cef5cb9477151c3f8c775951712867c12/_module_templates/macros_python.md#1): Added current\_version\_description and version\_history metadata
- [1.0.0](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/e983922162e6fbf971c03dc96052f68713cc72af/_module_templates/macros_python.md#1): Initial version
@end

import: https://raw.githubusercontent.com/LiaTemplates/Pyodide/master/README.md

@lesson_prep_python_pyodide
You will have opportunities for hands-on coding as you work your way through this module using interactive python cells.
The interactive python cells are powered by [Pyodide](https://github.com/pyodide/pyodide#what-is-pyodide). For the most part, these will appear with some code already in them, and you can run that code by clicking the **Execute** button <i aria-hidden="true" class="icon icon-compile-circle lia-btn__icon"></i> below and to the left of the cell.

**Give it a try:**

```python
print(7+2)
```
@Pyodide.eval

You can also edit the code in these cells and run your own code. 
**Try changing the expression in the cell above and re-running the code.**

When you edit code in a cell, you can "undo" the edits by clicking the **step back** button <i aria-hidden="true" class="icon icon-chevron-left lia-btn__icon"></i> at the bottom right of the code cell to return the code to its original state.
**Try stepping back through the code by clicking <i aria-hidden="true" class="icon icon-chevron-left lia-btn__icon"></i>.**

Variables will remain from one cell to the next:

```python
n = 3
n
```
@Pyodide.eval

These cells will compute everything you ask them to, but will only display what you explicitly request using the `print()` command.

```python
print(n*5)
```
@Pyodide.eval

If the cell can't compute the code you entered, you will get an error message which may be helpful in determining where your code went wrong:

```python
print(m+7)
```
@Pyodide.eval

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

Variables will persist from one page to the next as you navigate this module using the arrows or table of contents. 

If you reload the webpage, however, all of the cells will reset to their original state and you may need to navigate to an earlier page to re-define some variables.

</div>

@end


@pyodide_readcsv
```python   @Pyodide.exec
import pandas as pd
import io
from pyodide.http import open_url

url = @1

url_contents = open_url(url)
text = url_contents.read()
file = io.StringIO(text)

@0 = pd.read_csv(file);

"HTML: <a href='" + url + "'>@0</a> has been loaded"
```
@end


@pyodide_readcsv_explainer
<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

**If you refresh your browser at some point while working on this module, you will need to come back to this page to reload the data.**

</div>

<div class = "behind-the-scenes">
<b style="color: rgb(var(--color-highlight));">Behind the scenes</b><br>

**Why is the code including `pd.read_csv()` not executable?**

We're running Python in the browser for this module using [pyodide](https://pyodide.org/en/stable/index.html).
For the most part, the commands we would use to run Python with pyodide are exactly the same as the commands you would use when running Python on your own computer, but the one major exception is reading in data files. 

So, we do something a little sneaky with the code here -- we run a set of pyodide-specific commands to read in the data without displaying that code on the page, and then we include a non-executable code box showing the code you would actually want to run to do this on your own computer. 

If you're curious about pyodide, you can [view our modules, including this one, in their raw format](https://github.com/arcus/education_modules) to see the extra code. 
But there's no reason to bother with this unless you're curious! 
That's why we hid that extra code in the first place. 

</div>
@end

@pip_install
```python   @Pyodide.exec
import micropip
micropip.install('@0')
```
@end

@lesson_prep_python_sage
@sage

You will have opportunities for hands-on coding as you work your way through this module using interactive python cells.
The interactive python cells are powered by [SageMathCell](https://sagecell.sagemath.org/). For the most part, these will appear with some code already in them, and you can run that code by clicking the **Run python** button. You can also edit the code in these cells and run your own code.


**Give it a try:**
<div class="python">
<lia-keep>
<script type="text/x-sage">
print(7+2)
</script>
</lia-keep>
</div>

Code will not persist from one page to the next, and you can always refresh the page to return the code (and the stored memory of the cell) to its initial state.

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

These cells will compute everything you ask them to, but will only display what you explicitly request using the `print()` command.

</div>

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

**Navigating with arrow keys**

You can navigate the pages of this course using left and right arrow keys. This means that you **cannot** use left and right arrow keys to navigate **within** a code cell.

</div>

@end


@sage
<script input="hidden">
// Make *any* div with class 'python' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.python',
                       evalButtonText: 'Run python',
                       languages: ["python"],
                       hide: ['fullScreen', 'permalink'],
                       });
// Make *any* div with class 'python_run' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.python_run',
                      evalButtonText: 'Run python',
                      languages: ["python"],
                      hide: ['fullScreen', 'permalink'],
                      autoeval: 'true'
                      });
// Make *any* div with class 'python_link' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.python_link',
                      evalButtonText: 'Run python',
                      languages: ["python"],
                      hide: ['fullScreen', 'permalink'],
                      autoeval: 'false',
                      linked: 'true'
                      });
// Make *any* div with class 'python_data_init' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.python_data_init',
                      evalButtonText: 'Run python',
                      languages: ["python"],
                      editor: 'codemirror-readonly',
                      hide: ['fullScreen', 'permalink','output','evalButton'],
                      autoeval: 'true',
                      linked: 'true',
                      linkKey: "data"
                      });       
// Make *any* div with class 'python_data' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.python_data',
                      evalButtonText: 'Run python',
                      languages: ["python"],
                      hide: ['fullScreen', 'permalink'],
                      autoeval: 'false',
                      linked: 'true',
                      linkKey: "data"
                      });                

// Make *any* div with class 'r' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.r',
                      evalButtonText: 'Run R',
                      languages: ["r"],
                      hide: ['fullScreen', 'permalink'],
                      });
// Make *any* div with class 'r_run' a Sage cell
sagecell.makeSagecell({inputLocation: 'div.r_run',
                      evalButtonText: 'Run R',
                      languages: ["r"],
                      hide: ['fullScreen', 'permalink'],
                      autoeval: 'true'
                      });
</script>
@end

script: https://sagecell.sagemath.org/static/embedded_sagecell.js

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
-->

# Python Module Macros
## Pyodide

@lesson_prep_python_pyodide

@pyodide_readcsv_explainer

## Sage Math Cells
@sage

@lesson_prep_python_sage
