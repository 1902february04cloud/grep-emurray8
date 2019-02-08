#!/usr/bin/env python3
def main():
	with  open('cities.txt') as f:
		for line in f:
			line = line.strip()
			reverse = line[::-1]
			if line.lower() == reverse.lower():
				print(line)
if __name__ == '__main__':
	main()
