data	=	{"names":	["Kilho",	"Kilho",	"Kilho",	"Charles",	"Charles"],
			 "year":	[2014,	2015,	2016,	2015,	2016],
			 "points":	[1.5,	1.7,	3.6,	2.4,	2.9]}

df	=	pd.DataFrame(data,	columns=["year",	"names",	"points",	"penalty"],
                  			index=["one",	"two",	"three",	"four",	"five"])
