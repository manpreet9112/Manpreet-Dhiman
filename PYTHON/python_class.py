"""@package docstring
   Documentation for this module
   more detail """


class student:
        """documentation for class
        variable initialisation"""
	count=0
	

	def profile(self, name, rollno):
               """documentation for function
                accessing input variables through self.""" 
		self.name=name
    		self.rollno=rollno
		student.count+=1
               """display student number."""	
		print ' student no:', student.count 	
		print '\n' 		
 

	def display_profile(self):
                """function for showing output"""
		print ' name: ', self.name 
		print ' rollno:', self.rollno
		
	


"""class object created"""
s1=student()
s2=student()
"""accessing functions using objects."""
s1.profile('man',123)
s1.display_profile()
s2.profile('an',121)
s2.display_profile() 
print '\n'
"""show total students.""" 
print 'Total student:', student.count
