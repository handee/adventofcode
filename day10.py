
nstart="11"
start="1113122113"
for i in range(0,50):
	counter=1
	prev_value=start[0]
	output=""
	for j in range(1,len(start)):
	      value=start[j]
	      if value==prev_value:
		 counter+=1
	      else:
		 output=output+str(counter)
		 output=output+prev_value
		 counter=1
	      prev_value=value
	output=output+str(counter)
	output=output+value
	start=output

print len(output)
