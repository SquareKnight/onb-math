global modules, inputvars
modules = {}
inputvars = []

import os
for module in os.listdir(os.path.dirname(__file__)):
    # loop through all the files in the directory that this __init__.py file is in, and skip the loop if it isn't an eulerxxx.py
    if module == '__init__.py' or module[-3:] != '.py' or module[0:5] != 'euler':
        continue

    # if it is eulerxxx.py, import it
    __import__('solutions.' + module[:-3], locals(), globals())
    # and read in the docstring *
    s = eval(module[:-3]+'.__doc__')
    s = s.split('\n', 3)
    title = s[0] if len(s) > 0 else ''
    args = s[1] if len(s) > 1 else ''
    tags = [t[1:] for t in s[2].split('\t')] if len(s) > 2 else []
    text = s[3] if len(s) > 3 else ''

    modules[module[:-3]] = ((module[:-3], title, args, tags, text))
del module

# * note that all Euler files have the same docstring:
"""<here goes the title>
<here is a tab-separated list of inputs, each input is a semicolon-sepped triplet of name, descr and type: n;upper bound;int    b:something else:list
#<tags> #<again, tab-separated>
<all the rest of the docstring is put in one final string. 
Place the description from Project Euler here!
"""


