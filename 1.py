def function (ls):
	n = len(ls)
	for x in range(n +1):
		if x not in ls:
			return x


if __name__ == "__main__":
	ls = [3,0,1]
	print(function(ls))
