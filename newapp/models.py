#-*- coding: UTF-8 -*-
from django.db import models
# Create your models here.
import json
country_choices1 = (
(0, '--- Country ---'), (1, 'United States'), (2, 'United Kingdom'), (3, 'Australia'), (4, 'Canada'), (5, 'France'),
(6, 'New Zealand'), (7, 'India'), (8, 'Brazil'), (9, 'Afghanistan'), (10, 'Aland Islands'), (11, 'Albania'),
(12, 'Algeria'), (13, 'American Samoa'), (14, 'Andorra'), (15, 'Angola'), (16, 'Anguilla'), (17, 'Antarctica'),
(18, 'Antigua and Barbuda'), (19, 'Argentina'), (20, 'Armenia'), (21, 'Aruba'), (22, 'Austria'), (23, 'Azerbaijan'),
(24, 'Bahamas'), (25, 'Bahrain'), (26, 'Bangladesh'), (27, 'Barbados'), (28, 'Belarus'), (29, 'Belgium'),
(30, 'Belize'), (31, 'Benin'), (32, 'Bermuda'), (33, 'Bhutan'), (34, 'Bolivia'), (35, 'Bosnia and Herzegovina'),
(36, 'Botswana'), (37, 'British Indian Ocean Territory'), (38, 'Brunei Darussalam'), (39, 'Bulgaria'),
(40, 'Burkina Faso'), (41, 'Burundi'), (42, 'Cambodia'), (43, 'Cameroon'), (44, 'Cape Verde'), (45, 'Cayman Islands'),
(46, 'Central African Republic'), (47, 'Chad'), (48, 'Chile'), (49, 'China'), (50, 'Colombia'), (51, 'Comoros'),
(52, 'Democratic Republic of the Congo'), (53, 'Republic of the Congo'), (54, 'Cook Islands'), (55, 'Costa Rica'),
(56, 'Cote dIvoire'), (57, 'Croatia'), (58, 'Cuba'), (59, 'Cyprus'), (60, 'Czech Republic'), (61, 'Denmark'),
(62, 'Djibouti'), (63, 'Dominica'), (64, 'Dominican Republic'), (65, 'East Timor'), (66, 'Ecuador'), (67, 'Egypt'),
(68, 'El Salvador'), (69, 'Equatorial Guinea'), (70, 'Eritrea'), (71, 'Estonia'), (72, 'Ethiopia'),
(73, 'Faroe Islands'), (74, 'Fiji'), (75, 'Finland'), (76, 'Gabon'), (77, 'Gambia'), (78, 'Georgia'), (79, 'Germany'),
(80, 'Ghana'), (81, 'Gibraltar'), (82, 'Greece'), (83, 'Grenada'), (84, 'Guatemala'), (85, 'Guinea'),
(86, 'Guinea-Bissau'), (87, 'Guyana'), (88, 'Haiti'), (89, 'Honduras'), (90, 'Hong Kong'), (91, 'Hungary'),
(92, 'Iceland'), (93, 'Indonesia'), (94, 'Iran'), (95, 'Iraq'), (96, 'Ireland'), (97, 'Israel'), (98, 'Italy'),
(99, 'Jamaica'), (100, 'Japan'), (101, 'Jordan'), (102, 'Kazakhstan'), (103, 'Kenya'), (104, 'Kiribati'),
(105, 'North Korea'), (106, 'South Korea'), (107, 'Kuwait'), (108, 'Kyrgyzstan'), (109, 'Laos'), (110, 'Latvia'),
(111, 'Lebanon'), (112, 'Lesotho'), (113, 'Liberia'), (114, 'Libya'), (115, 'Liechtenstein'), (116, 'Lithuania'),
(117, 'Luxembourg'), (118, 'Macedonia'), (119, 'Madagascar'), (120, 'Malawi'), (121, 'Malaysia'), (122, 'Maldives'),
(123, 'Mali'), (124, 'Malta'), (125, 'Marshall Islands'), (126, 'Mauritania'), (127, 'Mauritius'), (128, 'Mexico'),
(129, 'Micronesia'), (130, 'Moldova'), (131, 'Monaco'), (132, 'Mongolia'), (133, 'Montenegro'), (134, 'Morocco'),
(135, 'Mozambique'), (136, 'Myanmar'), (137, 'Namibia'), (138, 'Nauru'), (139, 'Nepal'), (140, 'Netherlands'),
(141, 'Netherlands Antilles'), (142, 'Nicaragua'), (143, 'Niger'), (144, 'Nigeria'), (145, 'Norway'), (146, 'Oman'),
(147, 'Pakistan'), (148, 'Palau'), (149, 'Palestine'), (150, 'Panama'), (151, 'Papua New Guinea'), (152, 'Paraguay'),
(153, 'Peru'), (154, 'Philippines'), (155, 'Poland'), (156, 'Portugal'), (157, 'Puerto Rico'), (158, 'Qatar'),
(159, 'Romania'), (160, 'Russia'), (161, 'Rwanda'), (162, 'Saint Kitts and Nevis'), (163, 'Saint Lucia'),
(164, 'Saint Vincent and the Grenadines'), (165, 'Samoa'), (166, 'San Marino'), (167, 'Sao Tome and Principe'),
(168, 'Saudi Arabia'), (169, 'Senegal'), (170, 'Serbia'), (171, 'Seychelles'), (172, 'Sierra Leone'),
(173, 'Singapore'), (174, 'Slovakia'), (175, 'Slovenia'), (176, 'Solomon Islands'), (177, 'Somalia'),
(178, 'South Africa'), (179, 'Spain'), (180, 'Sri Lanka'), (181, 'Sudan'), (182, 'Suriname'), (183, 'Swaziland'),
(184, 'Sweden'), (185, 'Switzerland'), (186, 'Syria'), (187, 'Taiwan'), (188, 'Tajikistan'), (189, 'Tanzania'),
(190, 'Thailand'), (191, 'Togo'), (192, 'Tonga'), (193, 'Trinidad and Tobago'), (194, 'Tunisia'), (195, 'Turkey'),
(196, 'Turkmenistan'), (197, 'Tuvalu'), (198, 'Uganda'), (199, 'Ukraine'), (200, 'United Arab Emirates'),
(201, 'United States Minor Outlying Islands'), (202, 'Uruguay'), (203, 'Uzbekistan'), (204, 'Vanuatu'),
(205, 'Vatican City'), (206, 'Venezuela'), (207, 'Vietnam'), (208, 'Virgin Islands, British'),
(209, 'Virgin Islands, U.S.'), (210, 'Yemen'), (211, 'Zambia'), (212, 'Zimbabwe'))
intention_school_choices1=(('0','---院校---'),)
academic_interest_choices = ((0, '--- acdemic interest ---'), (1, 'Artificial Intelligence'), (2, 'Biocomputation'),
                             (3, 'Computer and Network Security'), (4, 'Human Computer Interaction'),
                             (5, 'Information Management and Analytics'), (6, 'Mobile and Internet Computing'),
                             (7, 'Real World Computing'), (8, 'Software Theory'), (9, 'Systems'),
                             (10, 'Theoretical Computer Science'))
graduate_school_choices = (('0','---毕业院校---'),)
major_choice=((0,'---专业---'),('EE','电子工程'),('CS','计算机科学'))
recommendation_choice=((1,'你的推荐者认识对方教授'),(2,'你的推荐者不认识对方教授'))
talentStudent_choice=((1,'是'),(2,'否'))
country_choices=(('0','---国家---'),('USA','美国'),('ENG','英国'),('CAN','加拿大'),('AUS','澳大利亚'))
highcountry_choice=(('0','---国家---'),('USA','美国'))#
highcountry_choice_uk=(('0','---国家---'),('ENG','英国'),('USA','美国'),('CAN','加拿大'))
highcountry_choice_ca=(('0','---国家---'),('ENG','英国'),('USA','美国'),('CAN','加拿大'))
ranking_choices=(('0','---专业排名---'),('top 5%','top 5%'),('top 10%','top 10%'),('top 30%','top 30%'),('top 50%','top 50%'))

def get_IntentionSchool():
    intention_school_choices1 = [('0', '---院校---')]
    for obj in University.objects.all():
        print(obj.id,obj.name)
        intention_school_choices1 = intention_school_choices1 + [(int(obj.gu_level), obj.name)]
    return intention_school_choices1


def get_GraduateSchool():
    graduate_school_choices = [('0', '---毕业院校---')]
    for obj in GraduateUniver.objects.raw('SELECT *from newapp_graduateuniver ORDER BY CONVERT(name USING gbk)'):
        graduate_school_choices = graduate_school_choices + [(obj.name, obj.name)]
    return graduate_school_choices

def get_HighSchool():
    highschool_choices = [('0', '---毕业院校---')]
    for obj in highSchool.objects.raw('SELECT *from newapp_highschool ORDER BY CONVERT(name USING gbk)'):
        highschool_choices = highschool_choices + [(obj.name, obj.name)]
    return highschool_choices


class Student(models.Model):
    name = models.CharField(max_length=32)
    age = models.CharField(max_length=20)
    score = models.CharField(max_length=32)

class StuInfo(models.Model):
    # basic information
    first_name_1 = models.CharField(max_length=20)
    last_name_1 = models.CharField(max_length=20)
    cell_phone_number = models.CharField(max_length=40)

    # Intention country,university and major
    intention_country = models.CharField(choices=country_choices, default=0,max_length=20)
    intention_school = models.IntegerField(choices=intention_school_choices1, default=0)
    academic_interest = models.IntegerField(choices=academic_interest_choices, default=0)

    # education history
    graduate_school = models.IntegerField(choices=graduate_school_choices, default=0)
    GPA = models.FloatField(max_length=10)
    IELFS_TOEFL = models.IntegerField(max_length=20)
    GRE_Total = models.IntegerField(max_length=20)
    GRE_VR = models.IntegerField(max_length= 20)
    GRE_QR =models.IntegerField(max_length=20)
    GRE_AW = models.IntegerField(max_length=20)
    In_Papers = models.IntegerField(max_length=20)
    Na_Papers = models.IntegerField(max_length=20)
    In_Patents = models.IntegerField(max_length=20)
    Na_Patents = models.IntegerField(max_length=20)
    Research = models.CharField(max_length=32)
    Placement = models.CharField(max_length=32)
    Social_Practice = models.CharField(max_length=32)
    Specilty = models.CharField(max_length= 32)
    # Recommendation
    Recommendation = models.CharField(max_length=32)

# 美国大学
class University(models.Model):
    name = models.CharField(max_length=32)
    level = models.IntegerField(max_length=32)
    sublevel = models.IntegerField(max_length=32)
    gu_level = models.IntegerField(max_length=32)
    rank_major = models.IntegerField(max_length=32)
    rank_total = models.IntegerField(max_length=32)
    country = models.CharField(max_length=32)
    major = models.CharField(max_length=32)
    category_level = models.IntegerField(max_length=32)

# 加拿大大学
class University_Ca(models.Model):
    name = models.CharField(max_length=32)
    level = models.IntegerField(max_length=32)
    sublevel = models.IntegerField(max_length=32)
    gu_level = models.IntegerField(max_length=32)
    rank_major = models.IntegerField(max_length=32)
    rank_total = models.IntegerField(max_length=32)
    country = models.CharField(max_length=32)
    major = models.CharField(max_length=32)
    category_level = models.IntegerField(max_length=32)

# 英国大学
class University_En(models.Model):
    name = models.CharField(max_length=32)
    level = models.IntegerField(max_length=32)
    sublevel = models.IntegerField(max_length=32)
    gu_level = models.IntegerField(max_length=32)
    rank_major = models.IntegerField(max_length=32)
    rank_total = models.IntegerField(max_length=32)
    country = models.CharField(max_length=32)
    major = models.CharField(max_length=32)
    category_level = models.IntegerField(max_length=32)

#澳洲大学
class University_Au(models.Model):
    name = models.CharField(max_length=32)
    level = models.IntegerField(max_length=32)
    sublevel = models.IntegerField(max_length=32)
    gu_level = models.IntegerField(max_length=32)
    rank_major = models.IntegerField(max_length=32)
    rank_total = models.IntegerField(max_length=32)
    country = models.CharField(max_length=32)
    major = models.CharField(max_length=32)
    category_level = models.IntegerField(max_length=32)

# 毕业院校
class GraduateUniver(models.Model):
    name = models.CharField(max_length=32)
    high = models.IntegerField(max_length=32)
    gu_level = models.IntegerField(max_length=32)
    gu_category = models.IntegerField(max_length=32)
    low = models.CharField(max_length=32)
    level = models.CharField(max_length=32)

class UserInfoFormModel(models.Model):
    first_name=models.CharField(verbose_name=u'姓',max_length=20,blank=True,null=True)#姓可以空白，可以为空值
    last_name=models.CharField(verbose_name=u'名',max_length=20,blank=True,null=True)#名可以空白，可以为空值
    cell_phone_number=models.CharField(u'电话',max_length=40) #电话必须要写

    intention_country=models.CharField(verbose_name=u'目标国家',max_length=20,choices=country_choices,default='0')#意向国家一定要写，默认为---国家---
    #intention_school=models.CharField(max_length=20,blank=True,choices=get_IntentionSchool())
    intention_school = models.CharField(verbose_name=u'目标院校',max_length=20, blank=True,null=True) #意向学校可以不选，可以为空白，可以空值
    intention_major=models.CharField(verbose_name=u'目标专业',choices=major_choice,default='0',max_length=20) #意向的专业一定要选，默认为---专业---
    graduate_school = models.CharField(verbose_name=u'毕业院校',choices=get_GraduateSchool(), default='0', max_length=20,blank=False,null=False) #毕业院校一定要选,不能为空

    ranking_in_major=models.CharField(verbose_name=u'专业排名',max_length=20,choices=ranking_choices,default='0')#专业排名一定要选

    score_GPA=models.FloatField(verbose_name=u'GPA',max_length=20) #GPA一定要填写，不能为空

    #雅思托福成绩一定要写，不能为空
    score_IELTS_TOEFL=models.FloatField(verbose_name=u'雅思/托福',max_length=20)
    score_IT_Listening=models.FloatField(verbose_name=u'听力(雅思/托福)',max_length=20)
    score_IT_Speaking=models.FloatField(verbose_name=u'口语(雅思/托福)',max_length=20)
    score_IT_Reading=models.FloatField(verbose_name=u'阅读(雅思/托福)',max_length=20)
    score_IT_Writing=models.FloatField(verbose_name=u'写作(雅思/托福)',max_length=20)

    # GRE成绩可以为空白，默认为0，所以设置为不能为空也行
    score_GRE = models.IntegerField(verbose_name=u'GRE总分',max_length=20,blank=True,null=True)
    score_GRE_Verbal = models.IntegerField(verbose_name=u'GRE(词汇)',max_length=20,blank=True,null=True)
    score_GRE_Quan = models.IntegerField(verbose_name=u'GRE(数学)',max_length=20,blank=True,null=True)
    score_GRE_Anal = models.IntegerField(verbose_name=u'GRE(分析性写作)',max_length=20,blank=True,null=True)
    # 专利和文章都可以为空白，可以为空值
    in_papers=models.IntegerField(verbose_name=u'国际期刊(篇数)',max_length=20,blank=True,null=True)
    na_papers=models.IntegerField(verbose_name=u'国内期刊(篇数)',max_length=20,blank=True,null=True)
    in_patent=models.IntegerField(verbose_name=u'国际专利(篇数)',max_length=20,blank=True,null=True)
    na_patent=models.IntegerField(verbose_name=u'国内专利(篇数)',max_length=20,blank=True,null=True)
    # 其余加分项可以空白，也可以为空值
    research=models.TextField(verbose_name=u'科研经历',blank=True,null=True)
    placement=models.TextField(verbose_name=u'实习',blank=True,null=True)
    social_practice=models.TextField(verbose_name=u'社会实践',blank=True,null=True)
    specilty=models.TextField(verbose_name=u'特长',blank=True,null=True)
    recommendation = models.IntegerField(verbose_name=u'推荐',choices=recommendation_choice,default=0)

    result_desc = models.CharField(verbose_name=u'测评结果',max_length=40)

    def __unicode__(self):
        return self.cell_phone_number

    def intention_country1(self):
        return self.intention_country

    intention_country1.short_description=u'目标院校'
    intention_country1.admin_order_field = 'intention_country'

    def full_name(self):
        if self.first_name is None:
            self.first_name = ''
        if self.last_name is None:
            self.last_name = ''
        if self.first_name == '' and self.last_name == '':
            self.first_name = '/'
        return self.first_name + '' + self.last_name

    full_name.admin_order_field='first_name'
    full_name.short_description = u"姓名"


# 以下是高中部分
# 高中毕业院校
class highSchool(models.Model):
    name = models.CharField(max_length=32)
    level = models.IntegerField(max_length=32)

# 高中留学美国大学
class high_University(models.Model):
    name = models.CharField(max_length=32)
    # id = models.IntegerField(max_length=32)
    world_rank = models.IntegerField(max_length=32)
    in_rank = models.IntegerField(max_length=32)
    level = models.IntegerField(max_length=32)
    country = models.CharField(max_length=32)

# 高中留学英国大学
class high_University_UK(models.Model):
    name = models.CharField(max_length=32)
    # id = models.IntegerField(max_length=32)
    world_rank = models.IntegerField(max_length=32)
    in_rank = models.IntegerField(max_length=32)
    level = models.IntegerField(max_length=32)
    country = models.CharField(max_length=32)

class high_University_CA(models.Model):
    name = models.CharField(max_length=32)
    # id = models.IntegerField(max_length=32)
    world_rank = models.IntegerField(max_length=32)
    in_rank = models.IntegerField(max_length=32)
    level = models.IntegerField(max_length=32)
    country = models.CharField(max_length=32)

class HighSchoolFormModel(models.Model):
    first_name = models.CharField(verbose_name=u'姓', max_length=20, blank=True, null=True)  # 姓可以空白，可以为空值
    last_name = models.CharField(verbose_name=u'名', max_length=20, blank=True, null=True)  # 名可以空白，可以为空值
    talentStudent = models.IntegerField(verbose_name=u'是否特长生', choices=talentStudent_choice, default=0)

    cell_phone_number = models.CharField(u'用户', max_length=40)  # 电话必须要写

    intention_country = models.CharField(verbose_name=u'目标国家', max_length=20, choices=highcountry_choice,
                                         default='0')  # 意向国家一定要写，默认为---国家---
    # intention_school=models.CharField(max_length=20,blank=True,choices=get_IntentionSchool())
    intention_school = models.CharField(verbose_name=u'目标院校', max_length=20, blank=True,null=True)  # 意向学校可以不选，可以为空白，可以空值
    graduate_school = models.CharField(verbose_name=u'毕业院校', choices=get_HighSchool(), default='0',
                                       max_length=20)  # 毕业院校一定要选,不能为空
    GPA_middle = models.FloatField(verbose_name=u'初中GPA', max_length=20)  # GPA一定要填写，不能为空
    GPA_high = models.FloatField(verbose_name=u'高中GPA', max_length=20)  # GPA一定要填写，不能为空

    score_SAT = models.IntegerField(verbose_name=u'SAT成绩', max_length=20)
    score_TOEFL = models.IntegerField(verbose_name=u'托福成绩', max_length=20)

    awards = models.TextField(verbose_name=u'所获奖项', blank=True, null=True)
    research = models.TextField(verbose_name=u'科研竞赛', blank=True, null=True)
    art = models.TextField(verbose_name=u'文学艺术', blank=True, null=True)

    recommendations=models.IntegerField(verbose_name=u'推荐信(篇数)',max_length=20)

    def __unicode__(self):
        return self.cell_phone_number

    def full_name(self):
        if self.first_name is None:
            self.first_name = ''
        if self.last_name is None:
            self.last_name = ''
        if self.first_name == '' and self.last_name == '':
            self.first_name = '/'
        return self.first_name + '' + self.last_name

    full_name.admin_order_field = 'first_name'
    full_name.short_description = u"姓名"

class HighSchoolFormModelUK(models.Model):
    first_name = models.CharField(verbose_name=u'姓', max_length=20, blank=True, null=True)  # 姓可以空白，可以为空值
    last_name = models.CharField(verbose_name=u'名', max_length=20, blank=True, null=True)  # 名可以空白，可以为空值
    talentStudent = models.IntegerField(verbose_name=u'是否特长生', choices=talentStudent_choice, default=0)

    cell_phone_number = models.CharField(u'用户', max_length=40)  # 电话必须要写

    intention_country = models.CharField(verbose_name=u'目标国家', max_length=20, choices=highcountry_choice_uk,
                                         default='0')  # 意向国家一定要写，默认为---国家---
    # intention_school=models.CharField(max_length=20,blank=True,choices=get_IntentionSchool())
    intention_school = models.CharField(verbose_name=u'目标院校', max_length=20, blank=True,null=True)  # 意向学校可以不选，可以为空白，可以空值
    graduate_school = models.CharField(verbose_name=u'毕业院校', choices=get_HighSchool(), default='0',
                                       max_length=20)  # 毕业院校一定要选,不能为空
    GPA_middle = models.FloatField(verbose_name=u'初中GPA', max_length=20)  # GPA一定要填写，不能为空
    GPA_high = models.FloatField(verbose_name=u'高中GPA', max_length=20)  # GPA一定要填写，不能为空


    score_IELT = models.IntegerField(verbose_name=u'雅思成绩', max_length=20)
    #美国
    score_SAT = models.IntegerField(verbose_name=u'SAT成绩', max_length=20)
    score_TOEFL = models.IntegerField(verbose_name=u'托福成绩', max_length=20)
    #加拿大
    score_all = models.IntegerField(verbose_name=u'总分', max_length=20)
    score_listen = models.IntegerField(verbose_name=u'听力', max_length=20)
    score_speak = models.IntegerField(verbose_name=u'口语', max_length=20)
    score_read = models.IntegerField(verbose_name=u'阅读', max_length=20)
    score_write = models.IntegerField(verbose_name=u'写作', max_length=20)

    awards = models.TextField(verbose_name=u'所获奖项', blank=True, null=True)
    research = models.TextField(verbose_name=u'科研竞赛', blank=True, null=True)
    art = models.TextField(verbose_name=u'文学艺术', blank=True, null=True)

    recommendations=models.IntegerField(verbose_name=u'推荐信(篇数)',max_length=20)

    def __unicode__(self):
        return self.cell_phone_number

    def full_name(self):
        if self.first_name is None:
            self.first_name = ''
        if self.last_name is None:
            self.last_name = ''
        if self.first_name == '' and self.last_name == '':
            self.first_name = '/'
        return self.first_name + '' + self.last_name

    full_name.admin_order_field = 'first_name'
    full_name.short_description = u"姓名"

class HighSchoolFormModelCA(models.Model):
    first_name = models.CharField(verbose_name=u'姓', max_length=20, blank=True, null=True)  # 姓可以空白，可以为空值
    last_name = models.CharField(verbose_name=u'名', max_length=20, blank=True, null=True)  # 名可以空白，可以为空值
    talentStudent = models.IntegerField(verbose_name=u'是否特长生', choices=talentStudent_choice, default=0)

    cell_phone_number = models.CharField(u'用户', max_length=40)  # 电话必须要写

    intention_country = models.CharField(verbose_name=u'目标国家', max_length=20, choices=highcountry_choice_ca,
                                         default='0')  # 意向国家一定要写，默认为---国家---
    # intention_school=models.CharField(max_length=20,blank=True,choices=get_IntentionSchool())
    intention_school = models.CharField(verbose_name=u'目标院校', max_length=20, blank=True,null=True)  # 意向学校可以不选，可以为空白，可以空值
    graduate_school = models.CharField(verbose_name=u'毕业院校', choices=get_HighSchool(), default='0',
                                       max_length=20)  # 毕业院校一定要选,不能为空
    GPA_middle = models.FloatField(verbose_name=u'初中GPA', max_length=20)  # GPA一定要填写，不能为空
    GPA_high = models.FloatField(verbose_name=u'高中GPA', max_length=20)  # GPA一定要填写，不能为空


    score_all = models.IntegerField(verbose_name=u'总分', max_length=20 )
    score_listen = models.IntegerField(verbose_name=u'听力', max_length=20)
    score_speak = models.IntegerField(verbose_name=u'口语', max_length=20 )
    score_read = models.IntegerField(verbose_name=u'阅读', max_length=20 )
    score_write = models.IntegerField(verbose_name=u'写作', max_length=20 )
    # eng default='0'
    score_IELT = models.IntegerField(verbose_name=u'雅思成绩', max_length=20 )

    awards = models.TextField(verbose_name=u'所获奖项', blank=True, null=True)
    research = models.TextField(verbose_name=u'科研竞赛', blank=True, null=True)
    art = models.TextField(verbose_name=u'文学艺术', blank=True, null=True)

    recommendations=models.IntegerField(verbose_name=u'推荐信(篇数)',max_length=20)

    def __unicode__(self):
        return self.cell_phone_number

    def full_name(self):
        if self.first_name is None:
            self.first_name = ''
        if self.last_name is None:
            self.last_name = ''
        if self.first_name == '' and self.last_name == '':
            self.first_name = '/'
        return self.first_name + '' + self.last_name

    full_name.admin_order_field = 'first_name'
    full_name.short_description = u"姓名"