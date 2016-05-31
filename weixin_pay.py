"""微信在服务器端下订单接口"""
'''
	tradeNo 为商家自己生成的订单号 						eg  abcdefghigklmn
	body   商品的描述									eg  2瓶水
	money  为商品的价格 ，必须为 int 类型 ，且传字符串  	eg "13
'''
'''下单 并构建给app的参数 '''
def weixinPlaceOrder(tradeNo,body,money):

	order = UnifiedOrder_pub()
	order.setParameter("out_trade_no",tradeNo)
	order.setParameter("body",body)
	order.setParameter("total_fee",money)
	order.setParameter("notify_url","https://www.zcdata.com.cn/jcbpay/ajax/purchase_complete_by_the_third/")
	order.setParameter("trade_type","APP")

	#print order.getResult()
	#第二次签名
	pdb.set_trace()
	tempResult = order.getResult()
	prepayId = tempResult["prepay_id"]
	timeStamp = int(time.time())
	timeStampStr ="{0}".format(timeStamp)
	nonce_str = hashlib.md5(timeStampStr).hexdigest()
	
	dic={}
	dic["appid"] = "wxbc8b2ea585528c56"
	dic["partnerid"] = "1252933401"
	dic["prepayid"] =  prepayId
	dic["package"] = "Sign=WXPay"
	dic["noncestr"] = nonce_str
	dic["timestamp"] = timeStampStr
	dic["sign"] =  getSign(dic)
	print "需要传递给app 发起支付的 参数\n"
	print dic