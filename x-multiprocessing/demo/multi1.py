#!/usr/bin/python3
import multiprocessing

def worker(mavar):
    """worker function"""
    print('Worker {}'.format(mavar))
jobs = []
noms = ["Xavier", "Xavki", "Paul"]
for nom in noms:
    p = multiprocessing.Process(target=worker,args=(nom,))
    jobs.append(p)
    p.start()


