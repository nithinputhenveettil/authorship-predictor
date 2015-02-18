import os
import sys
import math

def create_analysis(file_name) :
	try :
		file2 = open("analysis.csv","r")
		file2.close()
	except :
		file2 = open("analysis.csv","w")
		a = ","
		a += "Standard Deviation of comas per thousand tokens,"
		a += "Standard Deviation of semicolons per thousand tokens,"
		a += "Standard Deviation of quotation marks per thousand tokens,"
		a += "Standard Deviation of exclamation marks per thousand tokens,"
		a += "Standard Deviation of hyphens per thousand tokens,"
		a += "Standard Deviation of ands per thousand tokens,"
		a += "Standard Deviation of buts per thousand tokens,"
		a += "Standard Deviation of howevers per thousand tokens,"
		a += "Standard Deviation of ifs per thousand tokens,"
		a += "Standard Deviation of thats per thousand tokens,"
		a += "Standard Deviation of mores per thousand tokens,"
		a += "Standard Deviation of musts per thousand tokens,"
		a += "Standard Deviation of mights per thousand tokens,"
		a += "Standard Deviation of thiss per thousand tokens,"
		a += "Standard Deviation of verys per thousand tokens,"
		a += "Standard Deviation of Mean Word Length,"
		a += "Standard Deviation of Mean Sentence Length,"
		a += "Standard deviation of Sentence Length,\n"
		file2.close()
		
	file1 = open("./generated_files/"+file_name,"r")
	#file2 = open("./output/"+file_name,"w")
	file2 = open("analysis.csv","a+")

	a = file_name[:-4]
	a += ","
	novels = file1.read().split("\n")
	novel_data1=[]
	for novel in novels[1:] :
		novel_data1.append(novel.split(","))
	#print novel_data
	
	novel_data = []
	for i in novel_data1[:-1] :
		novel_data.append(i[:-1])
	for i in range(len(novel_data)) :
		for j in range(len(novel_data[i])-1) :
			novel_data[i][j+1] = float(novel_data[i][j+1])
	#print novel_data
	#print
	n1 = len(novel_data[0])
	n2 = len(novel_data)
	
	nv = novels[0].split(",")
	#print nv
	
	for j in range(1,n1) :
		sum1 = 0
		for i in range(n2) :
			sum1 += novel_data[i][j]
		avg = sum1/n2
		#print avg
		count1=0
		for i in range(n2) :
                        t = novel_data[i][j] - avg
                        #print t
			tt = t*t
			count1+=tt
		#print count1
		std_deviation = count1/n2
		#print "Standard deviation of ",nv[j]," = ",
		#print std_deviation
		a += str(std_deviation)+","
	a += "\n"
	file2.write(a)
	file2.close()
	file1.close()




def main() :
	try :
		input_files = os.listdir("generated_files")
	except :
		print "Put your source csv files in a folder named 'generated_files'."
		sys.exit()



	for file_name in input_files :
		create_analysis(file_name)

if __name__ == '__main__' :
	main()
