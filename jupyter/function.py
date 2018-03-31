import math

__base32 = '0123456789bcdefghjkmnpqrstuvwxyz'
__decodemap = { }
for i in range(len(__base32)):
    __decodemap[__base32[i]] = i
del i

def rad(tude):
    return (math.pi/180.0)*tude

#产出欧式距离

def produceLocationInfo(latitude1, longitude1,latitude2, longitude2):
    radLat1 = rad(latitude1)
    radLat2 = rad(latitude2)
    a = radLat1-radLat2
    b = rad(longitude1)-rad(longitude2)
    R = 6378137
    d = R*2*math.asin(math.sqrt(math.pow(math.sin(a/2),2)+math.cos(radLat1)*math.cos(radLat2)*math.pow(math.sin(b/2),2)))
    detallat = abs(a)*R
    detalLon = math.sqrt(d**2-detallat**2)
    if b==0:
        direction = 1/2 if a*b>0 else -1/2
    else:
        direction = math.atan(detallat/detalLon*(1 if a*b>0 else -1))/math.pi
    return round(d)

#返回 精确的经纬度和误差
def decode_exactly(geohash):
    lat_interval, lon_interval = (-90.0, 90.0), (-180.0, 180.0)
    lat_err, lon_err = 90.0, 180.0
    is_even = True
    for c in geohash:
        cd = __decodemap[c]
        for mask in [16, 8, 4, 2, 1]:
            if is_even: # adds longitude info
                lon_err /= 2
                if cd & mask:
                    lon_interval = ((lon_interval[0]+lon_interval[1])/2, lon_interval[1])
                else:
                    lon_interval = (lon_interval[0], (lon_interval[0]+lon_interval[1])/2)
            else:      # adds latitude info
                lat_err /= 2
                if cd & mask:
                    lat_interval = ((lat_interval[0]+lat_interval[1])/2, lat_interval[1])
                else:
                    lat_interval = (lat_interval[0], (lat_interval[0]+lat_interval[1])/2)
            is_even = not is_even
    lat = (lat_interval[0] + lat_interval[1]) / 2
    lon = (lon_interval[0] + lon_interval[1]) / 2
    return lat, lon, lat_err, lon_err


#返回 曼哈顿距离

def getManhattan(hotStartLocation,hotEndLocation):
    
    R = 6378137
    #当纬度差是0
    latitude1 = decode_exactly(hotStartLocation)[0]
    longitude1 = decode_exactly(hotStartLocation)[1]
    
    latitude2 = decode_exactly(hotStartLocation)[0]
    longitude2 = decode_exactly(hotEndLocation)[1]
    
    radLat1 = rad(latitude1)
    radLat2 = rad(latitude2)
    a = radLat1-radLat2
    b = rad(longitude1)-rad(longitude2)
    d1 = R*2*math.asin(math.sqrt(math.pow(math.sin(a/2),2)+math.cos(radLat1)*math.cos(radLat2)*math.pow(math.sin(b/2),2)))

    #当经度差是0
    latitude1 = decode_exactly(hotStartLocation)[0]
    longitude1 = decode_exactly(hotStartLocation)[1]
    
    latitude2 = decode_exactly(hotEndLocation)[0]
    longitude2 = decode_exactly(hotStartLocation)[1]
    
    radLat1 = rad(latitude1)
    radLat2 = rad(latitude2)
    a = radLat1-radLat2
    b = rad(longitude1)-rad(longitude2)
    d2 = R*2*math.asin(math.sqrt(math.pow(math.sin(a/2),2)+math.cos(radLat1)*math.cos(radLat2)*math.pow(math.sin(b/2),2)))

    #曼哈顿距离
    return round(d1+d2)
    

#得到欧式距离

def loc_2_dis(hotStartLocation,hotEndLocation):
    StartLocation = decode_exactly(hotStartLocation[:7])
    EndLocation = decode_exactly(hotEndLocation[:7])
    latitude1 = StartLocation[0]
    longitude1 = StartLocation[1]
    latitude2 = EndLocation[0]
    longitude2 = EndLocation[1]
    return produceLocationInfo(latitude1, longitude1, latitude2, longitude2)


#方向，正北是0
def getDegree(StartLocation,EndLocation):  
    """ 
    Args: 
        point p1(latA, lonA) 
        point p2(latB, lonB) 
    Returns: 
        bearing between the two GPS points, 
        default: the basis of heading direction is north 
    """  
    
    lat1 = decode_exactly(StartLocation)[0]
    long1 = decode_exactly(StartLocation)[1]
    
    lat2 = decode_exactly(EndLocation)[0]
    long2 = decode_exactly(EndLocation)[1]
    
    radLat1 = rad(lat1)  
    radLon1 = rad(long1)  
    radLat2 = rad(lat2)  
    radLon2 = rad(long2)  
    dLon = radLon2 - radLon1  
    y = math.sin(dLon) * math.cos(radLat2)  
    x = math.cos(radLat1) * math.sin(radLat2) - math.sin(radLat1) * math.cos(radLat2) * math.cos(dLon)  
    brng = math.degrees(math.atan2(y, x))  
    brng = (brng + 360) % 360  
    return brng  



#geohash的漂移，找到当前点的周围的邻居
oddarr = ["bcfguvyz","89destwx","2367kmqr","0145hjnp"]

evenarr = [
     "prxz",
     "nqwy",
     "jmtv",  
     "hksu",
     "57eg",
     "46df",
     "139c",
     "028b"]

arr = {"odd":oddarr,"even":evenarr }

ass = {"odd":[3,7],"even":[7,3]}#行,列

def getposition(center,length):
    
    last = center[length - 1]
    
    if length%2==0:#偶数
        for i in range(8):
            for j in range(4):
                if evenarr[i][j] == last:
                    row = i
                    col = j
                    return "even",row,col
    else:#奇数
        for i in range(4):
            for j in range(8):
                if oddarr[i][j] == last:
                    row = i
                    col = j
                    return "odd",row,col

def calculate(center,length,position):
    
    odd_even,row,col = getposition(center,length)#找到奇偶和row,col位置
    
    if position == "left":
        if 0 <= col-1:
            center = center[0:length -1] + arr[odd_even][row][col - 1] + center[length:]
            return center
        else:
            center = center[0:length -1] + arr[odd_even][row][ass[odd_even][1]] + center[length:]
    
    elif position == "right":
        if col+1 <= ass[odd_even][1]:
            center = center[0:length -1] + arr[odd_even][row][col + 1] + center[length:]
            return center
        else:
            center = center[0:length -1] + arr[odd_even][row][0] + center[length:]
            
    elif position == "top":
        if 0 <= row - 1:
            center = center[0:length -1] + arr[odd_even][row - 1][col] + center[length:]
            return center
        else:
            center = center[0:length -1] + arr[odd_even][ass[odd_even][0]][col] + center[length:]
            
    elif position == "bottom":
        if row + 1 <= ass[odd_even][0]:
            center = center[0:length -1] + arr[odd_even][row + 1][col] + center[length:]
            return center
        else:
            center = center[0:length -1] + arr[odd_even][0][col] + center[length:]
            
            
    elif position == "leftbottom":
        
        center = calculate(center,length,"bottom")
        
        center = calculate(center,length,"left")
        
        return center
            
    
    elif position == "rightbottom":
        
        center = calculate(center,length,"bottom")
        
        center = calculate(center,length,"right")
        
        return center
            
    elif position == "rightop":
        
        center = calculate(center,length,"top")
        
        center = calculate(center,length,"right")
        
        return center
    
    elif position == "leftop":
        
        center = calculate(center,length,"top")
        
        center = calculate(center,length,"left")
        
        return center
    
    
    if 0 < length - 1:
        return calculate(center,length - 1,position)
    else:
        return ""
    

def getNeighbors(center):
    
    neighbor = []
    
    length = len(center)#最后一个字符的位置
    
    left = calculate(center,length,"left")
    right = calculate(center,length,"right")
    top = calculate(center,length,"top")
    bottom = calculate(center,length,"bottom")
    
    leftbottom = calculate(center,length,"leftbottom")
    rightbottom = calculate(center,length,"rightbottom")
    lefttop = calculate(center,length,"leftop")
    rightop = calculate(center,length,"rightop")
    
    neighbor.append(left)
    neighbor.append(right)
    neighbor.append(lefttop)
    neighbor.append(top)
    
    neighbor.append(rightop)
    neighbor.append(leftbottom)
    neighbor.append(bottom)
    neighbor.append(rightbottom)
    
    return neighbor

def getAll_node_nei():
    #get all node

    node_list = set()
    i = 0
    csv_reader = csv.reader(open('./data/train_hard.csv', encoding='utf-8'))
    for row in csv_reader:
        i+=1
        if i == 1:
            continue
        node_list.add(row[5])
        node_list.add(row[6])

    i = 0
    csv_reader = csv.reader(open('./data/test_hard.csv', encoding='utf-8'))
    for row in csv_reader:
        i+=1
        if i == 1:
            continue
        node_list.add(row[5])
    node_nei = {}

    for node in node_list:
        temp = getNeighbors(node)
        temp.append(node)
        node_nei[node] = temp
    return node_nei
