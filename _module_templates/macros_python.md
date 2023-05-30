<!--

author:   DART Team
email:    dart@chop.edu
version:  1.0.0
language: en
narrator: UK English Female
title: Python Module Macros
comment:  This is placeholder module to save macros used in other modules.

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

-->

# Python Module Macros

@sage

@lesson_prep_python_sage
