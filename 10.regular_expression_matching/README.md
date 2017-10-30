# [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)

实现简单的正则匹配函数，支持以下两个控制字符:

- `.` 单个任意字符

- `*` 零个或者更多前面的字符

另外匹配是匹配整个字符串，即完全匹配

## 分析

`.` 特殊处理，`*` 写一个函数去匹配

## 总结

- 忽略了匹配 `*` 时字符串为空的情况，例如`isMatch("", "d*")`, `isMatch("a", "ad*")`

- 忘记删掉打印语句导致超时
