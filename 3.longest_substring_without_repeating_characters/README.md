# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## 题目

寻找最长没有重复字母的子串，例

    "abcabcbb" => "abc"
    "bbbbb" => "b"
    "pwwkew" => "wke"

## 分析

用 Hash 表记录已经出现过的字母。

解决过程：

- 先是在循环内使用 Hash 表，失败了即从出现重复的字符处重新寻找

- 只用一个 Hash 表，通过查看字符第一次出现的位置来判断是否在该循环出现

## 总结

出现的错误：

- 低级编码错误
