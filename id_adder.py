#!/usr/bin/env python3
import traceback
import argparse
import json

def get_ids(flname):
	"""
	Open a file and get ids from it
	"""
	with open(flname, "r") as fl:
		lines = fl.read().splitlines()
	out = []
	comment = ""
	for line in lines:
		if not line: #Skip empty lines
			continue
		if line[0] == "#": #Comments
			comment = line
			continue
		out.append([line[-11:], comment])
		comment = ""
	return out

def main():
	parser = argparse.ArgumentParser(description="Add/remove video ids and print them")
	parser.add_argument("--plus", dest="add", nargs="+", metavar="FILE", help="Files with ids to add", required=False)
	parser.add_argument("--minus", dest="remove", nargs="+", metavar="FILE", help="Files with ids to remove", required=False)
	parser.add_argument("--no-comments", dest="nocomments", action="store_true", help="Files with ids to remove")
	args = parser.parse_args()

	blacklist = []
	output = []

	if args.remove:
		for i in args.remove:
			vids = get_ids(i)
			for vid in vids:
				blacklist.append(vid[0])
	
	if args.add:
		for i in args.add:
			vids = get_ids(i)
			for vid in vids:
				if vid[0] not in blacklist:
					output.append(vid)
					blacklist.append(vid[0])
	
	for i in output:
		if(args.nocomments):
			print("https://youtube.com/watch?v={}".format(i[0]))
		else:
			if(i[1] != ""):
				print(i[1])
			print("https://youtube.com/watch?v={}".format(i[0]))
			print()

if(__name__ == "__main__"):
	try:
		main()
	except (KeyboardInterrupt, SystemExit, GeneratorExit):
		pass
	except:
		traceback.print_exc()
