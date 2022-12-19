# The first part of the code is similar to the code found in the notes since we were allowed to use that code
import csv

# This part open the CSV file for it to be read
with open('hierholzer-test1.txt', 'r') as csv_file:
    file_handle = csv.reader(csv_file)
    data = next(file_handle)
    
txt_output = open("test3_output.txt", "w")

# Reads the number of vertices
number_of_vertices = int(data[0])
# Starts the total edges at 0 to start counting
graph = [[0 for i in range(number_of_vertices)] for j in range(number_of_vertices)]
edges = []
k = 0

# Puts the matrix into something that can be analyzed
for i in range(0, number_of_vertices):
    for j in range(0, number_of_vertices):
        k += 1
        graph[i][j] = int(data[k])
        if int(data[k]) != 0:
            edges.append([int(data[k]),i,j])

# Sorts the edges based on the weight
edges.sort()

# Finds the total edges with the duplicates
total_edges = len(edges)

# These are the variables that I will use later in the algorithm
current_number_of_edges = 0
current_cycles = 1
current_edges_used = []
last_vertex_used = []
total_cycles = []
current_cycle_output =[]
start_of_cycle = edges[0][1]

# I hard code the first edge and print that edge
current_edges_used.append([edges[0][1], edges[0][2]])
print("Adding Edge: " + str([edges[0][1], edges[0][2]]))
txt_output.write("Adding Edge: " + str([edges[0][1], edges[0][2]]))
txt_output.write("\n")
current_edges_used.append([edges[0][2], edges[0][1]])
current_cycle_output.append(edges[0][1]) 
current_cycle_output.append(edges[0][2]) 
last_vertex_used.append(edges[0][2])
# I add two rather than one because my algorithm counts duplicates
current_number_of_edges = current_number_of_edges + 2

# Checks to see if all of the edges are touched before breaking out of the loop
while (current_number_of_edges < total_edges):
    # Starts from the second edge since we hard coded the first ome
    i = 1
    while (i < total_edges):
        # Sets the current edge up to be used
        current_edge = edges[i]
        current_start_vertex = current_edge[1]
        current_end_vertex = current_edge[2]
        current_edge = [current_start_vertex, current_end_vertex]
        # Need to find the inverse edge along with the original edge
        current_inverse_edge= [current_end_vertex, current_start_vertex]
        # Checks to see if the start vertex is the last vertex used
        if (current_start_vertex == last_vertex_used[-1]):
            # Checks to see if the edge has not already been used
            if (not(current_edge in current_edges_used)):
                # Adds the edge and resets some of the variables
                last_vertex_used.append(current_end_vertex)
                current_cycle_output.append(current_end_vertex)
                current_edges_used.append(current_edge)
                current_edges_used.append(current_inverse_edge)
                current_number_of_edges = current_number_of_edges + 2
                print("Adding Edge: " + str(current_edge))
                txt_output.write("Adding Edge: " + str(current_edge))
                txt_output.write("\n")
                # Reset i to iterate all the way through
                i = 0
                # This is to see if the end of the cycle is found
                if(current_end_vertex == start_of_cycle):
                    total_cycles.append(current_cycle_output)
                    print("Cycle Found: " + str(current_cycle_output))
                    print("\n")
                    txt_output.write("Cycle Found: " + str(current_cycle_output))
                    txt_output.write("\n")
                    txt_output.write("\n")
                    # Resets the cycle to find the next one
                    current_cycle_output = []
                    g = 0
                    # This is used to find the next edge we should use to start a sycle
                    while (g < total_edges):
                        # Sets up the variables
                        next_edge = edges[g]
                        next_start_vertex = next_edge[1]
                        next_end_vertex = next_edge[2]
                        next_edge = [next_start_vertex, next_end_vertex]
                        next_inverse_edge = [next_end_vertex, next_start_vertex]
                        # Make sure that edge has not been used
                        if (not(next_edge in current_edges_used)):
                            # Makes sure the vertex is in the used vertices
                            if(next_start_vertex in last_vertex_used):
                                # Adds the edge and resets the process
                                current_cycles = current_cycles + 1
                                start_of_cycle = next_start_vertex
                                last_vertex_used.append(next_end_vertex)
                                current_cycle_output.append(next_start_vertex)
                                current_cycle_output.append(next_end_vertex)
                                current_edges_used.append(next_edge)
                                current_edges_used.append(next_inverse_edge)
                                current_number_of_edges = current_number_of_edges + 2
                                print("Adding Edge: " + str(next_edge))
                                txt_output.write("Adding Edge: " + str(next_edge))
                                txt_output.write("\n")
                                # Resets i 
                                i = 0
                                break
                            else:
                                g = g + 1
                        else:
                            g = g + 1
        i = i + 1
        
# This prints the number of edges left
print("Edges Left: " + str(total_edges - current_number_of_edges))
txt_output.write("Edges Left: " + str(total_edges - current_number_of_edges))
txt_output.write("\n")
# This prints the total number of cycles found
print(str(current_cycles) + " cycles found")
txt_output.write(str(current_cycles) + " cycles found")
txt_output.write("\n")

# Puts the cycles together to make a eularian circuit
for h in range(1, len(total_cycles)):
    first_index = total_cycles[h][0]
    first_cycle_find = total_cycles[0].index(first_index)
    total_cycles[0] = total_cycles[0][0:first_cycle_find] + total_cycles[h][0:len(total_cycles[h]) -1] + total_cycles[0][first_cycle_find:]

# This prints the eularian circuit
print("The Eularian circuit is: " + str(total_cycles[0]))
txt_output.write("\n")
txt_output.write("The Eularian circuit is: " + str(total_cycles[0]))

txt_output.close()