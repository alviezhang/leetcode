package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestIsMatch(t *testing.T) {
	assert.Equal(t, isMatch("aa", "a"), false)
	assert.Equal(t, isMatch("aa", "aa"), true)
	assert.Equal(t, isMatch("aaa", "aa"), false)
	assert.Equal(t, isMatch("aa", "a*"), true)
	assert.Equal(t, isMatch("aa", ".*"), true)
	assert.Equal(t, isMatch("ab", ".*"), true)
	assert.Equal(t, isMatch("aab", "c*a*b"), true)
	assert.Equal(t, isMatch("abcd", "d*"), false)
	assert.Equal(t, isMatch("a", "ad*"), true)
	assert.Equal(t, isMatch("", "d*"), true)
	assert.Equal(t, isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"), false)
}
