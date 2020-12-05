def b2d(s):
  dec = 0
  for chr in s:
    dec = (dec*2+1) if (chr=='B' or chr=='R') else dec*2
  return dec
#print("Test ",b2d("BFFFBBFRRR"),"=567")
#print("Test ",b2d("FFFBBBFRRR"),"=119")
#print("Test ",b2d("BBFFBBFRLL"),"=820")

found_seats=[]
#avail_seats=[i for i in range(1024)]
input = open('day5/input.txt','r')
for line in input:
  s=b2d(line.strip())
  found_seats.append(s)
#  avail_seats.remove(s)

a=min(found_seats); b=max(found_seats)
seat_sum=(a+b)*(b-a+1)/2
my_seat=int(seat_sum-sum(found_seats))

print(max(found_seats),my_seat)

input.close()