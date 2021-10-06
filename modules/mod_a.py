from mod_c import *
from mod_b import *

print(mod_c.x)

#We are import modules "mod_c" and "mod_b". Okay, now we can use objects, which are contained in modules, but by means of importing modules new namespaces are creating. Now to get access for any object of modules we must specify namespace of module.

#--------------

#In second case we get number 5 because code was operated consistently. When "import mod_b" was operating x variable was rewritten as list to integer. And we printed integer.

#--------------

#In last case we are get the same result, because "from" construction used for importing special function or few functions and variables, but with "*" specifier we are importing all functions and vaariables.
