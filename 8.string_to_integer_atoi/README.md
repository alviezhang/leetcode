# [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)

实现 atoi 函数

## 分析

题目里附加了函数的一些特殊情况处理，一条条列下来分析好再实现。

## 总结

开始解决的时候从后往前遍历，试图遍历的时候顺带把数字转换也做了，但是类似 `  1234qwe1234` 会处理错误。不如正序遍历，先把数字暂存稍后处理。

## 简化逻辑

[solution1.py](solution1.py) 中循环内部判断太多，而且判断的顺序不能改变，非常不易读。
不如改成分步骤的解析，每步自己去循环，如 [solution2.py](solution2.py)
