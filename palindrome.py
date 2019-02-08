#!/usr/bin/env python3
def main():
	fh = open('cities.txt')
	for line in fh:
		line = line.strip()
		reverse = line[::-1]
		if line.lower() == reverse.lower():
			print(line)
	fh.close()
if __name__ == '__main__':
	main()
