# Fortunately, every present is a 
# box (a perfect right rectangular prism), 
# which makes calculating the required wrapping 
# paper for each gift a little easier: find the 
# surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. 
# The elves also need a little extra paper for each present: 
# the area of the smallest side.


total = 0
ribbon_total = 0

with open("/Users/plath/GameDev/Code/AOC/AOC15/elvesdata.txt") as f:
    data = f.readlines()

print(data)
# read string l x w x h, delete xs and \n
print("stop__________")

for i in range(len(data)):
    print(f"-----data entry {i}")
    entry = data[i]
    print(f"unedited entry: {entry}")
    cut = len(entry) - 1
    # cutting the linebreaks for every entry except the last one
    if i < len(data)-1:
       entry = entry[:cut]
    print(f"entry without the line break: {entry}")

    #removing the xs from the strings
    entry = entry.replace("x", " ")
    print(f"entry without the xs: {entry}")

    #writing the result back to the data
    data[i] = entry
    print(f"final rewritten entry without the xs: {data[i]}")

    #splitting the strings into sub-lists
    dimensions_list = entry.split(" ")
    print(f"extracted list of dimentions: {dimensions_list}")
    length, width, height = 0, 0, 0

    print(f"declaring variables --- length: {length}, width: {width}, height: {height}")
    for k in range(len(dimensions_list)):
        if k == 0:
            length = int(dimensions_list[k])

        if k == 1:
            width = int(dimensions_list[k])

        if k ==2:
            height = int(dimensions_list[k])

    print(f"writing values --- length: {length}, width: {width}, height: {height}")
    dimensions_hi = max([length, width, height])
    print(f"maximum of the three sides: {dimensions_hi}")
    ribbon_length = 2 * (length + width + height - dimensions_hi) + length * width * height
    print(f"The ribbon length for this package is: {ribbon_length}")

# surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. 
    sidea = length*width
    print(f"side a area: {sidea}")
    sideb = width*height
    print(f"side b area: {sideb}")
    sidec = height*length
    print(f"side c area: {sidec}")

    sided = min([sidea, sideb, sidec])
    print(f"side d area: {sided}")

    total += 2*sidea + 2*sideb + 2*sidec + sided
    ribbon_total += ribbon_length
    print(f"current total: {total}")
    print(f"current ribbon total: {ribbon_total}")
    print("")

    # A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present 
    # plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
    
  
#print(data)

print(f"The elves need {total} square feet of wrapping paper!!")
print(f"The elves need {ribbon_total} feet of ribbon!!")
