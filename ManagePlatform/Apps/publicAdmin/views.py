from django.shortcuts import render
from django.views import View

class IndexView(View):
    """ create admin index view"""
    def get(self,request):
        return render(request, 'index.html')
    

class CelebrityListView(View):
    """名人榜视图"""
    def get(self,request):
        return render(request, 'contacts.html')


# # Create your views here.
# import json
# from django.shortcuts import render
# from django.views import View
# from django.db.models import Count

# from news import models
# from utils.json_fun import to_json_data
# from utils.res_code import Code,error_map


# class IndexView(View):
#     """ create admin index view"""
#     def get(self,request):
#         return render(request,'admin/index/index.html')


# class TagManageView(View):
#     """
#     route: /admin/tags/
#     """
#     def get(self,request):
#         tags = models.Tag.objects.values('id','name').annotate(num_news = Count('news')).filter(is_delete=False).\
#             order_by('-num_news','update_time')
#         return render(request,'admin/news/tag_manage.html',locals())

#     def post(self,request):
#         """"""
#         json_data = request.body
#         if not json_data:
#             return to_json_data(errno=Code.PARAMERR, errmsg=error_map[Code.PARAMERR])
#         # 将json转化为dict
#         dict_data = json.loads(json_data.decode('utf8'))
#         tag_name = dict_data.get('name')
#         if tag_name:
#             tag_name = tag_name.strip()
#             tag_tuple = models.Tag.objects.get_or_create(name=tag_name)
#             tag_instance, tag_boolean = tag_tuple
#             news_tag_dict = {
#                 'id':tag_instance.id,
#                 'name':tag_instance.name
#             }
#             return to_json_data(errmsg='标签创建成功',data=news_tag_dict) if tag_boolean else to_json_data(errno=Code.DATAEXIST,errmsg='标签名已存在!')
#         else:
#             return to_json_data(errno=Code.PARAMERR,errmsg='标签名为空!')




# class TagEditView(View):
#     """
#     /admin/tags/<int:tag_id>/
#     """
#     def delete(self,request,tag_id):
#         tag = models.Tag.objects.only('id').filter(id=tag_id).first()
#         if tag:
#             tag.is_delete = True
#             tag.save(update_fields=['is_delete'])
#             return to_json_data(errmsg='标签删除成功!')
#         else:
#             return to_json_data(errno=Code.PARAMERR,errmsg="需要删除的标签不存在")

#     def put(self,request,tag_id):
#         json_data = request.body
#         if not json_data:
#             return to_json_data(errno=Code.PARAMERR, errmsg=error_map[Code.PARAMERR])
#         # 将json转化为dict
#         dict_data = json.loads(json_data.decode('utf8'))

#         tag_name = dict_data.get('name')
#         tag = models.Tag.objects.only('name').filter(id=tag_id).first()
#         if tag:
#             if tag_name:
#                 tag_name = tag_name.strip()
#                 if not models.Tag.objects.only('id').filter(name=tag_name).exists():
#                     tag.name = tag_name
#                     tag.save(update_fields=['name'])
#                     return to_json_data(errmsg='标签更新成功!')
#                 else:
#                     return to_json_data(errno=Code.PARAMERR, errmsg='需要更新的标签已存在!')
#         else:
#             return to_json_data(errno=Code.PARAMERR, errmsg='需要更新的标签不存在!')


# logger = logging.getLogger('django')

# class HotNewsManageView(View):
#     """"""
#     def get(self,request):
#         hot_news = models.HotNews.objects.select_related('news__tag').\
#             only('news_id','news__title','news__tag__name','priority').\
#             filter(is_delete=False).order_by('priority','-news__clicks')[:constants.SHOW_HOTNEWS_COUNT]
#         return render(request,'admin/news/news_hot.html',locals())


# class HotNewsEditView(View):
#     """"""
#     def delete(self,request,hotnews_id):
#         hotnews= models.HotNews.objects.only('id').filter(id=hotnews_id).first()
#         if hotnews:
#             hotnews.is_delete = True
#             hotnews.save(update_fields = ['is_delete'])
#             return to_json_data(errmsg='热门文章删除成功!')
#         else:
#             return to_json_data(errno=Code.PARAMERR,errmsg='需要删除的热门文章不存在!')

#     def put(self, request, hotnews_id):
#         json_data = request.body
#         if not json_data:
#             return to_json_data(errno=Code.PARAMERR, errmsg=error_map[Code.PARAMERR])
#         # 将json转化为dict
#         dict_data = json.loads(json_data.decode('utf8'))
#         try:
#             priority = int(dict_data.get('priority'))
#             priority_list = [i for i,_ in models.HotNews.PRI_CHOICES ]
#             if priority not in priority_list:
#                 return to_json_data(errno=Code.PARAMERR, errmsg='热门文章优先级设置错误!')
#         except Exception as e:
#             logger.info('热门文章优先级异常:\n{}'.format(e))
#             return to_json_data(errno=Code.PARAMERR,errmsg='热门文章优先级设置错误!')

#         hotnews = models.HotNews.objects.only('id').filter(id=hotnews_id).first()
#         if not hotnews:
#             return to_json_data(errno=Code.PARAMERR, errmsg='需要更新的热门文章不存在!')
#         if hotnews.priority == priority:
#             return to_json_data(errno=Code.PARAMERR, errmsg='热门文章的优先级未改变!!')

#         hotnews.priority = priority
#         hotnews.save(update_fields = ['priority'])
#         return to_json_data(errmsg='热门文章更新成功!')


# class HotNewsAddView(View):
#     """
#     /admin/hotnews/add
#     """
#     def get(self,request):
#         tags = models.Tag.objects.values('id','name').annotate(num_news = Count('news')).filter(is_delete=False).\
#             order_by('-num_news','update_time')
#         priority_dict  = dict(models.HotNews.PRI_CHOICES)
#         return render(request,'admin/news/news_hot_add.html',locals())

#     def post(self,request):
#         json_data = request.body
#         if not json_data:
#             return to_json_data(errno=Code.PARAMERR, errmsg=error_map[Code.PARAMERR])
#         # 将json转化为dict
#         dict_data = json.loads(json_data.decode('utf8'))

#         try:
#             news_id = int(dict_data.get('news_id'))
#         except Exception as e:
#             logger.info('热门文章:\n{}'.format(e))
#             return to_json_data(errno=Code.PARAMERR, errmsg='参数错误')

#         if not models.News.objects.filter(id=news_id).exists():
#             return to_json_data(errno=Code.PARAMERR, errmsg='文章不存在')

#         try:
#             priority = int(dict_data.get('priority'))
#             priority_list = [i for i, _ in models.HotNews.PRI_CHOICES]
#             if priority not in priority_list:
#                 return to_json_data(errno=Code.PARAMERR, errmsg='热门文章的优先级设置错误')
#         except Exception as e:
#             logger.info('热门文章优先级异常：\n{}'.format(e))
#             return to_json_data(errno=Code.PARAMERR, errmsg='热门文章的优先级设置错误')

#         # 创建热门新闻
#         hotnews_tuple = models.HotNews.objects.get_or_create(news_id=news_id)
#         hotnews, is_created = hotnews_tuple
#         hotnews.priority = priority  # 修改优先级
#         hotnews.save(update_fields=['priority'])
#         return to_json_data(errmsg="热门文章创建成功")



# class NewsByTagIdView(View):
#     '''
#     /admin/tags/<int:tag_id>/
#     '''
#     def get(self,request,tag_id):
#         newses = models.News.objects.values('id','title').filter(is_delete=False,tag_id=tag_id)
#         news_list = [i for i in newses]

#         return to_json_data(data={
#             'news':news_list
#         })