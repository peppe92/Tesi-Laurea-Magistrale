def monta():
	lista=[]
	dt=[0.25/1.2]
	for i in arange(0,19):
	    dt+=[dt[-1]/1.2]
	dt=array(dt)
	for i in arange(0,len(dt)): 
		dts= '{0:.6f}'.format(dt[i])
		nome="forza"+dts+".npy"
		nome_err="errore_"+dts+".npy"
		x,m=np.load(nome)
		x,err=np.load(nome_err)
		lista+=[[x,m,err]]
	#lista=array(lista)
	#return(lista)	
	x,m,err=transpose(lista)
	fill_between(x,m-err,m+err,color=(.7,.7,.7))
	plot(x,m,"-o")
	return x,m,err
