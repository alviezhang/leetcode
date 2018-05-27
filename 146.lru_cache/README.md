# [146. LRU Cache](https://leetcode.com/problems/lru-cache/)

## 分析

LRU 特点:

1. 大小固定

2. 被访问的节点会被置顶

满足以上条件，需要满足

1. get(key) O(1)

2. put(key, value) O(1)

由于 set, get 均为 O(1), 所以要用 Hash 表来定位 key。另外需要解决的就是如何淘汰过期的 key, 比较容易想到的是使用优先队列，这样的话 get, set 时间复杂度变成了 O(lgN) 不符合题意。

所以我们需要一个这样的数据结构来存储数据:

1. 找到最近、最久的时间复杂度是 O(1)
2. 调整节点的时间复杂度 O(1)

显然，双向链表满足以上需求。综合前面的判断，可以写一个结合 HashTab 和 LinkList 的结构，可以写出时间复杂度为 O(1) 的 LRUCache。


## 总结

1. 因为链表的小错误出错
