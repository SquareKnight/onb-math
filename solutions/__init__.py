global modules, inputvars
modules = []
inputvars = []

import os
for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py' or module[-3:] != '.py' or module[0:5] != 'euler':
        continue
    __import__('solutions.' + module[:-3], locals(), globals())
    modules.append(module[:-3])

    if modules[-1]=='euler001':
        tmp = euler001.__doc__.split('\n')
        print(tmp[0])
del module


