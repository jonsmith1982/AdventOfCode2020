
highest = 0
mySeatID = range(240, 807)

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

f = open("challenge-05-12-2020.txt", "r")  
for x in f:
  
  x = x.rstrip()
  
  if (x[0] == 'F'):
    row = range(0,64)
  else :
    row = range(64,128)
    
  if (x[1] == 'F'):
    row = chunkIt(row, 2)[0]
  else :
    row = chunkIt(row, 2)[1]
  
  if (x[2] == 'F'):
    row = chunkIt(row, 2)[0]
  else :
    row = chunkIt(row, 2)[1]
  
  if (x[3] == 'F'):
    row = chunkIt(row, 2)[0]
  else :
    row = chunkIt(row, 2)[1]
  
  if (x[4] == 'F'):
    row = chunkIt(row, 2)[0]
  else :
    row = chunkIt(row, 2)[1]
  
  if (x[5] == 'F'):
    row = chunkIt(row, 2)[0]
  else :
    row = chunkIt(row, 2)[1]
  
  if (x[6] == 'F'):
    row = chunkIt(row, 2)[0]
  else :
    row = chunkIt(row, 2)[1]

  if (x[7] == 'L'):
    column = range(0, 4)
  else :
    column = range(4, 8)
  
  if (x[8] == 'L'):
    column = chunkIt(column, 2)[0]
  else :
    column = chunkIt(column, 2)[1]
    
  if (x[9] == 'L'):
    column = chunkIt(column, 2)[0]
  else :
    column = chunkIt(column, 2)[1]
  
  seatID = row[0] * 8 + column[0]
  if (seatID > highest):
    highest = seatID
  #print(str(row[0]) + ' ' + str(column[0]) + ' ' + str(seatID))
  
  if (seatID in mySeatID):
    mySeatID.remove(seatID)
  
f.close()

print(mySeatID)

