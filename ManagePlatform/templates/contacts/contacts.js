document.addEventListener("DOMContentLoaded", function() {
    // 获取弹出框元素
	var modal = document.getElementById("myModal");
	
	// 获取打开弹出框的按钮
	var btn = document.getElementById("openModal");
	
	// 获取关闭按钮
	var span = document.getElementsByClassName("close")[0];
	
	// 点击打开弹出框按钮时显示弹出框
	btn.onclick = function() {
	  modal.style.display = "block";
	}
	
	// 点击关闭按钮时隐藏弹出框
	span.onclick = function() {
	  modal.style.display = "none";
	}
	
	// 在用户点击弹出框外部时隐藏弹出框
	window.onclick = function(event) {
	  if (event.target == modal) {
		modal.style.display = "none";
	  }
	}
});