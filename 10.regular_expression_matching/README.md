# [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)

实现简单的正则匹配函数，支持以下两个控制字符:

- `.` 单个任意字符

- `*` 零个或者更多前面的字符

另外匹配是匹配整个字符串，即完全匹配

## 分析

`.` 比较好处理，`*` 需要穷举去匹配。

最朴素的解法，当遇到 `*` 时，用 match_star 来匹配文本，则有:

```python
def match_star(text, pattern):
    if text[0] in (pattern[0], '.'):
        return match_star(text, pattern[2:]) or match_star(text[1:], pattern)
    else:
        return match_star(text, pattern[2:])
```

上式其实亦等同于：

```python
def match_star(text, pattern):
    return match_star(text, pattern[2:]) or text[0] in (pattern[0], '.') and match_star(text[1:], pattern)
```

而对于整个匹配函数来说，可以归纳为 [solution1.py](solution1.py):

```python
def match(text, pattern):
    if not pattern:
        return len(text) == 0

    first_match = text and pattern[0] in (text[0], '.')

    if len(pattern) >= 2 and pattern[1] == '*':
        return self.isMatch(text, pattern[2:]) or first_match and self.isMatch(text[1:], pattern)
    else:
        return first_match and self.isMatch(text[1:], pattern[1:])
```

对于匹配 `"aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"` 这样的情况，会重复调用 `isMatch` 多次，
假设我们调用的 `isMatch(text[i:], pattern[j:])`，那么对于任意合法 i, j，相同参数的结果是一样的，
故可以设 dp(i, j) 为相应调用的结果，自顶向下或者自底向上得到结果。详见 [solution2.py](solution2.py)

## 总结

- 忽略了匹配 `*` 时字符串为空的情况，例如`isMatch("", "d*")`, `isMatch("a", "ad*")`

- 忘记删掉打印语句导致超时

- 优化递归产生的重复调用
