import random


def workerModel(worker):
    return ({
        "id": worker.fileid,
        "name": worker.worker_name,
        "sex": worker.sex,
        "age": worker.age,
        "education": worker.edu_level,
        "college": worker.edu_school
    })


def jobModel(job):
    return ({
        "jname": job.jname,  # 工作名称
        "jneed_age": job.jneed_age,  # 年龄要求 25表示25岁以上 -25 表示25岁以下
        "jneed_edu": job.jneed_edu,  # 教育要求
        "jneed_year": job.jneed_year,  # 工作经验
        "jneed_other": job.jneed_other,  # 其他所有的要求
    })


def infoModel(worker):
    return ({
        "fileid": worker.fileid,
        "worker_name": worker.worker_name,
        "sex": worker.sex,
        "age": worker.age,
        "phone_number": worker.phone_number,
        "e_mail": worker.e_mail,
        "location": worker.location,
        "edu_school": worker.edu_school,
        "edu_level": worker.edu_level,
        "work_year": worker.work_year,
        "statue": worker.statue,
        "hash_code": worker.hash_code
    })


def addScore(score, a, b):
    return score + round(random.uniform(a, b), 2)


def getScore(worker):
    score = 0.0
    if len(worker.worker_name) != 0: addScore(score, 15, 20)
    if len(worker.sex) != 0: addScore(score, 5, 10)
    if len(worker.age) != 0: addScore(score, 5, 10)
    if len(worker.phone_number) != 0: addScore(score, 5, 10)
    if len(worker.e_mail) != 0: addScore(score, 5, 10)
    if len(worker.location) != 0: addScore(score, 5, 10)
    if len(worker.edu_school) != 0: addScore(score, 5, 10)
    if len(worker.edu_level) != 0: addScore(score, 5, 10)
    if worker.work_year > 0: addScore(score, 5, 10)
    return score
