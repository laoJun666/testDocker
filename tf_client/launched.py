#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
该脚本作为镜像启动的第一个脚本，负责将启动时传入的参数传递给项目，并启动项目；
意义在于简化镜像启动命令，镜像启动只需要传入集群参数即可不需要关心启动的具体脚本
"""

import sys
import os  

WORKSPACE =  os.environ.get('KD_WORKSPACE')
TARGETFILE = os.environ.get('KD_TARGET_FILE')

if __name__ == '__main__':

	t_file = TARGETFILE

	print(TARGETFILE)
	print(t_file[0])

	# if t_file[0] != '/':
	# 	t_file = './' + t_file
	# else:
	# 	t_file = '.' + t_file

	if t_file[0] != '/':
		t_file = '/' + t_file


	project_path = WORKSPACE + t_file
	exceStr = ""

	if project_path[0] != '/':
		exceStr = "/"

	argString=""
	# print(sys.argv[1:])
	for arg in sys.argv[1:]:
		argString += "\t\"%s\"" % (arg)

	exceStr =  "python" + "\t" +  exceStr + project_path + "\t" + argString
	os.system("echo exceStr ->  %s" % (exceStr))
	os.system(exceStr)

# for arg in sys.argv[1:]:
 #   		 print arg  

