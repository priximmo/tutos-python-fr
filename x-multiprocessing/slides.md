%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : Multiprocessing

<br>
* objectifs : utiliser tous les cores cpu

```
#!/usr/bin/python3
import multiprocessing
print("CPUs : ", multiprocessing.cpu_count())
```

<br>
* exemple : 

```
def worker(mavar):
    """worker function"""
    print('Worker {}'.format(mavar))
jobs = []
noms = ["Xavier", "Xavki", "Paul"]
for nom in noms:
    p = multiprocessing.Process(target=worker,args=(nom,))
    jobs.append(p)
    p.start()
```

