import json

# get the curveShape that we want
curveData = []
vertexes = cmds.ls(sl = True, fl = True)
for vertex in vertexes:
    position = cmds.xform(vertex, q = True, translation = True)
    curveData.append(position)

print(curveData)


filePath = "C:\\Users\\Yourim Kim\\Documents\\maya\\2022\\scripts\\mayaTools\\curveShapeData.json"

with open(filePath, "w") as json_file:
    json.dump(curveData, json_file, sort_keys = True, indent=4)


