list = [1, 2, 3, 4, 5, 6, 7]
list1 = []
for ea in list:
	list1.append([])
print(list1)

list2 = []
for ea in range(0,252):
	list2.append(ea)
# print(list2)

counter = 0
for ea in list2:
	if counter == 0:
		print("<tr>")
		print("        <td>", ea, "</td>")
		counter += 1
	elif counter % 7 != 0:
		print("        <td>", ea, "</td>")
		counter += 1	
	else:
		print("</tr>")
		print("<tr>")
		print("        <td>", ea, "</td>")
		counter += 1
print("</tr>")
print("mod", 0%7)
