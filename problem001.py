import string
import random

def coupon_creator(digit):
	coupon = ''
	for x in range(digit):
		coupon += random.choice(string.ascii_uppercase + string.digits)
		if (x+1)%4==0 and x+1!=digit:
			coupon += '-'
	return coupon;

def two_hundred_coupons():
	data = ''
	count = 1
	for x in range(200):
		digit = 12
		#count +=1
		data += 'coupon number:'+str(count)+' '+coupon_creator(digit)+'\n'
		count +=1
	return data

coupondata = open('coupondata.txt','w')
coupondata.write(two_hundred_coupons())
coupondata.close()

