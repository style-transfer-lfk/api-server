from bottle import route, run

@route('/hello')
def hello():
	return "Hello World!"
@route('/style/seurat')
def seurat():
	f = open('/home/ec2-user/filter-mode','w')
	f.write('seurat')
	f.close()

@route('/style/composition')
def seurat():
	f = open('/home/ec2-user/filter-mode','w')
	f.write('composition')
	f.close()

@route('/style/original')
def seurat():
	f = open('/home/ec2-user/filter-mode','w')
	f.write('original')
	f.close()

@route('/style/hokusai')
def seurat():
	f = open('/home/ec2-user/filter-mode','w')
	f.write('hokusai')
	f.close()

@route('/style/kandinsky')
def seurat():
	f = open('/home/ec2-user/filter-mode','w')
	f.write('kandinsky')
	f.close()

run(host='0.0.0.0', port=8080, debug=True)
