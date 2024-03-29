from django.db import models
from utils.models import ModelBase

# Create your models here.
class Tag(ModelBase):
    """
    """

    name = models.CharField(max_length=64, verbose_name="标签名", help_text="标签名")

    class Meta:
        ordering = ['-update_time', '-id']
        db_table = "tb_tag"  # 指明数据库表名
        verbose_name = "新闻标签"  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return self.name

    
class News(ModelBase):
    """
    """
    title = models.CharField(max_length=150, verbose_name="标题", help_text="标题")
    digest = models.CharField(max_length=200, verbose_name="摘要", help_text="摘要")
    content = models.TextField(verbose_name="内容", help_text="内容")
    clicks = models.IntegerField(default=0, verbose_name="点击量", help_text="点击量")
    image_url = models.URLField(default="", verbose_name="图片url", help_text="图片url")
    tag = models.ForeignKey('Tag', on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey('users.Users', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-update_time', '-id']
        db_table = "tb_news"  # 指明数据库表名
        verbose_name = "新闻"  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return self.title


class Comments(ModelBase):
    """
    """
    content = models.TextField(verbose_name="内容", help_text="内容")

    author = models.ForeignKey('users.Users', on_delete=models.SET_NULL, null=True)
    news = models.ForeignKey('News', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-update_time', '-id']
        db_table = "tb_comments"  # 指明数据库表名
        verbose_name = "评论"  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return '<评论{}>'.format(self.id)


class HotNews(ModelBase):
    """
    """
    news = models.OneToOneField('News', on_delete=models.CASCADE)
    priority = models.IntegerField(verbose_name="优先级", help_text="优先级")

    class Meta:
        ordering = ['-update_time', '-id']
        db_table = "tb_hotnews"  # 指明数据库表名
        verbose_name = "热门新闻"  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return '<热门新闻{}>'.format(self.id)


class Banner(ModelBase):
    """
    """
    image_url = models.URLField(verbose_name="轮播图url", help_text="轮播图url")
    priority = models.IntegerField(verbose_name="优先级", help_text="优先级")
    news = models.OneToOneField('News', on_delete=models.CASCADE)

    class Meta:
        ordering = ['priority', '-update_time', '-id']
        db_table = "tb_banner"  # 指明数据库表名
        verbose_name = "轮播图"  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return '<轮播图{}>'.format(self.id)