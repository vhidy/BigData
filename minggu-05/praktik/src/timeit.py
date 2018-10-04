>>> from timeit import Timer
		    
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
		    
0.03929218400026002
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
		    
0.03342259999999442
