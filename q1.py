# 2019 codejam q1

def split(N):
	stringN = str(N)
	stringA = ""
	stringB = ""
	for c in stringN:
		if c != "4":
			stringA += c
			stringB += "0"
		else:
			stringA += "2"
			stringB += "2"
	stringB = str(int(stringB))
	return stringA + " " + stringB


T = int(input())
for x in range(1,T+1):
	output = "Case #" + str(x) +": " +split(int(input()))
	print(output)

