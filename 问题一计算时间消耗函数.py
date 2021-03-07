#!/usr/bin/env python
# coding: utf-8

#此代码用于计算fwalk和fmine 因为测试数据过多，未给出测试数据，可以利用函数做测试。得到走路或挖矿的消耗。

weather = [
    2,2,1,0,1,2,0,1,2,2,
    0,2,1,2,2,2,0,0,2,2,
    1,1,2,1,0,2,1,1,2,2
]

w1 = 5
w2 = 8
f1 = 7
f2 = 6
ws = 10
fs = 10

kg1 = 29
kg2 = 36
kg3 = 50


def fwalk(t0,t1,weather):
    count = t0
    kgc = 0
    wc = 0
    fc = 0
    while(count !=t1):
        if(weather[count]==1):
            kgc = kgc + kg1*2
            wc = wc +2*w1
            fc = fc + 2*f1
        elif(weather[count]==2):
            kgc = kgc + kg2*2
            wc = wc +2*w2
            fc = fc + 2*f2
        else:
            kgc = kgc + kg3
            t1 = t1 + 1
            wc = wc +ws
            fc = fc + fs
        count = count + 1
    return t1,kgc,wc,fc


def mine_time(t2,kg,weather):
    while(kg>=0):
        if(weather[t2-1]==1):
            kg = kg - 3*kg1
        elif(weather[t2-1]==2):
            kg = kg - 3*kg2
        else:
            kg = kg - 3*kg3
        print(kg)
        t2 = t2 + 1
    return t2-1


def fmine(t0,t1,weather):
    count = t0
    kgc = 0
    wc = 0
    fc = 0
    while(count !=t1):
        if(weather[count]==1):
            kgc = kgc + kg1*3
            wc = wc +3*w1
            fc = fc + 3*f1
        elif(weather[count]==2):
            kgc = kgc + kg2*3
            wc = wc +3*w2
            fc = fc + 3*f2
        else:
            kgc = kgc + 3*kg3
            #t1 = t1 + 1
            wc = wc +3*ws
            fc = fc + 3*fs
        count = count + 1
    return t1,kgc,wc,fc

