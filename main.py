#!/bin/env python3

import sys
import os
import git

# add root file for git repos
def spider_dir_tree():
	return os.getcwd().split("/")[:]

def root_path(to_item):
	list_to_cut = spider_dir_tree()
	items = (it for k,it in enumerate(list_to_cut) if to_item in list_to_cut[k:])
	return "/".join(list(items))


# traverse root directory, and list directories as dirs and files as files
def walk_dir(path_root):
    return [ root.split(os.sep) for root, dirs, files in os.walk(path_root) ]

def git_pull_request(path_list):
	path_git = "/".join(path_list)
	g = git.cmd.Git(path_git)
	g.pull()
	print(path_git)


def main(list_a):
	no_failures = 0
	path_fail = []
	list_a = [i[:-1] for i in list_a if i[-1] == ".git"  ]
	for path_a in list_a:
		try:
			git_pull_request(path_a)
		except:	
			no_failures += 1
			path_fail.append(path_a)
			print("git pull origin master for","/".join(path_a),"was unsuccessful.")
			pass
	print("Failures to pull:",no_failures,":\n","\n".join("/".join(i) for i in path_fail))
	#spider_dir_tree(git_pull_request())

if __name__ == "__main__":
	walk_dir(root_path(sys.argv[1]))
	main(walk_dir(root_path(sys.argv[1])))
	
