#!/usr/bin/env python
#coding=utf-8
f=open("ATM.txt","a")
deposit=5000
while deposit>0:
	print '帳戶尚有%d元存款' %deposit
	f.write('帳戶尚有%d元存款\n'%deposit)
	withdrawal=input('請問想提領多少現金：')
	f.write('請問想提領多少現金：%d' %withdrawal)
	
	if withdrawal>deposit:
		print '\n'
		f.write('\n')
		print '您的存款不足'
		f.write('您的存款不足\n')
	if withdrawal==deposit:
		deposit=deposit-withdrawal
		print '\n'
		f.write('\n')
		print '已提領%d元現金' %withdrawal
		f.write('已提領%d元現金\n' %withdrawal)
		print '帳戶無餘額'
		f.write('帳戶無餘額\n')
	if withdrawal<deposit:
		deposit=deposit-withdrawal
		print '\n'
		f.write('\n')
		print '已提領%d元現金' %withdrawal
		f.write('已提領%d元現金\n' %withdrawal)
		print '帳戶剩餘%d元現金' %deposit
		f.write('帳戶剩餘%d元現金\n' %deposit)
		
	print '----本次提領作業結束----'
	f.write('----本次提領作業結束----\n')
f.close()
