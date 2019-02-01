#!/bin/env python3

import sys
import os
import git

# add root file for git repos
def spider_dir_tree():
	return os.getcwd().split("/")[1:]
	#go to git dir
	#list dir
	#go from list to dir

a = spider_dir_tree()

def gen_list(list_to_cut, to_find):
	for i in range(len(list_to_cut)):
		yield list_to_cut[i]
		i+=1
		if list_to_cut[i] == to_find:
			break

def get_path_to_dir(to_dir):
	return [next(genlist(spider_dir_tree(),to_dir))]

print(a)
print(get_path_to_dir("git"))

def git_pull_request():
	print(os.listdir())
	g = git.cmd.Git(os.getcwd())
	g.pull()
	# there is a dir with name .git, try pull request

def main():
	pass
	#spider_dir_tree(git_pull_request())

if __name__ == "__main__":
	main()
	git_pull_request()
	print(spider_dir_tree())
	
