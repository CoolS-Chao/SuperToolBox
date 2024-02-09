from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import logout
import json
from utils.jsonFormat import json_representation
from utils.messageCode import Code, error_map


# Create your views here.
class LoginView(View):
	def get(self, request):
		return render(request, 'login.html')
    
	def post(self, request):
		json_data = request.body
		if not json_data:
			return json_representation(errno=Code.PARAMERR, errmsg=error_map[Code.PARAMERR])
		# 将json转化为dict
		dict_data = json.loads(json_data.decode('utf8')) # 没有解码，会产生bug
		#form = LoginForm(data=dict_data, request=request)
		# if form.is_valid():
		return json_representation(errmsg="恭喜您，登录成功！")
		# else:
		# 	# 定义一个错误信息列表
		# 	err_msg_list = []
		# 	for item in form.errors.get_json_data().values():
		# 		err_msg_list.append(item[0].get('message'))
		# 	err_msg_str = '/'.join(err_msg_list)  # 拼接错误信息为一个字符串

		# 	return to_json_data(errno=Code.PARAMERR, errmsg=err_msg_str)

        

class LogoutView(View):
    """
    """
    def get(self, request):
        logout(request)

        return redirect(reverse("users:login"))
	

class RankingPersionlistView(View):
	def get(self, request):
		people = [
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
			{'name': 'Nicole Pearson', 'job_title': 'Digital Strategist', 'about': 'Web Designer / UX / Graphic Artist / Coffee Lover', 'address': 'Demo Street 123, Demo City 04312, NJ', 'phone': '+ 800 - 12 12 23 52'},
		]
		return render(request, 'contacts.html', {'people': people})