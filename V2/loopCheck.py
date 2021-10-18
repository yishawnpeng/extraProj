import subprocess
import os 
import sys
import traceback

def compileOneTime(studentID ) :
	#make dir
	try:
		subprocess.check_output(["mkdir",studentID])
	except:
		NIL = 0


	#copy code
	subprocess.check_output(["cp", studentID+".cpp", studentID+"/"])

	#change dir
	newDir = "./"+studentID
	os.chdir(newDir)

	#run docker container
	try: #compile OK
		#complie
		subprocess.check_output("gcc "+studentID+ ".cpp 2>  err1.txt", shell=True,stderr=subprocess.STDOUT ,timeout = 5)
		print("compile OK")
		
		#run it 
		child = subprocess.Popen("docker run --rm -it --ulimit cpu=1 -v ./docker_gcc/:/usr/src/myapp gcc-test:v1 ./a > result.txt",shell=True)
		child.wait()
		print("execute OK")
		
		#read result
		f = open('result.txt', 'r')
		returnOutput = f.read()
		print(returnOutput)
		
		#change to father dir 
		os.chdir("/V2")
		
		#return result
		return(returnOutput)		
		
	except Exception as e: #compile fail
		error_class = e.__class__.__name__ #error type 
		detail = e.args[0] #detail
		cl, exc, tb = sys.exc_info() #Call Stack
		lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
		
		if (error_class=="TimeoutExpired") :
			returnOutput = "Runtime Error!"
		else:
			returnOutput = e
			print ("exception")
			f = open('err1.txt', 'r')
			returnOutput = f.read()
			f.close()
			
		#change to father dir 
		os.chdir("/V2")
		
		#delete dir
		subprocess.check_output("rm -r /V2/"+studentID , shell=True ) #forceddd
		
		#return result
		return(returnOutput)	

if __name__=="__main__" :
	ans = compileOneTime("10977030")
	print(ans)