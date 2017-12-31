from graph_tool.all import *
import os
g=Graph(directed=False)
vprop = g.new_vertex_property("string")
v={}
with open("/home/uditennam/Rutgers/can_citations.txt",'r') as f:
#with open("/home/uditennam/testtext.txt",'r') as f:
  i = 0
  e = []
  for line in f.readlines():
    if i==30000:
        break;
    i += 1
    line=line.split("\t")
    x=int(line[0])
    y=int((line[1].split("\n"))[0])
    if x==0 or y==0:
      pass
    else:
      if x not in v.keys():
          v[x] = g.add_vertex()
          vprop[v[x]] = str(x)
      if y not in v.keys():
          v[y] = g.add_vertex()
          vprop[v[y]] = str(y)
      if [y,x] not in e:
          g.add_edge(v[x],v[y])
          e.append([x,y])
  g.vertex_properties["name"]=vprop
  print(g.vertex_index)
  graph_draw(g, vertex_text=g.vertex_properties["name"],output_size=(1000, 700), output="test.png", vertex_font_size=5)
  print("done")
       

