# My proposed solution
pd.melt(frame=students, \
	    id_vars=['full_name', 'gender_age', 'grade'], \
	    value_vars=['fractions', 'probability'], \
	    value_name='score', \
	    var_name='exam')

students = pd.melt(frame=students, \
	               id_vars=['full_name','gender_age','grade'], \
	               value_vars=['fractions', 'probability'], \
	               value_name='score', \
	               var_name='exam')