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
	
