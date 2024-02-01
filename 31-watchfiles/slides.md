%title: Python
%author: xavki


██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                     
-----------------------------------------------------------------------------------------------------------                                          

# Python : Watchfiles

<br>

Purposes : reloader & check changes

	* watch change into files & directories

    'watch',
    'awatch',
    'run_process',
    'arun_process',
    'Change',
    'BaseFilter',
    'DefaultFilter',
    'PythonFilter',

Documentation : https://watchfiles.helpmanual.io/

-----------------------------------------------------------------------------------------------------------                                          

# Python : Watchfiles

<br>

* minimalist mode

```
#!/usr/bin/env python3

from watchfiles import watch

path = './dir1'
for changes in watch(path):
    print(changes)
```

-----------------------------------------------------------------------------------------------------------                                          

# Python : Watchfiles

<br>

* read all files in directory

```
#!/usr/bin/env python3

from watchfiles import watch
import os

path = './dir1'

for changes in watch(path):
    print(changes)
    dir_list = os.listdir(path)
    for file in dir_list:
      file_path = path + "/" + file
      with open(file_path, 'r') as f:
        print(f.read())
```

-----------------------------------------------------------------------------------------------------------                                          

# Python : Watchfiles

<br>

* restart a process

```
#!/usr/bin/env python3

from watchfiles import run_process
import os

file = './dir1/myfile.txt'

def printer():
  with open(file, 'r') as f:
    print(f.read())

if __name__ == '__main__':
  run_process(file, target=printer)
```

-----------------------------------------------------------------------------------------------------------                                          

# Python : Watchfiles

<br>

* restart with a callback

```
#!/usr/bin/env python3

from watchfiles import run_process
import os

file = './dir1/myfile.txt'

def printer():
  with open(file, 'r') as f:
    print(f.read())

def changer(changes):
  print('changes detected:', changes)

if __name__ == '__main__':
  run_process(file, target=printer,callback=changer)
```

-----------------------------------------------------------------------------------------------------------                                          

# Python : Watchfiles

<br>

* filter on file extensions & reuse file path directly

```
#!/usr/bin/env python3

from watchfiles import Change, DefaultFilter, watch

dir_web = './dir1/'

class WebFilter(DefaultFilter):
    allowed_extensions = '.html', '.css', '.js'

    def __call__(self, change: Change, path: str) -> bool:
        return (
            super().__call__(change, path) and
            path.endswith(self.allowed_extensions)
        )

for changes in watch(dir_web, watch_filter=WebFilter()):
    for change_info, file in changes:
      print(change_info.raw_str(), file)
      with open(file, 'r') as f:
        print(f.read())
```

-----------------------------------------------------------------------------------------------------------                                          

# Python : Watchfiles

<br>

* with just the CLI

```
watchfiles "cat dir1/toto" dir1/
watchfiles "cat dir1/toto" dir1/ --verbosity warning
```
