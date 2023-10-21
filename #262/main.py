if __name__ == "__main__":
    print("Coding problem #262")
    print("This problem was asked by Mozilla.\n"
          "A bridge in a connected (undirected) graph is an edge that, if removed, "
          "causes the graph to become disconnected. Find all the bridges in a graph")

    graph = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "F"), ("E", "G"), ("C", "G"), ("F", "G")]

    for edge in graph:
        queue = []
        visited = []

        start, end = edge
        queue.append(start)

        notFound = True
        while len(queue) > 0 and notFound:
            current = queue[0]
            del queue[0]
            notFound = current != end

            visited.append(current)

            # Get list of connected nodes with the current visited nodes
            for a, b in graph:
                # Case for the starting edge
                if a == start and b == end:
                    continue
                elif a == current and b not in visited:
                    queue.append(b)
                elif b == current and a not in visited:
                    queue.append(a)

        print("Edge: {} - Bridge: {}".format(edge, notFound))
