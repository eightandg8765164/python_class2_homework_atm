#!/usr/bin/env python
#coding=utf-8
f=open("ATM.txt","a")
deposit=5000
while deposit>0:
	print '�b��|��%d���s��' %deposit
	f.write('�b��|��%d���s��\n'%deposit)
	withdrawal=input('�аݷQ����h�ֲ{���G')
	f.write('�аݷQ����h�ֲ{���G%d' %withdrawal)
	
	if withdrawal>deposit:
		print '\n'
		f.write('\n')
		print '�z���s�ڤ���'
		f.write('�z���s�ڤ���\n')
	if withdrawal==deposit:
		deposit=deposit-withdrawal
		print '\n'
		f.write('\n')
		print '�w����%d���{��' %withdrawal
		f.write('�w����%d���{��\n' %withdrawal)
		print '�b��L�l�B'
		f.write('�b��L�l�B\n')
	if withdrawal<deposit:
		deposit=deposit-withdrawal
		print '\n'
		f.write('\n')
		print '�w����%d���{��' %withdrawal
		f.write('�w����%d���{��\n' %withdrawal)
		print '�b��Ѿl%d���{��' %deposit
		f.write('�b��Ѿl%d���{��\n' %deposit)
		
	print '----��������@�~����----'
	f.write('----��������@�~����----\n')
f.close()
