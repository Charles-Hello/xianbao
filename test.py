
import pyhttpx
 
sess = pyhttpx.HttpSession()
r = sess.get('https://httpbin.org/get', headers={'User-Agent': '3301'}, cookies={'k': '3301'})
print(r.status_code)
print(r.request.raw)