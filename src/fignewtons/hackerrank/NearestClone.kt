package fignewtons.hackerrank

import java.util.*

/*
https://www.hackerrank.com/challenges/find-the-nearest-clone
 */
data class Graph (val edges: Map<Int, Set<Int>>,
                  val nodes: Map<Int, Int>,
                  val colors: Map<Int, Set<Int>>) {

  class Builder(nodes: Int) {

    private val edges: Map<Int, MutableSet<Int>> =
      (1..nodes).associateWith { mutableSetOf<Int>() }

    private val nodes: MutableMap<Int, Int> = mutableMapOf()
    private val colors: MutableMap<Int, MutableSet<Int>> = mutableMapOf()

    fun edge(e: Pair<Int, Int>) {
      edges.getValue(e.first).add(e.second)
      edges.getValue(e.second).add(e.first)
    }

    fun colors(nodeColors: Array<Int>) {
      for (i in 0 until nodeColors.size) {
        nodes[i + 1] = nodeColors[i]
        colors.computeIfAbsent(nodeColors[i]) { mutableSetOf() }.add(i + 1)
      }
    }

    fun build() = Graph(edges, nodes, colors)
  }

}


fun nearestClone(graph: Graph, color: Int): Int {

  val visited: Map<Int, Array<Boolean>> = (1..graph.nodes.size).associateWith { Array(graph.nodes.size) { false } }
  var round = 0

  val queue = ArrayDeque<Pair<Int, Int>>()
  for (node in graph.colors.getValue(color))
    queue.add(node to node)
  queue.add(0 to 0)

  while (queue.isNotEmpty()) {

    val (start, current) = queue.pop()

    if (start == 0 && current == 0) {
      round++
      if (queue.isNotEmpty())
        queue.add(0 to 0)
    } else {
      visited.getValue(start)[current - 1] = true
      if (start != current && graph.nodes[current] == color)
        return round

      for (neighbor in graph.edges.getValue(current)) {
        if (!visited.getValue(start)[neighbor - 1]) {
          queue.add(start to neighbor)
        }
      }
    }

  }

  return -1
}


fun main() {

  val builder = Graph.Builder(5)
  val edges = listOf(
    1 to 2,
    1 to 3,
    2 to 4,
    3 to 5
  )
  for (edge in edges)
    builder.edge(edge)

  builder.colors(arrayOf(1, 2, 3, 3, 2))
  val graph = builder.build()

  println(nearestClone(graph, 2))
}
