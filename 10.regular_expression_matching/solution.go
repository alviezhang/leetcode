package main

import "fmt"

const DOT = '.'
const STAR = '*'

func isMatch(s string, p string) bool {
	return match(s, p, 0, 0)
}

func match(s string, p string, s_pos int, p_pos int) bool {
	//fmt.Printf("match(%s, %s, %d, %d)\n", s, p, s_pos, p_pos)

	if s_pos >= len(s) && p_pos >= len(p) {
		return true
	}

	if p_pos >= len(p) {
		return false
	}

	if p_pos+1 < len(p) && p[p_pos+1] == STAR {
		return match_star(s, p, s_pos, p_pos+1)
	}

	if s_pos >= len(s) {
		return false
	}

	if s[s_pos] == p[p_pos] || p[p_pos] == DOT {
		return match(s, p, s_pos+1, p_pos+1)
	}
	return false
}

func match_star(s string, p string, s_pos int, p_pos int) bool {
	//fmt.Printf("match_star(%s, %s, %d, %d)\n", s, p, s_pos, p_pos)
	// patter error
	if p_pos == 0 {
		//fmt.Println("pattern error")
		return false
	}
	previous := p[p_pos-1]

	for i := s_pos; i < len(s); i++ {
		if previous == DOT || s[i] == previous {
			if match(s, p, i+1, p_pos+1) {
				return true
			}
		} else {
			break
		}
	}
	return match(s, p, s_pos, p_pos+1)
}

func main() {
	fmt.Println(isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
}
