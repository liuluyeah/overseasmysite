# coding:utf-8
from django import forms
from django.forms import ModelForm
from .models import UserInfoFormModel,HighSchoolFormModel,HighSchoolFormModelUK,HighSchoolFormModelCA

class UserInfoForm(ModelForm):
    class Meta:
        model=UserInfoFormModel
        fields=('first_name', 'last_name','cell_phone_number','intention_country','intention_major','ranking_in_major',
                'intention_school','graduate_school','score_GPA','score_IELTS_TOEFL','score_IT_Listening',
                'score_IT_Speaking','score_IT_Reading','score_IT_Writing','score_GRE','score_GRE_Verbal',
                'score_GRE_Quan','score_GRE_Anal','in_papers','na_papers','in_patent','na_patent','research',
                'placement','social_practice','specilty','recommendation')
        widgets={
            'first_name':forms.TextInput(attrs={'placeholder': '姓','size': '8', }),
            'last_name':forms.TextInput(attrs={'placeholder': '名','size': '14', }),
            'cell_phone_number':forms.TextInput(attrs={'placeholder': '手机号码', 'class': 'large', 'pattern': '[+]?[\.\s\-\(\)\*\#0-9]{3,}'}),
            'score_GPA':forms.TextInput(attrs={'placeholder': 'GPA(4分制)', 'class': 'large', 'pattern': '[0-9]+[\.]?[0-9]*$' }),

            'score_IELTS_TOEFL':forms.TextInput(attrs={'placeholder': '雅思/托福总分', 'class': 'medium'}),
            'score_IT_Listening':forms.TextInput(attrs={'placeholder': '听力', 'class': 'medium'}),
            'score_IT_Speaking':forms.TextInput(attrs={'placeholder': '口语', 'class': 'medium'}),
            'score_IT_Reading':forms.TextInput(attrs={'placeholder': '阅读', 'class': 'medium'}),
            'score_IT_Writing':forms.TextInput(attrs={'placeholder': '写作', 'class': 'medium'}),

            'score_GRE':forms.TextInput(attrs={'placeholder': 'GRE总分', 'class': 'medium' }),
            'score_GRE_Verbal':forms.TextInput(attrs={'placeholder': 'Verbal Reasoning', 'class': 'medium'}),
            'score_GRE_Quan':forms.TextInput(attrs={'placeholder': 'Quantitative Reasoning', 'class': 'medium'}),
            'score_GRE_Anal':forms.TextInput(attrs={'placeholder': 'Analytical Writing', 'class': 'medium'}),

            'in_papers':forms.TextInput(attrs={'placeholder': '国际期刊', 'class': 'large'}),
            'na_papers':forms.TextInput(attrs={'placeholder': '其他期刊', 'class': 'large'}),
            'in_patent':forms.TextInput(attrs={'placeholder': '国际专利', 'class': 'large'}),
            'na_patent':forms.TextInput(attrs={'placeholder': '国内专利', 'class': 'large'}),
            'research':forms.Textarea(attrs={'placeholder': '简单描述你的科研经历', 'class': 'small'}),
            'placement':forms.Textarea(attrs={'placeholder': '介绍你的工作/实习经历', 'class': 'small'}),
            'social_practice':forms.Textarea(attrs={'placeholder': '简述你做过的社会实践', 'class': 'small'}),
            'specilty':forms.Textarea(attrs={'placeholder': '你的特长', 'class': 'small'}),
            'recommendation':forms.RadioSelect(),
            #'intention_school': forms.Select(attrs={'prompt':'学校' , 'size': '14', }),
            #'graduate_school': forms.TextInput(attrs={'placeholder': '毕业院校', 'size': '14', }),
        }


class HighSchoolForm(ModelForm):
    class Meta:
        model=HighSchoolFormModel
        fields=('first_name', 'last_name','talentStudent','cell_phone_number','intention_country','intention_school',
                'graduate_school','GPA_middle','GPA_high','score_SAT','score_TOEFL','awards','research'
                ,'art','recommendations')

        widgets={
            'first_name': forms.TextInput(attrs={'placeholder': '姓', 'size': '8', }),
            'last_name': forms.TextInput(attrs={'placeholder': '名', 'size': '14', }),
            'talentStudent':forms.RadioSelect(),

            'cell_phone_number': forms.TextInput(
                attrs={'placeholder': '手机号码', 'class': 'large', 'pattern': '[+]?[\.\s\-\(\)\*\#0-9]{3,}'}),

            'GPA_middle': forms.TextInput(
                attrs={'placeholder': '初中GPA(4分制)', 'class': 'large', 'pattern': '[0-9]+[\.]?[0-9]*$'}),
            'GPA_high': forms.TextInput(
                attrs={'placeholder': '高中GPA(4分制)', 'class': 'large', 'pattern': '[0-9]+[\.]?[0-9]*$'}),

            'score_SAT': forms.TextInput(
                attrs={'placeholder': 'SAT成绩', 'class': 'large', }),
            'score_TOEFL': forms.TextInput(
                attrs={'placeholder': '托福成绩', 'class': 'large',}),

            'awards': forms.Textarea(attrs={'placeholder': '具备专业特长者需填写此项', 'class': 'small'}),
            # 'research': forms.Textarea(attrs={'placeholder': '专业特长者至少填写一项', 'class': 'small'}),
            # 'art': forms.Textarea(attrs={'placeholder': '专业特长者至少填写一项', 'class': 'small'}),

            'recommendations': forms.TextInput(
                attrs={'placeholder': '请输入推荐信数目', 'class': 'large', }),
        }

class HighSchoolFormUK(ModelForm):
    class Meta:
        model=HighSchoolFormModelUK
        fields=('first_name', 'last_name','talentStudent','cell_phone_number','intention_country','intention_school',
                'graduate_school','GPA_middle','GPA_high','score_IELT','awards','research','score_SAT','score_TOEFL'
                ,'score_all','score_listen','score_speak','score_read','score_write','art','recommendations')

        widgets={
            'first_name': forms.TextInput(attrs={'placeholder': '姓', 'size': '8', }),
            'last_name': forms.TextInput(attrs={'placeholder': '名', 'size': '14', }),
            'talentStudent':forms.RadioSelect(),

            'cell_phone_number': forms.TextInput(
                attrs={'placeholder': '手机号码', 'class': 'large', 'pattern': '[+]?[\.\s\-\(\)\*\#0-9]{3,}'}),

            'GPA_middle': forms.TextInput(
                attrs={'placeholder': '初中GPA(4分制)', 'class': 'large', 'pattern': '[0-9]+[\.]?[0-9]*$'}),
            'GPA_high': forms.TextInput(
                attrs={'placeholder': '高中GPA(4分制)', 'class': 'large', 'pattern': '[0-9]+[\.]?[0-9]*$'}),

            'score_IELT': forms.TextInput(
                attrs={'placeholder': '雅思成绩', 'class': 'medium', }),
            # 'score_TOEFL': forms.TextInput(
            #     attrs={'placeholder': '托福成绩', 'class': 'medium',}),
            #美国
            'score_SAT': forms.TextInput(
                attrs={'placeholder': 'SAT成绩', 'class': 'medium', }),
            'score_TOEFL': forms.TextInput(
                attrs={'placeholder': '托福成绩', 'class': 'medium', }),
            #加拿大
            'score_all': forms.TextInput(
                attrs={'placeholder': '总分', 'class': 'medium', }),
            'score_listen': forms.TextInput(
                attrs={'placeholder': '听力', 'class': 'medium', }),
            'score_speak': forms.TextInput(
                attrs={'placeholder': '口语', 'class': 'medium', }),
            'score_read': forms.TextInput(
                attrs={'placeholder': '阅读', 'class': 'medium', }),
            'score_write': forms.TextInput(
                attrs={'placeholder': '写作', 'class': 'medium', }),

            'awards': forms.Textarea(attrs={'placeholder': '具备专业特长者需填写此项', 'class': 'small'}),
            'research': forms.Textarea(attrs={'placeholder': '专业特长者至少填写一项', 'class': 'small'}),
            'art': forms.Textarea(attrs={'placeholder': '专业特长者至少填写一项', 'class': 'small'}),

            'recommendations': forms.TextInput(
                attrs={'placeholder': '请输入推荐信数目', 'class': 'large', }),
        }

class HighSchoolFormCA(ModelForm):
    class Meta:
        model=HighSchoolFormModelCA
        fields=('first_name', 'last_name','talentStudent','cell_phone_number','intention_country','intention_school',
                'graduate_school','GPA_middle','GPA_high','score_all','score_listen','score_speak','score_read','score_write','awards','research'
                ,'art','recommendations')

        widgets={
            'first_name': forms.TextInput(attrs={'placeholder': '姓', 'size': '8', }),
            'last_name': forms.TextInput(attrs={'placeholder': '名', 'size': '14', }),
            'talentStudent':forms.RadioSelect(),

            'cell_phone_number': forms.TextInput(
                attrs={'placeholder': '手机号码', 'class': 'large', 'pattern': '[+]?[\.\s\-\(\)\*\#0-9]{3,}'}),

            'GPA_middle': forms.TextInput(
                attrs={'placeholder': '初中GPA(4分制)', 'class': 'large', 'pattern': '[0-9]+[\.]?[0-9]*$'}),
            'GPA_high': forms.TextInput(
                attrs={'placeholder': '高中GPA(4分制)', 'class': 'large', 'pattern': '[0-9]+[\.]?[0-9]*$'}),
            'score_all': forms.TextInput(
                attrs={'placeholder': '总分', 'class': 'medium', }),
            'score_listen': forms.TextInput(
                attrs={'placeholder': '听力', 'class': 'medium', }),
            'score_speak': forms.TextInput(
                attrs={'placeholder': '口语', 'class': 'medium',}),
            'score_read': forms.TextInput(
                attrs={'placeholder': '阅读', 'class': 'medium', }),
            'score_write': forms.TextInput(
                attrs={'placeholder': '写作', 'class': 'medium', }),
            # eng
            # 'score_IELT': forms.TextInput(
            #     attrs={'placeholder': '雅思成绩', 'class': 'medium', }),

            'awards': forms.Textarea(attrs={'placeholder': '专业特长者需填写此项', 'class': 'small'}),

            'recommendations': forms.TextInput(
                attrs={'placeholder': '请输入推荐信数目', 'class': 'large', }),
        }