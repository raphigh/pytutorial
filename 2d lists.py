cube_list =[
    [2,3,3],
    [4,8,2],
    [3,5,4],
]
print(cube_list[1][0])
for cube in cube_list:
    result = 1
    for dim in cube:
        result *= dim
    print(result)