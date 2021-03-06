1.python wrapper for ls command
	#!/usr/bin/env python
	import subprocess
	subprocess.call(["ls", "-l"])
2.System information script
	#!usr/bin/env python
	#System Information Gathering Script
	import subprocess
	#Command1
	uname = 'uname'
	uname_arg = '-a'
	print "Gathering system information with %s command:\n" % uname
	subprocess.call([uname, uname_arg])
	#Command2
	diskspace = 'df'
	diskspace_arg = '-h'
	print "Gathering diskspace imformation %s command:\n" % diskspace
	subprocess.call([diskspace, diskspace_arg])
3.shell vs python
	shell(1):
		for ((i=0; i<5; i++))
		do
			echo $i
		done
	shell(2):
		for i in `seq 0 4`
		do
			echo $i
		done
	python:
		for i in range(5):
			print i
4.Converted Pythoon systeminfo into script: pysysinfo_func.py
Note:the result will output when you type the command "import pysysinfo_func",the solution is that adding a statement (if__name__ == "__main__") beyond the main() 
	#!/usr/bin/env python
	import subprocess

	#command 1
	def uname_func():
		uname = "uname"
		uname_arg = "-a"
		print "Gathering system information with %s command:\n" % uname
		subprocess.call([uname, uname_arg])
	#command 2
	def disk_func():
		diskspace = "df"
		diskspace_arg = "-h"
		print "Gathering system information with %s command:\n" % diskspace
		subprocess.call([diskspace, diskspace_arg])
	
	#Main function that call other functions
	def main():
		uname_func()
		disk_func()
	(if __name__ == "__main__")
     main()

5.Converted Bash system info script: bashsysinfo_func.sh
	#!/usr/bin/env bash
	#Command 1
	function uname_func()
	{
		UNAME="uname -a"  #notice that between UNAME and equal without blank,otherwise will cause a error! 
		print "Gathering system information with $UNAME command:\n\n"
		$UNAME
	}
	function main()
	{
		uname_func
	}

	main

	