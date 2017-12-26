#-*- coding: UTF-8 -*-
from django.shortcuts import render
from django.shortcuts import HttpResponse
from newapp import models
from newapp.models import high_University,highSchool,high_University_UK,high_University_CA
import json
from newapp.models import University,GraduateUniver,University_Au,University_Ca,University_En
from newapp.forms import UserInfoForm,HighSchoolForm,HighSchoolFormUK,HighSchoolFormCA
from .models import UserInfoFormModel,HighSchoolFormModel,HighSchoolFormModelUK,HighSchoolFormModelCA
import sys,importlib
defaultencoding = 'utf-8'

# Create your views here.
countries_list = [
    {"name": "USA", "id": 1},
    {"name": "ENG", "id": 2},
    {"name": "CAN", "id": 3},
    {"name": "AUS", "id": 4},
]

def index(request):
    return render(request,"index.html")

# ajax返回所选国家的大学列表
def getUniversityList(request):
    if request.method=="POST":
        country=request.POST.get("targetCountry").encode("utf-8");
        # 专业
        intention_major = request.POST.get("targetMajor")
        if country == 'USA':#美国
            universities = University.objects.raw('SELECT *from newapp_university where major=%s GROUP BY name ORDER BY CONVERT(name USING gbk)',[intention_major])
        elif country == 'ENG':#英国
            universities = University_En.objects.raw('SELECT *from newapp_university_en where major=%s GROUP BY name ORDER BY CONVERT(name USING gbk)',[intention_major]);
        elif country == 'CAN':#加拿大
            universities = University_Ca.objects.raw('SELECT *from newapp_university_ca where major=%s GROUP  BY name ORDER BY CONVERT(name USING gbk)',[intention_major]);
        elif country == 'AUS': #澳大利亚
            universities = University_Au.objects.raw('SELECT *from newapp_university_au where major=%s  GROUP BY name ORDER BY CONVERT(name USING gbk)',[intention_major]);
       # elif country == "加拿大":
        #    universities = University.objects.raw('SELECT *from newapp_university_ca GROUP BY name ORDER BY CONVERT(name USING gbk)');
        universityName=[]
        universityLevel=[]
        universitycategoryLevel = []
        for u in universities:
            universityName.append(u.name)
            universityLevel.append(u.level)
            universitycategoryLevel.append(u.category_level)
        data={"universityName":universityName,"universitycategoryLevel":universitycategoryLevel}
        return HttpResponse(json.dumps(data),content_type='application/json');

def assessmentForm(request):
    if request.method == "POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
            studentFName = form.cleaned_data['first_name']
            studentLName = form.cleaned_data['last_name']
            if studentFName is None:
                studentFName= ''
            if studentLName is None:
                studentLName =''
            cell_phone_number=form.cleaned_data['cell_phone_number']
            # 获取国家的名字
            intention_countryName = form.cleaned_data['intention_country'].encode("utf-8")  # 国家名字 如果不使用encode的话就是Unicode编码，但是使用encode之后还不是中文。。。
            for coun in countries_list:
                if coun["name"] == intention_countryName:  # coun["name"]不是unicode编码，因此如果intention_countryName不使用encode的话是unicode编码，两者无法比较
                    intention_countryId = coun["id"]  # intention_countryId 国家Id

            # 想去的学校
            #intention_school = form.cleaned_data['intention_school'].encode("utf-8")# 学校的名称
            intention_school=request.POST.get("intention_school")
            # 专业
            intention_major = form.cleaned_data['intention_major']

            # 本科院校gu_level
            gu_name=form.cleaned_data['graduate_school']
            gu_level = GraduateUniver.objects.raw('SELECT *from newapp_graduateuniver where name=%s',[gu_name])[0].gu_level

            # GPA
            GPA = float(form.cleaned_data['score_GPA'])
            rank_in_major=form.cleaned_data['ranking_in_major']

            # 雅思/托福
            IELTS_TOEFL = float(form.cleaned_data['score_IELTS_TOEFL'])  # 总分
            IT_Listening = float(form.cleaned_data['score_IT_Listening'])  # 听
            IT_Speaking = float(form.cleaned_data['score_IT_Speaking'])  # 听
            IT_Reading = float(form.cleaned_data['score_IT_Reading'])  # 读
            IT_Writing = float(form.cleaned_data['score_IT_Writing'])  # 写

            # GRE
            GRE_Total = form.cleaned_data['score_GRE']
            score_GRE_Verbal=form.cleaned_data['score_GRE_Verbal']
            score_GRE_Quan = form.cleaned_data['score_GRE_Quan']
            score_GRE_Anal = form.cleaned_data['score_GRE_Anal']
            if score_GRE_Verbal is None:
                score_GRE_Verbal=0
            if score_GRE_Quan is None:
                score_GRE_Quan=0
            if score_GRE_Anal is None:
                score_GRE_Anal=0

            # 获取加分项
            In_Papers = form.cleaned_data['in_papers']# paper篇数
            Na_Papers = form.cleaned_data['na_papers']

            In_Patents = form.cleaned_data['in_patent'] # 专利篇数
            Na_Patents = form.cleaned_data['na_patent']

            Research = form.cleaned_data['research']
            Placement = form.cleaned_data['placement']
            Social_Practice = form.cleaned_data['social_practice']
            Specilty = form.cleaned_data['specilty']

            Recommendation = form.cleaned_data['recommendation']

            # 根据获取的数据计算得分
            sum = 0
            GPA_good = False
            # 转换GPA的值
            if GPA >= 3.9:
                GPA_level = 1
                GPA_Trans = 100
            elif GPA >= 3.8:
                GPA_level = 1
                GPA_good = True
                GPA_Trans = 95
            elif GPA >= 3.7:
                GPA_level = 2
                GPA_good = True
                GPA_Trans = 90
            elif GPA >= 3.6:
                GPA_level = 2
                GPA_Trans = 85
            elif GPA >= 3.5:
                GPA_level = 2
                GPA_Trans = 80
            elif GPA >= 3.4:
                GPA_level = 3
                GPA_Trans = 75
            elif GPA >= 3.3:
                GPA_level = 3
                GPA_Trans = 70
            elif GPA >= 3.2:
                GPA_level = 3
                GPA_Trans = 65
            elif GPA >= 3.1:
                GPA_level = 3
                GPA_Trans = 60
            elif GPA >= 3.0:
                GPA_level = 4
                GPA_Trans = 55
            else:
                GPA_level = 5
                GPA_Trans = 50
            gpa_score = GPA_Trans * 0.2669

            IELTS_TOEFL_good = False

            # 计算语言成绩：雅思/托福
            yt_Listening = 1
            yt_Speaking = 1
            yt_Reading = 1
            yt_Writing = 1
            yt_flag = 0
            if IELTS_TOEFL > 10:  # 说明是托福成绩
                if IELTS_TOEFL > 110:
                    IELTS_TOEFL_level = 1
                    IELTS_TOEFL_good = True
                    IELTS_TOEFL_Trans = 100
                elif IELTS_TOEFL > 100:
                    IELTS_TOEFL_level = 2
                    IELTS_TOEFL_Trans = 95
                elif IELTS_TOEFL > 90:
                    IELTS_TOEFL_level = 3
                    IELTS_TOEFL_Trans = 85
                elif IELTS_TOEFL > 80:
                    IELTS_TOEFL_level = 3
                    IELTS_TOEFL_Trans = 75
                else:
                    IELTS_TOEFL_level = 4
                    IELTS_TOEFL_Trans = 70
                if (IT_Listening < 20):
                    yt_Listening = 0
                    yt_flag = 1
                if (IT_Speaking < 20):
                    yt_Speaking = 0
                    yt_flag = 1
                if (IT_Reading < 20):
                    yt_Reading = 0
                    yt_flag = 1
                if (IT_Writing < 20):
                    yt_Writing = 0
                    yt_flag = 1
            else:
                if IELTS_TOEFL >= 7.0:
                    IELTS_TOEFL_level = 1
                    IELTS_TOEFL_good = True
                    IELTS_TOEFL_Trans = 100
                elif IELTS_TOEFL >= 6.5:
                    IELTS_TOEFL_level = 2
                    IELTS_TOEFL_Trans = 90
                elif IELTS_TOEFL >= 6.0:
                    IELTS_TOEFL_level = 3
                    IELTS_TOEFL_Trans = 80
                else:
                    IELTS_TOEFL_level = 4
                    IELTS_TOEFL_Trans = 70
                if (IT_Listening < 6.0):
                    yt_Listening = 0
                    yt_flag = 1
                if (IT_Speaking < 6.0):
                    yt_Speaking = 0
                    yt_flag = 1
                if (IT_Reading < 6.0):
                    yt_Reading = 0
                    yt_flag = 1
                if (IT_Writing < 6.0):
                    yt_Writing = 0
                    yt_flag = 1

            i_score = IELTS_TOEFL_Trans * 0.2669

            # 计算GRE的值
            if GRE_Total != ''and GRE_Total is not None:
                gre = int(GRE_Total)
                if gre > 333:
                    GRE_Trans = 100
                elif gre > 325:
                    GRE_Trans = 90
                elif gre > 320:
                    GRE_Trans = 85
                elif gre > 300:
                    GRE_Trans = 80
                else:
                    GRE_Trans = 70
            else:
                GRE_Total=0
                GRE_Trans = 85
            g_score = GRE_Trans * 0.1335

            # 计算paper的分值
            if In_Papers != '' and In_Papers is not None:
                inpapers = int(In_Papers)
            else:
                In_Papers = 0
                inpapers = 0
            if Na_Papers != ''and Na_Papers is not None:
                napapers = int(Na_Papers)
            else:
                Na_Papers=0
                napapers = 0

            # 计算patent的分值
            if In_Patents != ''and In_Patents is not None:
                inpatent = int(In_Patents)
            else:
                In_Patents=0
                inpatent = 0
            if Na_Patents != ''and Na_Patents is not None:
                napatents = int(Na_Patents)
            else:
                Na_Patents=0
                napatents = 0

            paper_score = inpapers * 2.5 + napapers
            patent_score = inpatent * 2.5 + napatents
            if paper_score > 5: paper_score = 5
            if patent_score > 5: patent_score = 5

            if paper_score >= 3:
                paper_good = True;
            else:
                paper_good = False;

            if patent_score >= 3:
                patent_good = True;
            else:
                patent_good = False;
            # 计算科研，竞赛，实习，社会实践，特长的分值，不空就给分
            if Research == '':
                research_score = 0
            else:
                research_score = 5

            if Social_Practice == '':
                socialpractice_score = 0
            else:
                socialpractice_score = 4

            if Placement == '':
                placement_score = 0
            else:
                placement_score = 5

            if Specilty is '' or Specilty is None:
                Specilty = 0
                specilty_score = 0
            else:
                specilty_score = 4

            # 计算总分
            sum = i_score + gpa_score + g_score + patent_score + paper_score + specilty_score + research_score + placement_score + socialpractice_score

            # 根据成绩分为三个level
            level = 0;
            if sum > 65:
                level = 1
            elif sum < 50:
                level = 3
            else:
                level = 2

            if intention_countryId == 1:  # 选择了美国
                countryName='美国'
                gu_category = University.objects.filter(gu_level=gu_level, level=level, sublevel=2)[
                    0].category_level  # 获取该学生能上的学校的category_level
                if(intention_school != '0'):
                    intention_school_qu = University.objects.filter(name=intention_school);
                university_h = University.objects.filter(gu_level=gu_level, level=level, sublevel=1,
                                                         major=intention_major).order_by('rank_major')[
                               0:6]  # 大学的级别，每档大学中的级别，所推荐学校的级别
                university_eg = University.objects.filter(gu_level=gu_level, level=level, sublevel=1,
                                                          major=intention_major).order_by('rank_major')[0:2]
                university_m = University.objects.filter(gu_level=gu_level, level=level, sublevel=2,
                                                         major=intention_major).order_by('rank_major')[0:6]
                university_l = University.objects.filter(gu_level=gu_level, level=level, sublevel=3,
                                                         major=intention_major).order_by('rank_major')[0:4]

            elif intention_countryId == 2:  # 英国
                countryName = '英国'
                gu_category = University_En.objects.filter(gu_level=gu_level, level=level, sublevel=2)[
                    0].category_level  # 获取该学生能上的学校的category_level
                if (intention_school != '0'):
                    intention_school_qu = University_En.objects.filter(name=intention_school);
                university_eg = University_En.objects.filter(gu_level=gu_level, level=level, sublevel=1,
                                                             major=intention_major).order_by('rank_major')[0:2]
                university_h = University_En.objects.filter(gu_level=gu_level, level=level, sublevel=1,
                                                            major=intention_major).order_by('rank_major')[
                               0:6]  # 大学的级别，每档大学中的级别，所推荐学校的级别
                university_m = University_En.objects.filter(gu_level=gu_level, level=level, sublevel=2,
                                                            major=intention_major).order_by('rank_major')[0:6]
                university_l = University_En.objects.filter(gu_level=gu_level, level=level, sublevel=3,
                                                            major=intention_major).order_by('rank_major')[0:4]
            elif intention_countryId == 3:  # 加拿大
                countryName = '加拿大'
                gu_category = University_Ca.objects.filter(gu_level=gu_level, level=level, sublevel=2)[
                    0].category_level  # 获取该学生能上的学校的category_level
                if (intention_school != '0'):
                    intention_school_qu = University_Ca.objects.filter(name=intention_school);
                university_eg = University_Ca.objects.filter(gu_level=gu_level, level=level, sublevel=1,
                                                             major=intention_major).order_by('rank_major')[0:2]
                university_h = University_Ca.objects.filter(gu_level=gu_level, level=level, sublevel=1,
                                                            major=intention_major).order_by('rank_major')[
                               0:6]  # 大学的级别，每档大学中的级别，所推荐学校的级别
                university_m = University_Ca.objects.filter(gu_level=gu_level, level=level, sublevel=2,
                                                            major=intention_major).order_by('rank_major')[0:6]
                university_l = University_Ca.objects.filter(gu_level=gu_level, level=level, sublevel=3,
                                                            major=intention_major).order_by('rank_major')[0:4]
            elif intention_countryId == 4:  # 澳大利亚
                countryName = '澳大利亚'
                gu_category = University_Au.objects.filter(gu_level=gu_level, level=level, sublevel=2)[
                    0].category_level  # 获取该学生能上的学校的category_level
                if (intention_school != '0'):
                    intention_school_qu = University_Au.objects.filter(name=intention_school);
                university_eg = University_Au.objects.filter(gu_level=gu_level, level=level, sublevel=1,
                                                             major=intention_major).order_by('rank_major')[0:2]
                university_h = University_Au.objects.filter(gu_level=gu_level, level=level, sublevel=1,
                                                            major=intention_major).order_by('rank_major')[
                               0:6]  # 大学的级别，每档大学中的级别，所推荐学校的级别
                university_m = University_Au.objects.filter(gu_level=gu_level, level=level, sublevel=2,
                                                            major=intention_major).order_by('rank_major')[0:6]
                university_l = University_Au.objects.filter(gu_level=gu_level, level=level, sublevel=3,
                                                            major=intention_major).order_by('rank_major')[0:4]
            no_high = 0
            no_mid = 0
            no_low = 0
            if (len(university_h) == 0):
                no_high = 1
            if (len(university_m) == 0):
                no_mid = 1
            if (len(university_l) == 0):
                no_low = 1

            # 加权计算总分
            if Recommendation == 1:  # 推荐人认识导师
                recommendation = 1;
            else:  # 不认识
                recommendation = 0;

            if intention_school == '0':  # 等于0表示没选学校
                result_desc='未选择目标院校'
                intention_school='无'
                UserInfoObject = UserInfoFormModel(first_name=studentFName, last_name=studentLName,
                                                   cell_phone_number=cell_phone_number,
                                                   intention_country=countryName,
                                                   intention_school=intention_school,
                                                   intention_major=intention_major, graduate_school=gu_name,
                                                   ranking_in_major=rank_in_major,
                                                   score_GPA=GPA, score_IELTS_TOEFL=IELTS_TOEFL,
                                                   score_IT_Listening=IT_Listening,
                                                   score_IT_Speaking=IT_Speaking, score_IT_Reading=IT_Reading,
                                                   score_IT_Writing=IT_Writing,
                                                   score_GRE=GRE_Total, score_GRE_Quan=score_GRE_Quan,
                                                   score_GRE_Verbal=score_GRE_Verbal,
                                                   score_GRE_Anal=score_GRE_Anal, in_papers=In_Papers,
                                                   na_papers=Na_Papers, in_patent=In_Patents,
                                                   na_patent=Na_Patents, research=Research, placement=Placement,
                                                   social_practice=Social_Practice,
                                                   specilty=Specilty, recommendation=Recommendation,
                                                   result_desc=result_desc
                                                   )
                UserInfoObject.save()
                return render(request, "result_2.html",
                              {"studentFName": studentFName,
                               "studentLName": studentLName,
                               "university_h": university_h, "university_m": university_m,
                               "university_l": university_l,
                               "in_patent": inpatent, "na_patent": napatents,
                               "in_paper": inpapers, "na_paper": napapers,
                               "GPA_level": GPA_level,
                               "IELTS_TOEFL_level": IELTS_TOEFL_level,
                               "IELTS_TOEFL_good": IELTS_TOEFL_good,
                               "GPA_good": GPA_good,
                               "result": 1,
                               "no_high": no_high,
                               "no_mid": no_mid,
                               "no_low": no_low,
                               "gu_level": int(gu_level),
                               "intention_school": intention_school,
                               "intention_major": intention_major,
                               "paper_good": paper_good,
                               "patent_good": patent_good,
                               "recommendation": recommendation,
                               "yt_Listening": yt_Listening,
                               "yt_Speaking": yt_Speaking,
                               "yt_Reading": yt_Reading,
                               "yt_Writing": yt_Writing,
                               "yt_flag": yt_flag
                               #   "intention_school":
                               })  # 直接推荐学校
            else:  # 选择了学校 intention_school
                intention_category = intention_school_qu[0].category_level
                rank_total = intention_school_qu[0].rank_total
                rank_major = intention_school_qu[0].rank_major
                difference = int(intention_category) - int(
                    gu_category)  # 想去的学校与自己所在学校的level差，大于0代表想去的学校可以上，小于0表示上不了

                if difference <= 0:  # 如果想去的学校级别等于可以上的学校
                    if difference == 0:  # 所选的正好是可以上的，通过，成绩成绩一般
                        result = 2
                        if recommendation ==1:
                            result_desc=u'有大牛推荐，通过但成绩一般'
                        else:
                            result_desc = u'通过但成绩一般'
                    elif difference == -1:
                        result = 3  # 所选的高于可上的一级，虽然没有通过，但是可以尝试冲刺
                        if recommendation ==1:
                            result_desc=u'成绩低，因为有大牛推荐才能通过'
                        else:
                            result_desc = u'未通过，建议冲刺'
                    else:
                        result = 4;  # 所选的高于可上的2级以上,直接不通过
                        if recommendation ==1:
                            result_desc=u'成绩低，因为有大牛推荐才能通过'
                        else:
                            result_desc = u'未通过'
                else:
                    result = 5;  # 所选的学校level有点低了，可以建议选择更好的学校
                    result_desc=u'优秀'

                if GPA_level >= 4:
                    if IELTS_TOEFL_level >= 4:
                        result_desc = u'GPA和语言成绩太低，未通过'
                        result = 10
                    else:
                        result_desc = u'GPA太低，未通过'
                        result = 1
                else:
                    if IELTS_TOEFL_level >= 4:
                        result_desc = u'语言成绩太低，未通过'
                        result = 0

                UserInfoObject = UserInfoFormModel(first_name=studentFName, last_name=studentLName,
                                                   cell_phone_number=cell_phone_number,
                                                   intention_country=countryName,
                                                   intention_school=intention_school,
                                                   intention_major=intention_major, graduate_school=gu_name,
                                                   ranking_in_major=rank_in_major,
                                                   score_GPA=GPA, score_IELTS_TOEFL=IELTS_TOEFL,
                                                   score_IT_Listening=IT_Listening,
                                                   score_IT_Speaking=IT_Speaking, score_IT_Reading=IT_Reading,
                                                   score_IT_Writing=IT_Writing,
                                                   score_GRE=GRE_Total, score_GRE_Quan=score_GRE_Quan,
                                                   score_GRE_Verbal=score_GRE_Verbal,
                                                   score_GRE_Anal=score_GRE_Anal, in_papers=In_Papers,
                                                   na_papers=Na_Papers, in_patent=In_Patents,
                                                   na_patent=Na_Patents, research=Research, placement=Placement,
                                                   social_practice=Social_Practice,
                                                   specilty=Specilty, recommendation=Recommendation,
                                                   result_desc=result_desc
                                                   )
                UserInfoObject.save()
                return render(request, "result_11.html",
                              {"studentFName": studentFName,
                               "studentLName": studentLName,
                               "university_h": university_h, "university_m": university_m,
                               "university_l": university_l,
                               "university_eg": university_eg,
                               "in_patent": inpatent, "na_patent": napatents,
                               "in_paper": inpapers, "na_paper": napapers,
                               "GPA_level": GPA_level,
                               "IELTS_TOEFL_level": IELTS_TOEFL_level,
                               "IELTS_TOEFL_good": IELTS_TOEFL_good,
                               "GPA_good": GPA_good,
                               "result": result,
                               "no_high": no_high,
                               "no_mid": no_mid,
                               "no_low": no_low,
                               "gu_level": int(gu_level),
                               "intention_school": intention_school,
                               "rank_total": rank_total,
                               "rank_major": rank_major,
                               "intention_major": intention_major,
                               "paper_good": paper_good,
                               "patent_good": patent_good,
                               "recommendation": recommendation,
                               "yt_Listening": yt_Listening,
                               "yt_Speaking": yt_Speaking,
                               "yt_Reading": yt_Reading,
                               "yt_Writing": yt_Writing,
                               "yt_flag": yt_flag
                               })
        else:
           # return  HttpResponse(u'测试')
            return render(request, 'indexForm.html', {"form": form})
    else:
        form=UserInfoForm()
        return render(request, 'indexForm.html', {"form":form})



# 高中部分

# ajax返回所选国家的大学列表
def highCountry(request):
    countries_list = [
        {"name": "美国","id":1},
        {"name": "英国","id":2},
        {"name": "加拿大","id":3},
        # {"name": "澳大利亚","id":4},
    ]
    if request.method=="POST":
        country=request.POST.get("targetCountry").encode("utf-8");
        # print(country)
        if country == b'USA':
            universities = University.objects.raw('SELECT *from newapp_high_university GROUP BY name ORDER BY CONVERT(name USING gbk)');
        if country == b'ENG':
            universities = University.objects.raw('SELECT *from newapp_high_university_uk GROUP BY name ORDER BY CONVERT(name USING gbk)');
        if country == b'CAN':
            universities = University.objects.raw('SELECT *from newapp_high_university_ca GROUP BY name ORDER BY CONVERT(name USING gbk)');
        # print(universities)
        universityName=[]
        universityLevel=[]
        for u in universities:
            universityName.append(u.name)
            universityLevel.append(u.level)
        data={"universityName":universityName}
        return HttpResponse(json.dumps(data),content_type='application/json');


#高中留学返回界面
def highResult(request):
    if request.method == "POST":
        form = HighSchoolForm(request.POST)
        if form.is_valid():
            studentFName = form.cleaned_data['first_name']
            studentLName = form.cleaned_data['last_name']
            if studentFName is None:
                studentFName = ''
            if studentLName is None:
                studentLName = ''

            cell_phone_number = form.cleaned_data['cell_phone_number']

            intention_countryName = form.cleaned_data['intention_country'].encode("utf-8")  # 国家名字如果不使用encode的话就是Unicode编码，但是使用encode之后还不是中文。。。
            for coun in countries_list:
                if coun["name"] == intention_countryName:  # coun["name"]不是unicode编码，因此如果intention_countryName不使用encode的话是unicode编码，两者无法比较
                    intention_countryId = coun["id"]  # intention_countryId 国家Id

            # 想去的学校
            intention_school = request.POST.get("intention_school")
            highSchool = request.POST.get("graduate_school")
            # GPA
            GPA_high = float(form.cleaned_data['GPA_high'])
            GPA_middle = form.cleaned_data['GPA_middle']

            # 托福
            TOEFL_Total = float(form.cleaned_data['score_TOEFL'])  # 总分
            SAT_Total = float(form.cleaned_data['score_SAT'])

            # 获取加分项
            research = form.cleaned_data['research']
            awards = form.cleaned_data['awards']
            art = form.cleaned_data['art']

            Recomm_Total = form.cleaned_data['recommendations']

            Special= form.cleaned_data['talentStudent']

            if awards!=''or research!=''or art!='':
                artwork=100
            else:
                artwork=0

            if GPA_high  is not None:
                GPA_high = float(GPA_high)
            if GPA_middle  is not None:
                GPA_middle = float(GPA_middle)

            GPA_good = False
            GPA_level=1

            if highSchool==1:
                guscore=6
            elif highSchool==2:
                guscore=5
            elif highSchool==3:
                guscore=3
            elif highSchool==4:
                guscore=2
            else:
                guscore=0
            # 转换GPA的值
            if GPA_high >= 3.8:
                GPA_Trans = 100
            elif GPA_high >= 3.7:
                GPA_level = 1
                GPA_good = True
                GPA_Trans = 95
            elif GPA_high >= 3.7:
                GPA_level = 1
                GPA_good = True
                GPA_Trans = 90
            elif GPA_high >= 3.65:
                GPA_level = 2
                GPA_Trans = 90
            elif GPA_high >= 3.5:
                GPA_level = 3
                GPA_Trans = 80
            else:
                GPA_level = 5
                GPA_Trans = 60
            # 计算SAT的值

            SAT_Total = int(SAT_Total)
            if SAT_Total>=2100:
                SAT_Trans = 105
            elif SAT_Total >= 2050:
                SAT_Trans = 100
            elif SAT_Total >= 1990:
                SAT_Trans = 90
            elif SAT_Total >= 1860:
                SAT_Trans = 80
            elif SAT_Total >= 1770:
                SAT_Trans = 75
            elif SAT_Total >= 1630:
                SAT_Trans = 70
            elif SAT_Total >= 1260:
                SAT_Trans = 60
            else:
                SAT_Trans = 50
            # 计算TOEFL的值
            IELTS_TOEFL_good = False
            IELTS_TOEFL_level=1
            TOEFL_Total = int(TOEFL_Total)
            if TOEFL_Total>= 110:
                IELTS_TOEFL_level = 1
                IELTS_TOEFL_good = True
                TOEFL_Trans = 105
            elif TOEFL_Total>= 100:
                IELTS_TOEFL_level = 1
                TOEFL_Trans = 100
            elif TOEFL_Total >= 90:
                IELTS_TOEFL_level = 2
                TOEFL_Trans = 90
            elif TOEFL_Total >= 80:
                IELTS_TOEFL_level = 3
                TOEFL_Trans = 80
            elif TOEFL_Total >= 70:
                IELTS_TOEFL_level = 4
                TOEFL_Trans = 70
            elif TOEFL_Total >= 60:
                IELTS_TOEFL_level = 4
                TOEFL_Trans = 60
            else:
                TOEFL_Trans = 50
                IELTS_TOEFL_level = 4
            sum = 0.0
            addscore=0
            if GPA_high>GPA_middle:
                addscore=2
            if Special== 2: #不是特长生
                sum=float(GPA_Trans*0.6)+float(SAT_Trans*0.15)+float(TOEFL_Trans*0.15)+addscore+int(Recomm_Total)+guscore
            else:
                sum = float(GPA_Trans*0.15)+float(SAT_Trans*0.2)+float(TOEFL_Trans*0.15)+addscore+int(Recomm_Total)+artwork*0.4

            if sum>=93:
                level = 1
            elif sum>=83:
                level = 2
            else:
                level = 3
            no_high = 0
            no_mid = 0
            no_low = 0
            #u=high_University.objects.all();
            university_h = high_University.objects.filter(level=level).order_by('usa_rank')[0:4]
            university_m = high_University.objects.filter(level=level).order_by('usa_rank')[5:9]
            university_l = high_University.objects.filter(level=level).order_by('usa_rank')[9:]

            HighSchoolObject = HighSchoolFormModel(first_name=studentFName,
                                               last_name=studentLName,
                                               cell_phone_number=cell_phone_number,
                                               intention_country=intention_countryName,
                                               intention_school=intention_school,
                                               graduate_school=highSchool,
                                               GPA_high=GPA_high,
                                               GPA_middle=GPA_middle,
                                               score_TOEFL=TOEFL_Total,
                                               score_SAT=SAT_Total,
                                               research=research, art=art,
                                               awards=awards,
                                               talentStudent=Special, recommendations=Recomm_Total,
                                               )
            HighSchoolObject.save()
            return render(request, "highResult.html",
                              {   "studentFName":studentFName,
                                  "studentLName":studentLName,
                                  "university_h": university_h,
                                  "university_m": university_m, "university_l": university_l,
                                  "country": intention_countryName,
                                   "GPA_level": GPA_level,
                                   "IELTS_TOEFL_level": IELTS_TOEFL_level,
                                   "IELTS_TOEFL_good": IELTS_TOEFL_good ,
                                   "GPA_good": GPA_good,
                                  "no_high": no_high,
                                  "no_mid": no_mid,
                                  "no_low": no_low,
                               })
        else:
            return render(request, 'highAssessment.html', {"form": form})
    else:
        form = HighSchoolForm()
        return render(request, 'highAssessment.html', {"form": form})

    '''  intention_school = request.POST.get("intention_school")  # 学校的名称
   # intention_school_qu = highUniversity.objects.filter(name=intention_school)[0].level;
    #gu_category = University.objects.filter(level=level, sublevel=2)[0].category_level  # 获取该学生能上的学校的category_level
    university_h = highUniversity.objects.filter(level=level).order_by('usa_rank')[0:4]  # 大学的级别，每档大学中的级别，所推荐学校的级别
    university_m = highUniversity.objects.filter(level=level).order_by('usa_rank')[4:7]
    university_l = highUniversity.objects.filter(level=level).order_by('usa_rank')[7:9]
    no_high = 0
    no_mid = 0
    no_low = 0
    if (len(university_h) == 0):
        no_high = 1
    if (len(university_m) == 0):
        no_mid = 1
    if (len(university_l) == 0):
        no_low = 1
    if intention_school == '0':  # 等于0表示没选学校
        return render(request, "highResult.html",
                      {   "studentLName":studentLName,
                           "university_h": university_h, "university_m": university_m, "university_l": university_l,
                           "country": intention_countryName,
                           "GPA_level": 1,
                           "IELTS_TOEFL_level": 1,
                           "IELTS_TOEFL_good": 1,
                           "GPA_good": 1,
                           "no_high": no_high,
                           "no_mid": no_mid,
                           "no_low": no_low,
                       })  # 直接推荐学校
    else:  # 选择了学校 intention_school
        return render(request, "highResult.html",
                      {
                           "studentLName":studentLName,
                           "university_h": university_h, "university_m": university_m, "university_l": university_l,
                           "country": intention_countryName,
                           "GPA_level": 1,
                           "IELTS_TOEFL_level": 1,
                           "IELTS_TOEFL_good": 1,
                           "GPA_good": 1,
                           "no_high": no_high,
                           "no_mid": no_mid,
                           "no_low": no_low,
                       })
        '''

def highResultUK(request):
    if request.method == "POST":
        form = HighSchoolFormUK(request.POST)
        if form.is_valid():
            studentFName = form.cleaned_data['first_name']
            studentLName = form.cleaned_data['last_name']
            if studentFName is None:
                studentFName = ''
            if studentLName is None:
                studentLName = ''

            cell_phone_number = form.cleaned_data['cell_phone_number']

            intention_countryName = form.cleaned_data['intention_country'].encode("utf-8")  # 国家名字如果不使用encode的话就是Unicode编码，但是使用encode之后还不是中文。。。
            # print(intention_countryName)
            for coun in countries_list:
                if coun["name"] == intention_countryName:  # coun["name"]不是unicode编码，因此如果intention_countryName不使用encode的话是unicode编码，两者无法比较
                    intention_countryId = coun["id"]  # intention_countryId 国家Id

            # 想去的学校
            intention_school = request.POST.get("intention_school")
            highSchool = request.POST.get("graduate_school")
            # GPA
            GPA_high = float(form.cleaned_data['GPA_high'])
            GPA_middle = form.cleaned_data['GPA_middle']
            awards = form.cleaned_data['awards']


            Recomm_Total = form.cleaned_data['recommendations']

            Special= form.cleaned_data['talentStudent']

            if awards!='':
                artwork=100
            else:
                artwork=0


            #u=high_University.objects.all();
            university_h="";
            university_l="";
            university_m="";
            if GPA_high is not None:
                GPA_high = float(GPA_high)
            if GPA_middle is not None:
                GPA_middle = float(GPA_middle)
            if IELT_Total is not None:
                IELT_Total = float(IELT_Total)

            if highSchool == 1:
                guscore = 6
            elif highSchool == 2:
                guscore = 5
            elif highSchool == 3:
                guscore = 3
            elif highSchool == 4:
                guscore = 2
            else:
                guscore = 0
            sum = 0.0
            addscore = 0
            if GPA_high > GPA_middle:
                addscore = 2
            if(intention_countryId == 2):
                # 雅思
                IELT_Total = float(form.cleaned_data['score_IELT'])  # 总分
                GPA_good = False
                GPA_level = 1
                # 转换GPA的值
                if GPA_high >= 3.8:
                    GPA_Trans = 100
                elif GPA_high >= 3.7:
                    GPA_level = 1
                    GPA_good = True
                    GPA_Trans = 95
                elif GPA_high >= 3.7:
                    GPA_level = 1
                    GPA_good = True
                    GPA_Trans = 90
                elif GPA_high >= 3.65:
                    GPA_level = 2
                    GPA_Trans = 90
                elif GPA_high >= 3.5:
                    GPA_level = 3
                    GPA_Trans = 80
                else:
                    GPA_level = 5
                    GPA_Trans = 60
                # 计算IELT的值
                IELTS_TOEFL_good = False
                IELTS_TOEFL_level = 1
                if IELT_Total >= 9.0:
                    IELTS_TOEFL_level = 1
                    IELTS_TOEFL_good = True
                    IELT_Trans = 110
                elif IELT_Total >= 8.5:
                    IELTS_TOEFL_level = 1
                    IELTS_TOEFL_good = True
                    IELT_Trans = 100
                elif IELT_Total >= 7:
                    IELTS_TOEFL_level = 2
                    IELT_Trans = 90
                elif IELT_Total >= 6:
                    IELTS_TOEFL_level = 2
                    IELT_Trans = 80
                elif IELT_Total >= 5.5:
                    IELTS_TOEFL_level = 3
                    IELT_Trans = 70
                else:
                    IELTS_TOEFL_level = 4
                    IELT_Trans = 50
                if Special == 2:  # 不是特长生
                    sum = float(GPA_Trans * 0.6) + float(IELT_Trans * 0.3) + addscore + int(Recomm_Total) + guscore
                else:
                    sum = float(GPA_Trans * 0.15) + float(IELT_Trans * 0.4) + addscore + int(Recomm_Total) + artwork * 0.4 + guscore

                if sum >= 90:
                    level = 1
                elif sum >= 80:
                    level = 2
                else:
                    level = 3
                no_high = 0
                no_mid = 0
                no_low = 0
                university_h = high_University_UK.objects.filter(level=level).order_by('uk_rank')[0:4]
                university_m = high_University_UK.objects.filter(level=level).order_by('uk_rank')[5:9]
                university_l = high_University_UK.objects.filter(level=level).order_by('uk_rank')[9:]
                HighSchoolObject = HighSchoolFormModelUK(first_name=studentFName,
                                                         last_name=studentLName,
                                                         cell_phone_number=cell_phone_number,
                                                         intention_country=intention_countryName,
                                                         intention_school=intention_school,
                                                         graduate_school=highSchool,
                                                         GPA_high=GPA_high,
                                                         GPA_middle=GPA_middle,
                                                         score_IELT=IELT_Total,
                                                         awards=awards,
                                                         talentStudent=Special, recommendations=Recomm_Total,
                                                         )
                return render(request, "highResultUK.html",
                              {"studentFName": studentFName,
                               "studentLName": studentLName,
                               "university_h": university_h,
                               "university_m": university_m, "university_l": university_l,
                               "country": intention_countryName,
                               "GPA_level": GPA_level,
                               "IELTS_TOEFL_level": IELTS_TOEFL_level,
                               "IELTS_TOEFL_good": IELTS_TOEFL_good,
                               "GPA_good": GPA_good,
                               "no_high": no_high,
                               "no_mid": no_mid,
                               "no_low": no_low,
                               })
            elif(intention_countryId == 1):
                # 托福
                TOEFL_Total = float(form.cleaned_data['score_TOEFL'])  # 总分
                SAT_Total = float(form.cleaned_data['score_SAT'])
                if awards != '' :
                    artwork = 100
                else:
                    artwork = 0
                GPA_good = False
                GPA_level = 1

                # 转换GPA的值
                if GPA_high >= 3.8:
                    GPA_Trans = 100
                elif GPA_high >= 3.7:
                    GPA_level = 1
                    GPA_good = True
                    GPA_Trans = 95
                elif GPA_high >= 3.7:
                    GPA_level = 1
                    GPA_good = True
                    GPA_Trans = 90
                elif GPA_high >= 3.65:
                    GPA_level = 2
                    GPA_Trans = 90
                elif GPA_high >= 3.5:
                    GPA_level = 3
                    GPA_Trans = 80
                else:
                    GPA_level = 5
                    GPA_Trans = 60
                # 计算SAT的值
                SAT_Total = int(SAT_Total)
                if SAT_Total >= 2100:
                    SAT_Trans = 105
                elif SAT_Total >= 2050:
                    SAT_Trans = 100
                elif SAT_Total >= 1990:
                    SAT_Trans = 90
                elif SAT_Total >= 1860:
                    SAT_Trans = 80
                elif SAT_Total >= 1770:
                    SAT_Trans = 75
                elif SAT_Total >= 1630:
                    SAT_Trans = 70
                elif SAT_Total >= 1260:
                    SAT_Trans = 60
                else:
                    SAT_Trans = 50
                # 计算TOEFL的值
                IELTS_TOEFL_good = False
                TOEFL_Total = int(TOEFL_Total)
                if TOEFL_Total >= 110:
                    IELTS_TOEFL_level = 1
                    IELTS_TOEFL_good = True
                    TOEFL_Trans = 105
                elif TOEFL_Total >= 100:
                    IELTS_TOEFL_level = 1
                    TOEFL_Trans = 100
                elif TOEFL_Total >= 90:
                    IELTS_TOEFL_level = 2
                    TOEFL_Trans = 90
                elif TOEFL_Total >= 80:
                    IELTS_TOEFL_level = 3
                    TOEFL_Trans = 80
                elif TOEFL_Total >= 70:
                    IELTS_TOEFL_level = 4
                    TOEFL_Trans = 70
                elif TOEFL_Total >= 60:
                    IELTS_TOEFL_level = 4
                    TOEFL_Trans = 60
                else:
                    TOEFL_Trans = 50
                    IELTS_TOEFL_level = 4
                if Special == 2:  # 不是特长生
                    sum = float(GPA_Trans * 0.6) + float(SAT_Trans * 0.15) + float(TOEFL_Trans * 0.15) + addscore + int( Recomm_Total) + guscore
                else:
                    sum = float(GPA_Trans * 0.15) + float(SAT_Trans * 0.2) + float(TOEFL_Trans * 0.15) + addscore + int( Recomm_Total) + artwork * 0.4

                if sum >= 93:
                    level = 1
                elif sum >= 83:
                    level = 2
                else:
                    level = 3
                no_high = 0
                no_mid = 0
                no_low = 0
                university_h = high_University.objects.filter(level=level).order_by('usa_rank')[0:4]
                university_m = high_University.objects.filter(level=level).order_by('usa_rank')[5:9]
                university_l = high_University.objects.filter(level=level).order_by('usa_rank')[9:]
                HighSchoolObject = HighSchoolFormModel(first_name=studentFName,
                                               last_name=studentLName,
                                               cell_phone_number=cell_phone_number,
                                               intention_country=intention_countryName,
                                               intention_school=intention_school,
                                               graduate_school=highSchool,
                                               GPA_high=GPA_high,
                                               GPA_middle=GPA_middle,
                                               score_IELT=IELT_Total,
                                               awards=awards,
                                               talentStudent=Special, recommendations=Recomm_Total,
                                               )
                return render(request, "highResultUK.html",
                              {   "studentFName":studentFName,
                                  "studentLName":studentLName,
                                  "university_h": university_h,
                                  "university_m": university_m, "university_l": university_l,
                                   "country": intention_countryName,
                                   "GPA_level": GPA_level,
                                   "IELTS_TOEFL_level": IELTS_TOEFL_level,
                                   "IELTS_TOEFL_good": IELTS_TOEFL_good ,
                                   "GPA_good": GPA_good,
                                  "no_high": no_high,
                                  "no_mid": no_mid,
                                  "no_low": no_low,
                               })

            #HighSchoolObject.save()
            # return render(request, "highResultUK.html",
            #                   {   "studentFName":studentFName,
            #                       "studentLName":studentLName,
            #                       "university_h": university_h,
            #                       "university_m": university_m, "university_l": university_l,
            #                        "country": intention_countryName,
            #                        "GPA_level": GPA_level,
            #                        "IELTS_TOEFL_level": IELTS_TOEFL_level,
            #                        "IELTS_TOEFL_good": IELTS_TOEFL_good ,
            #                        "GPA_good": GPA_good,
            #                       "no_high": no_high,
            #                       "no_mid": no_mid,
            #                       "no_low": no_low,
            #                    })
        else:
            return render(request, 'highAssessmentUK.html', {"form": form})
    else:
        form = HighSchoolFormUK()
        return render(request, 'highAssessmentUK.html', {"form": form})

def highResultCA(request):
    if request.method == "POST":
        form = HighSchoolFormCA(request.POST)
        if form.is_valid():
            studentFName = form.cleaned_data['first_name']
            studentLName = form.cleaned_data['last_name']
            if studentFName is None:
                studentFName = ''
            if studentLName is None:
                studentLName = ''

            cell_phone_number = form.cleaned_data['cell_phone_number']

            intention_countryName = form.cleaned_data['intention_country'].encode("utf-8")  # 国家名字如果不使用encode的话就是Unicode编码，但是使用encode之后还不是中文。。。
            for coun in countries_list:
                if coun["name"] == intention_countryName:  # coun["name"]不是unicode编码，因此如果intention_countryName不使用encode的话是unicode编码，两者无法比较
                    intention_countryId = coun["id"]  # intention_countryId 国家Id

            # print(intention_countryName)
            # 想去的学校
            intention_school = request.POST.get("intention_school")
            highSchool = request.POST.get("graduate_school")
            # GPA
            GPA_high = float(form.cleaned_data['GPA_high'])
            GPA_middle = form.cleaned_data['GPA_middle']
            # 雅思
            IELT_Total = float(form.cleaned_data['score_all'])  # 总分
            # print(IELT_Total)
            listen = float(form.cleaned_data['score_listen'])
            speak = float(form.cleaned_data['score_speak'])
            read = float(form.cleaned_data['score_read'])
            write = float(form.cleaned_data['score_write'])
            # print(listen)
            # 获取加分项

            awards = form.cleaned_data['awards']
            Recomm_Total = form.cleaned_data['recommendations']

            Special= form.cleaned_data['talentStudent']

            if awards!='':
                artwork=100
            else:
                artwork=0

            if GPA_high  is not None:
                GPA_high = float(GPA_high)
            if GPA_middle  is not None:
                GPA_middle = float(GPA_middle)
            if IELT_Total  is not None:
                IELT_Total = float(IELT_Total)
            GPA_good = False
            GPA_level=1

            if highSchool==1:
                guscore=6
            elif highSchool==2:
                guscore=5
            elif highSchool==3:
                guscore=3
            elif highSchool==4:
                guscore=2
            else:
                guscore=0

            # 转换GPA的值
            if GPA_high >= 3.8:
                GPA_Trans = 100
            elif GPA_high >= 3.7:
                GPA_level = 1
                GPA_good = True
                GPA_Trans = 95
            elif GPA_high >= 3.7:
                GPA_level = 1
                GPA_good = True
                GPA_Trans = 90
            elif GPA_high >= 3.65:
                GPA_level = 2
                GPA_Trans = 90
            elif GPA_high >= 3.5:
                GPA_level = 3
                GPA_Trans = 80
            elif GPA_high >= 3.0:
                GPA_level = 3
                GPA_Trans = 70
            else:
                GPA_level = 5
                GPA_Trans = 60
            # 计算IELT的值
            # 计算语言成绩：雅思/托福
            yt_Listening = 1
            yt_Speaking = 1
            yt_Reading = 1
            yt_Writing = 1
            yt_flag = 0
            IELTS_TOEFL_good = False
            IELTS_TOEFL_level=1
            if IELT_Total > 10:  # 说明是托福成绩
                if IELT_Total > 110:
                    IELTS_TOEFL_level = 1
                    IELTS_TOEFL_good = True
                    IELTS_TOEFL_Trans = 100
                elif IELT_Total > 100:
                    IELTS_TOEFL_level = 2
                    IELTS_TOEFL_Trans = 95
                elif IELT_Total > 90:
                    IELTS_TOEFL_level = 3
                    IELTS_TOEFL_Trans = 85
                elif IELT_Total > 80:
                    IELTS_TOEFL_level = 3
                    IELTS_TOEFL_Trans = 75
                else:
                    IELTS_TOEFL_level = 4
                    IELTS_TOEFL_Trans = 70
                if (listen < 22):
                    yt_Listening = 0
                    yt_flag = 1
                if (speak < 22):
                    yt_Speaking = 0
                    yt_flag = 1
                if (read < 22):
                    yt_Reading = 0
                    yt_flag = 1
                if (write< 22):
                    yt_Writing = 0
                    yt_flag = 1
            else:
                if IELT_Total >= 8.0:
                    IELTS_TOEFL_level = 1
                    IELTS_TOEFL_good = True
                    IELTS_TOEFL_Trans = 100
                elif IELT_Total >= 7.5:
                    IELTS_TOEFL_level = 2
                    IELTS_TOEFL_Trans = 90
                elif IELT_Total >= 6.5:
                    IELTS_TOEFL_level = 3
                    IELTS_TOEFL_Trans = 80
                else:
                    IELTS_TOEFL_level = 4
                    IELTS_TOEFL_Trans = 70
                if (listen < 6.0):
                    yt_Listening = 0
                    yt_flag = 1
                if (speak< 6.0):
                    yt_Speaking = 0
                    yt_flag = 1
                if (read < 6.0):
                    yt_Reading = 0
                    yt_flag = 1
                if (write < 6.0):
                    yt_Writing = 0
                    yt_flag = 1

            sum = 0.0
            addscore=0
            if GPA_high>GPA_middle:
                addscore=2
            if Special== 2: #不是特长生
                sum=float(GPA_Trans*0.6)+float(IELTS_TOEFL_Trans*0.3)+addscore+int(Recomm_Total)+guscore
            else:
                sum = float(GPA_Trans*0.15)+float(IELTS_TOEFL_Trans*0.4)+addscore+int(Recomm_Total)+artwork*0.3+guscore

            if sum>=92:
                level = 1
            elif sum>=82:
                level = 2
            else:
                level = 3
            no_high = 0
            no_mid = 0
            no_low = 0
            #u=high_University.objects.all();

            if intention_countryName==b'CAN':
                if sum >= 92:
                    level = 1
                elif sum >= 82:
                    level = 2
                else:
                    level = 3
                no_high = 0
                no_mid = 0
                no_low = 0
                university_h = high_University_CA.objects.filter(level=level).order_by('in_rank')[0:3]
                university_m = high_University_CA.objects.filter(level=level).order_by('in_rank')[3:6]
                university_l = high_University_CA.objects.filter(level=level).order_by('in_rank')[6:]

            elif intention_countryName==b'ENG':
                if Special == 2:  # 不是特长生
                    sum = float(GPA_Trans * 0.6) + float(IELTS_TOEFL_Trans * 0.3) + addscore + int(
                        Recomm_Total) + guscore
                else:
                    sum = float(GPA_Trans * 0.15) + float(IELTS_TOEFL_Trans * 0.4) + addscore + int(Recomm_Total) + artwork * 0.3 + guscore+12;
                print(sum)
                if sum >= 91:
                    level = 1
                elif sum >= 72:
                    level = 2
                else:
                    level = 3
                no_high = 0
                no_mid = 0
                no_low = 0
                university_h = high_University_UK.objects.filter(level=level).order_by('in_rank')[0:4]
                university_m = high_University_UK.objects.filter(level=level).order_by('in_rank')[4:8]
                university_l = high_University_UK.objects.filter(level=level).order_by('in_rank')[8:]
            # elif intention_countryName==b'ENG':
            #     ukscore = float(request.POST.get("ukscore"))
            #     sumUK = 0.0
            #     if Special == 2:  # 不是特长生
            #         sumUK = float(GPA_Trans * 0.6) + float(ukscore * 0.15) + addscore + int(Recomm_Total) + guscore
            #     else:
            #         sumUK= float(GPA_Trans * 0.15) + float(ukscore * 0.2)  + addscore + int( Recomm_Total) + artwork * 0.4
            #     print(sumUK)
            #     if sumUK >= 93:
            #         level = 1
            #     elif sumUK >= 83:
            #         level = 2
            #     else:
            #         level = 3
            #     university_h = high_University_UK.objects.filter(level=level).order_by('in_rank')[0:5]
            #     university_m = high_University_UK.objects.filter(level=level).order_by('in_rank')[5:9]
            #     university_l = high_University_UK.objects.filter(level=level).order_by('in_rank')[9:]
            else:
                satscore = float(request.POST.get("satscore"))
                sumUSA = 0.0
                if Special == 2:  # 不是特长生
                    sumUSA = float(GPA_Trans * 0.6) + float(satscore * 0.15) + float(IELTS_TOEFL_Trans * 0.15) + addscore + int(Recomm_Total) + guscore
                else:
                    sumUSA = float(GPA_Trans * 0.15) + float(satscore * 0.2) + float(IELTS_TOEFL_Trans * 0.15) + addscore + int( Recomm_Total) + artwork * 0.4
                print(sumUSA)
                if sumUSA >= 375:
                    level = 1
                elif sumUSA >= 327:
                    level = 2
                else:
                    level = 3
                university_h = high_University.objects.filter(level=level).order_by('in_rank')[0:5]
                university_m = high_University.objects.filter(level=level).order_by('in_rank')[5:10]
                university_l = high_University.objects.filter(level=level).order_by('in_rank')[10:]


            HighSchoolObject = HighSchoolFormModelCA(first_name=studentFName,
                                               last_name=studentLName,
                                               cell_phone_number=cell_phone_number,
                                               intention_country=intention_countryName,
                                               intention_school=intention_school,
                                               graduate_school=highSchool,
                                               GPA_high=GPA_high,
                                               GPA_middle=GPA_middle,
                                               score_all=IELT_Total,
                                               score_listen=listen,
                                               score_speak=speak,
                                               score_read=read,
                                               score_write=write,
                                               awards=awards,
                                               talentStudent=Special,
                                               recommendations=Recomm_Total,
                                               )

            #HighSchoolObject.save()
            return render(request, "highResultCA.html",
                              {   "studentFName":studentFName,
                                  "studentLName":studentLName,
                                  "university_h": university_h,
                                  "university_m": university_m, "university_l": university_l,
                                  # "country": intention_countryName,
                                   "GPA_level": GPA_level,
                                   "IELTS_TOEFL_level": IELTS_TOEFL_level,
                                   "IELTS_TOEFL_good": IELTS_TOEFL_good ,
                                   "GPA_good": GPA_good,
                                  "no_high": no_high,
                                  "no_mid": no_mid,
                                  "no_low": no_low,
                                  "yt_Listening": yt_Listening,
                                  "yt_Speaking": yt_Speaking,
                                  "yt_Reading": yt_Reading,
                                  "yt_Writing": yt_Writing,
                                  "yt_flag": yt_flag
                               })
        else:
            return render(request, 'highAssessmentCA.html', {"form": form})
    else:
        form = HighSchoolFormCA()
        return render(request, 'highAssessmentCA.html', {"form": form})

