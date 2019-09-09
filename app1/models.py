# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
import uuid  # Required for unique book instances


class UserIPInfo(models.Model):
    ip = models.CharField(max_length=400, default='', verbose_name=u'ip地址', null=True)
    time = models.DateTimeField(verbose_name=u'更新时间', auto_now=True)
    port = models.CharField(max_length=10000, default='', verbose_name=u'端口信息', null=True)

    class Meta:
        verbose_name = u'用户访问地址信息表'
        verbose_name_plural = verbose_name
        db_table = "useripinfo"


class BrowseInfo(models.Model):
    useragent = models.CharField(max_length=10000, default='', verbose_name=u'用户浏览器信息', null=True)
    ip = models.CharField(max_length=2560, verbose_name=u'唯一设备ID', default="")
    uip = models.CharField(max_length=256, verbose_name=u'IP', default="")

    # port = models.CharField(max_length=10000, default='', verbose_name=u'端口信息', null=True)

    ip = models.ForeignKey("UserIPInfo", on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'用户浏览器信息表'
        verbose_name_plural = verbose_name
        db_table = "browseinfo"

    def get_absolute_url(self):
        return reverse('user_ip', args=[self.uip])

    def __str__(self):
        return self.uip


# 图书系统模型
class MyModelName(models.Model):
    # 名字字段
    my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")

    class Meta:
        # 查询模型返回的记录默认排序字段
        ordering = ["-my_field_name"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.my_field_name


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    # 书名
    title = models.CharField(max_length=200)
    # 作者
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    # 日期
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    # 书本唯一编号
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.id, self.book.title)


class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)


class K_USER(models.Model):
    """
    Model representing an k_user.
    """
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    logintime = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.username, self.username)
