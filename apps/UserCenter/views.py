from rest_framework.response import Response
from rest_framework.views import APIView
from UserCenter.models import mycol
from UserCenter.serializer import *
from UserCenter.tools import *


class loadUserInfo(APIView):
    def post(self, request):
        # Worker 字段字典
        Person = tools_person
        Person = newPerson(Person)

        # 用于分析的字段
        anaPerson = tools_anaperson
        anaPerson = newAnaPerson(anaPerson)
        token = request.data["token"]

        userid = confirmUser(token)
        if userid == -1:
            return Response({
                "error": "user token not existed"
            })

        Person["fileid"] = request.data["id"]
        param = request.data["conList"]

        flag_num = False
        flag_work = False
        flag_now = False
        work_years = []

        # 匹配字段
        for i in range(0, len(param)):
            str = param[i]["words"]
            if i == 0:
                Person["worker_name"] = str
            flag = idx(str)
            res = str[flag:]
            if check(str, Names) and len(res) <= 4 and 2 <= len(str) <= 7 and not check(str, Noname):
                if flag == -1:
                    Person["worker_name"] = str
                else:
                    if 2 <= len(res) <= 4:
                        Person["worker_name"] = res
                # 检查姓名
                Person["worker_name"] = check_worker_name(Person["worker_name"])
            if check(str, Sex):
                Person["sex"] = check_sex(str)
                
            if check(str, Age) or birthdata(str):
                Person["age"] = str if flag == -1 else res
                Person["age"] = find_numbers(Person["age"])
                
                continue
            if flag_num == False:
                if check(str, Phone_number) and not check(str, Edu_school | Edu_level):
                    if len(str) >= 7:
                        Person["phone_number"] = str if flag == -1 else res
                        # 检查 phone_number 是否符合格式
                        Person["phone_number"] = check_phone(Person["phone_number"])
                        flag_num = good_phone(Person["phone_number"])
                    
            if check(str, E_mail):
                if len(str) > 5:
                    Person["e_mail"] = str if flag == -1 else res
                
            if check(str, Location) and not check(str, Edu_school | Award) and len(str) <= 13:
                Person["location"] = str if flag == -1 else res
                
            if check(str, Edu_school) and len(str) <= 13 and not check(str, Noschool):
                Person["edu_school"] = str if flag == -1 else res
                
            if check(str, Edu_level):
                str = str if flag == -1 else res
                if len(str) > 2:
                    for tag in Edu_level:
                        if tag in str:
                            str = tag
                            if str == "专科":
                                str = "大专"
                            break
                Person["edu_level"] = str
                
            if check(str, Statue):
                str = str if flag == -1 else res
                if len(str) > 2:
                    for tag in Statue:
                        if tag in str:
                            str = tag
                            break
                Person["statue"] = str
                
            if check(str, Skills) and not check(str, Award):
                anaPerson["skills"] += str if flag == -1 else res
                
            if check(str, JobHunt):
                anaPerson["jobHunt"] = str if flag == -1 else res
                
            if check(str, Award) and not check(str, Skills | Action):
                anaPerson["award"] += str if flag == -1 else res
                
            if check(str, Action) and len(str) >= 3 and check(str, Flag) == False:
                anaPerson["self"] += str
            if check(str, workFlag): flag_work = True
            if "至今" in str: flag_now = True
            if flag_work:
                dates = extract_dates(str)
                work_years.extend(dates)
        # 检查 worker_name 是否符合格式
        Person["worker_name"] = check_name(Person["worker_name"], param)
        # 对所有日期从小到大排序
        work_years.sort(key=lambda x: tuple(map(int, x.split('.'))))
        # 添加至今的日期
        if flag_now:
            work_years.append(datetime.now().strftime("%Y.%m.%d"))
        # 计算工作经历
        work_year = calculate_work_year(work_years)
        if work_year > 10:
            if Person["edu_level"] == "本科": work_year -= 4
        Person["work_year"] = work_year
        # 计算年龄
        Person["age"] = calculate_age(Person["age"])
        # 计算该 worker 的 hash_code
        hash_code = hash_token(Person)
        # 查询是否存在 Worker
        Worker = check_has(hash_code)
        if Worker:
            return Response({
                "error": "worker existed"
            })
        else:
            Person["hash_code"] = hash_code
            # 将 Person 序列化
            Worker = Worker_Serializer(Person)
            # 插入一条 Worker 记录
            models.Worker.objects.create(**Worker.data)
            wid = check_has(hash_code).wid
            anaPerson["id"] = wid
            anaPerson["_id"] = hash_code
            have = {
                "uid": userid,
                "wid": wid
            }
            # 将关系序列化
            Have = Have_Serializer(have)
            models.Have.objects.create(**Have.data)
            # 将 anaPerson 存入 MongoDB
            mycol.insert_one(anaPerson)

        return Response({
            "success": "ok"
        })


class addWorkNeed(APIView):
    def post(self, request):
        param = request.data
        hash_code = hash_work(param)
        Work = check_work(hash_code)
        Job = {
            "jname": param['jname'],  # 工作名称
            "jneed_age": param['jneed_age'],  # 年龄要求 25表示25岁以上 -25 表示25岁以下
            "jneed_edu": param['jneed_edu'],  # 教育要求
            "jneed_year": param['jneed_year'],  # 工作经验
            "jneed_other": param['jneed_other'],  # 其他所有的要求
            "hash_code": ""
        }
        if Work:
            return Response({
                "error": "The work has existed"
            })
        else:
            Job['hash_code'] = hash_code
            Job = Job_Serializer(Job)
            models.Job.objects.create(**Job.data)
            return Response(Job.data)
