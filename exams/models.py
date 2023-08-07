from django.db import models
import uuid
# Create your models here.

class Exam(models.Model):
    exam_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    qualgbcd = models.CharField(max_length=100) #자격구분
    qualgbnm = models.CharField(max_length=100) #자격구분명
    seriescd = models.IntegerField() #계열코드
    seriesnm = models.CharField(max_length=100) #계열명
    jmcd = models.IntegerField() #종목코드
    jmfldnm = models.CharField(max_length=100) #종목명
    obligfldcd = models.IntegerField() #대직무분야코드
    obligfldnm = models.CharField(max_length=100) #대직무분야명
    mdobligfldcd = models.IntegerField() #중직무분야코드
    mdobligfldnm = models.CharField(max_length=100) #중직무분야명
    #대직무분야코드/ 중직무분야코드 api 명세서에 없어서 일단 안넣었는데 추가여부 확인해야합니다.
    #일단 넣어놓겠습니다. 필요없으면 빼주세요.
    is_favorite = models.BooleanField(default=False)
    #default = False로 해둠 -> 일단은 즐찾이 안된 상태로 시작하니까?

class Exam_plan(models.Model):
    exam_plan_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    exam_id = models.ForeignKey(Exam,on_delete=models.CASCADE,null=False) #위에 있는 Exam모델 참조
    implYy = models.IntegerField() #시행년도
    implSeq = models.IntegerField() #시행회차
    description = models.TextField() #설명
    docRegStartDt = models.DateField() #필기시험 원서접수 시작일자
    docRegEndDt = models.DateField() #필기시험 원서접수 종료일자
    docExamStartDt = models.DateField() #필기시험 시작일자
    docExamEndDt = models.DateField() #필기시험 종료일자
    docPassDt = models.DateField() #필기시험 합격(예정)자 발표일자
    pracRegStartDt = models.DateField() #실기(작업)/면접 시험 원서접수 시작일자
    pracRegEndDt = models.DateField() #실기(작업)/면접 시험 원서접수 종료일자
    pracExamStartDt = models.DateField() #실기(작업)/면접 시험 시작일자
    pracExamEndDt = models.DateField() #실기(작업)/면접 시험 종료일자
    pracPassDt = models.DateField() #실기(작업)/면접 합격자 발표일자