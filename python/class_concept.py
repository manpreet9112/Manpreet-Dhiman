class student:
	count=0
	
	def profile(self, name, rollno):
		self.name=name
    		self.rollno=rollno
		student.count+=1	
		print ' student no:', student.count 	
		print '\n' 		
 


	def display_profile(self):
		print ' name: ', self.name 
		print ' rollno:', self.rollno
		
	



s1=student()
s2=student()
s1.profile('man',123)
s1.display_profile()
s2.profile('an',121)
s2.display_profile() 
print '\n'
print 'Total student:', student.count
