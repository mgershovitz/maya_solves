package main

import "fmt"

func main() {
	space := ""
	for _, c := range "Hello World" {
		fmt.Println(space + string(c))
		space += " "
	}
}
