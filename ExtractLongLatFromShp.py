import sys, os, json
import networkx as nx
import shapefile

def SaveTxt(path, data):
    text_file = open(path, "w")
    for d in data:
        text_file.write(d)
    text_file.close()
def SaveJson(path, data): # "source\\K-town_streetviews.json"
    with open(path, 'w') as f:
        f.write(json.dumps(data, indent=4, ensure_ascii=False, encoding="latin1"))
        f.close()

sf = shapefile.Reader("TN_STTREE_W.shp")
len(list(sf.iterShapes()))
s = sf.shape(7)
shapes = sf.shapes()

#  # 37.566238, 126.966628
#  # Seoul Station  37.555387, 126.971172
x0 =126.971172;
y0 = 37.555387;
R = (y0 -  37.566238) + 2.4;
R2 = R * R;
print "radius: ", R2

locations = []
for i in range(len(shapes)):
    theLong = shapes[i].points[0][0]
    theLat = shapes[i].points[0][1]
    
    dx = theLong - x0
    dy = theLat - y0
    if R2 > ((dx * dx) + (dy*dy) ):
        locations.append(
            {
                "x": theLong,  
                "y": theLat
            }
        )
    # if i > 1000:
    #     break
SaveJson("C:/Users/NJ9/Desktop/loc.json", locations)
print "done"