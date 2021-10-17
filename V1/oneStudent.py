import subprocess
import os 

def compileOneTime( studentID ) :
	#make dir
	try:
		subprocess.check_output(["mkdir",studentID])
	except:
		NIL = 0
	
	#copy code
	#subprocess.check_output(["cp", "Dockerfile", studentID+"/"])
	subprocess.check_output(["cp", studentID+".cpp", studentID+"/"])

	#change dir
	#wd = os.getcwd()
	newDir = "./"+studentID
	os.chdir(newDir)

	#make Dockerfile
	personDockerfile = open("Dockerfile", mode="w")
	personDockerfile.write("FROM gcc\nWORKDIR /\nCOPY ")
	personDockerfile.write(studentID)
	personDockerfile.write(".cpp ./\nRUN  g++ -o temp ")
	personDockerfile.write(studentID)
	personDockerfile.write(".cpp \ \n    && ./temp")
	personDockerfile.close()

	#run dockerfile and return
	returnOutput = subprocess.check_output("sudo docker build -t "+studentID+"image"+" . --no-cache", shell=True)
	returnOutput=returnOutput.decode("utf-8")
	returnOutput=returnOutput.split("Removing") #student out put can't have Removing
	returnOutput=returnOutput[-2]
	returnOutput=returnOutput[192:]
	output=returnOutput
	print(returnOutput)

	#find image
	imageIDwithName = subprocess.check_output("sudo docker images --format \"{{.ID}}: {{.Repository}}\" | grep "+studentID+"image | cut -d\" \" -f2", shell=True)
	imageIDwithName=imageIDwithName[:-1] #"...\n"
	imageIDwithName=imageIDwithName.decode("utf-8")
	#print(imageIDwithName)

	#kill image
	subprocess.check_output("sudo docker rmi "+imageIDwithName, shell=True)
	
	#change dir
	os.chdir("/home/cycuigopher/桌面/10977030-test")
	
	return output
