def find_max(data: list) -> int:

  if	data == None or len(data) == 0: 
    return None
  if	len(data) == 1: 
	  return data[0]
  
  mid = len(data)//2 
  max1 = find_max(data[0:mid]) 
  max2 = find_max(data[mid:]) 
  
  return max(max1,max2)


datos = [3,7,1,9,2,0,2,6,3]

print ("El mayor valor es {}".format(find_max(datos)))