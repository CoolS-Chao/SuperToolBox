document.addEventListener("DOMContentLoaded", function () {
	// 在页面加载完成后执行的代码
	let loginForm = document.querySelector('.form-contain');

	loginForm.addEventListener('submit', function (e) {
		// 阻止默认提交操作
		e.preventDefault();

		let sUserAccount = document.querySelector("input[name=email]").value;
		let sPassword = document.querySelector("input[name=password]").value;
		// 获取用户是否勾许"记住我", 勾许为true, 不勾许为false
		let bStatus = document.getElementById("remember").checked;

		if (sUserAccount === "") {
			alert('用户账号不能为空');
			return;
		}

		if (!sPassword) {
			alert('密码不能为空');
			return;
		}

		if (sPassword.length < 6 || sPassword.length > 20) {
			alert('密码的长度需在6~20位以内');
			return;
		}

		// 创建请求参数
		let SdataParams = {
			"user_account": sUserAccount,
			"password": sPassword,
			"remember_me": bStatus
		};

		// 创建一个新的 XMLHttpRequest 对象
		let xhr = new XMLHttpRequest();
		// 配置请求
		xhr.open("POST", "/login/", true);
		xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
		// 处理请求的回调函数
		xhr.onreadystatechange = function () {
			if (xhr.readyState === XMLHttpRequest.DONE) {
				if (xhr.status === 200) {
					let res = JSON.parse(xhr.responseText);
					if (res.errno === "0") {
						alert('恭喜你, 登录成功!');
						setTimeout(function () {
							// 登录成功之后重定向到打开登录页面之前的页面
							window.location.href = document.referrer;
						}, 1000);
					} else {
						alert(res.errmsg);
					}
				} else {
					alert('服务器出错, 请重试!');
				}
			}
		};

		xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
		xhr.send(JSON.stringify(SdataParams));
	});

	// getCookie/csrfSafeMethod 函数与 AJAX 请求一起使用, 在请求时处理 CSRF 保护和获取必要的 cookie.
	function getCookie(name) {
		let cookieValue = null;
		if (document.cookie && document.cookie !== '') {
			let cookies = document.cookie.split(';');
			for (let i = 0; i < cookies.length; i++) {
				let cookie = cookies[i].trim();
				if (cookie.substring(0, name.length + 1) === (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}
	function csrfSafeMethod(method) {
		return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
	}
});
