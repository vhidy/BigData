>>> from datetime import date
		    
>>> now = date.today()
		    
>>> now
		    
datetime.date(2018, 10, 4)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
		    
'10-04-18. 04 Oct 2018 is a Thursday on the 04 day of October.'
>>> birthday = date(1964, 7, 31)
		    
>>> age = now - birthday
		    
>>> age.days
		    
19788
