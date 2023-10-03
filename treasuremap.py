n1 = [ 1, 1, 1]
n2 = [ 1, 1, 1]
n3 = [ 1, 1, 1]
n = [n1, n2, n3]
position = input("Enter the position yoy want to keep the Hunt location")
print(f" {n1} \n {n2} \n {n3}")
h = int(position[0])
v = int(position[1])
n[h-1][v-1] = "#"
print("The tresure map is ready to show !!! {<>}")
print(f" {n1} \n {n2} \n {n3}")
