import os
import sys

path = os.path.dirname(os.path.realpath(sys.argv[0]))

class Training() :
	def __init__(self) :
		self.noa = 0
		self.author_names = []
		self.train_data = []
		self.author_files = os.listdir(path+"/generated_files")
		#print author_names
		for author in self.author_files :
			text1 = open(path+"/generated_files/"+author,"r").read().split("\n")
			#print text1[1:-1]
			for txt in text1[1:-1] :
				t = []
				t.append(self.noa) 
				for i in txt.split(",")[1:-1] :
					t.append(i)
				self.train_data.append(t)
			self.noa += 1
		print self.train_data
			


def main() :
	t = Training()

if __name__ == '__main__' :
	main()
