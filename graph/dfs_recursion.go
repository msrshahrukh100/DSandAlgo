package main

import "fmt"

type Graph struct {
	graph map[int][]int
}

var g Graph

func addEdge(u int, v int) {
	g.graph[u] = append(g.graph[u], v)
}

func dfsUtil(v int, visited []bool) {
	visited[v] = true
	fmt.Println(v)

	for _, i := range g.graph[v] {
		if !visited[i] {
			dfsUtil(i, visited)
		}
	}
}

func printGraph() {
	for k, v := range g.graph {
		fmt.Println(k, " --> ", v)
	}
}

func dfs(v int, numberOfNodes int) {
	visited := make([]bool, numberOfNodes)
	dfsUtil(v, visited)
}

func main() {
	g.graph = make(map[int][]int)
	addEdge(0, 1)
	addEdge(0, 2)
	addEdge(1, 2)
	addEdge(2, 0)
	addEdge(2, 3)
	addEdge(3, 3)
	printGraph()
	fmt.Println("Following is DFS from (starting from vertex 2)")
	dfs(2, 4)
}
