import os

for root, dirs, files in os.walk('.'):
	for f in files:
		if f.endswith('.ui'):
			os.system('pyuic4 -o ui_%s.py %s' % (f.rsplit('.', 1)[0], os.path.join(root,f)))
		elif f.endswith('.qrc'):
			print f
			os.system('pyrcc4 -o %s_rc.py %s' % (f.rsplit('.', 1)[0], os.path.join(root,f)))