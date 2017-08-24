package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func (root *ListNode) print() {
	var node *ListNode
	for node = root; node != nil; node = node.Next {
		fmt.Print(node.Val)
		if node.Next != nil {
			fmt.Printf(" -> ")
		}
	}
	fmt.Println()
}

func constructList(numbers []int) *ListNode {
	var root, parent *ListNode
	for index, element := range numbers {
		var node ListNode
		node.Val = element
		if index == 0 {
			root = &node
		} else {
			parent.Next = &node
		}
		parent = &node
	}
	return root
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	i1 := l1
	i2 := l2
	cc := false

	var dummy_head ListNode

	cur := &dummy_head

	for {
		if i1 == nil && i2 == nil && cc == false {
			break
		}

		sum := 0

		if i1 != nil {
			sum += i1.Val
		}

		if i2 != nil {
			sum += i2.Val
		}

		if cc {
			sum += 1
			cc = false
		}

		if sum >= 10 {
			sum -= 10
			cc = true
		}

		cur.Next = &ListNode{Val: sum, Next: nil}
		cur = cur.Next

		if i1 != nil {
			i1 = i1.Next
		}

		if i2 != nil {
			i2 = i2.Next
		}
	}
	return dummy_head.Next
}

func main() {
	a := constructList([]int{1, 8, 9})
	b := constructList([]int{2, 7})
	addTwoNumbers(a, b).print()
}
