KNOWN PROBLEMS
==============

CodeMirror line wrapping
************************

Since v2.24, the behavior of ``lineWrapping`` seems to have changed, with some *old* 
browsers like FF 4.0.1 which have cursor issue in CodeMirror with end of lines, wrapped 
or not, the cursor is often badly positionned at end of lines.

From issues of CodeMirror, it seems it could be reproduced on other browser but this is 
not confirmed.

**Fix :** Always set ``lineWrapping`` to *False*, this will fix the cursor issue. But you 
          loose the line wrapping feature.
