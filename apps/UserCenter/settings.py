Names = {"姓名", "名字", "皇甫", "司马", "南宫",
         "侯", "谢", "阮", "李", "王", "张", "赵", "刘", "陈", "杨", "黄", "赵",
         "周", "吴", "魏", "林", "江", "胡", "冯", "罗", "杜", "朱", "孙", "钱",
         "叶", "武", "郑", "燕", "蒋", "毛", "康", "田", "梁", "史", "穆", "宋",
         "唐", "连", "吴", "肖", "关", "高", "万", "何", "袁", "路", "曹", "徐",
         "贾", "苏", "吕", "樊", "马", "邢", "宇", "雨", "欣", "佳", "思", "闫",
         "靳", "沈", "华", "寇", "薛", "于", "玉", "豪", "郭", "方", "董", "金",
         "黄", "梁", "申", "凌", "康", "原", "傅", "姚", "管", "邝", "韩", "卢",
         "陆", "严", "梅", "尹", "尚", "阳", "常", "闻", "乔", "邱", "钟", "余",
         "裴", "栗", "元", "秦", "赖", "景", "戴", "骆", "范", "段", "游", "滕",
         "洪", "鸿", "潘", "白", "荆", "高", "玲", "雷", "汪", "俞", "石", "武"}


Sex = {"性别", "男", "女"}

Age = {"生日", "出生", "年龄", "岁"}

Phone_number = {"电话", "手机", "话:", "话：", "机:", "机：", "联系"}

E_mail = {"邮箱", "邮件", "箱:", "箱：", "@"}

Location = {"籍贯", "地址", "地点", "住址", "省"}

Edu_school = {"毕业院校", "大学", "学院", "中专", "学校", "中学", "高中"}

Edu_level = {"学历", "博士", "硕士", "本科", "专科", "大专", "中专"}

Statue = {"政治面貌", "群面", "党员", "团员", "群众"}

Skills = {"办公软件", "技能", "软件", "EXCEL", "Excel", "excel", "PPT", "ppt",
          "WORD", "Word", "word", "PS", "Ps", "PhotoShop", "Office", "WPS"}

JobHunt = {"求职"}

Self = {"自我评价"}

Award = {"获奖", "奖", "证书", "大赛", "班长", "班干", "会长", "优秀", "三好", "称号",
         "标兵", "普通话", "冠军", "亚军", "季军", "优胜", "省赛", "国赛", "奥林匹克",
         "技能", "全国大学生", "竞赛", "良好", "征文", "演讲", "省级", "国家级", "等级",
         "大学英语", "数学", "教育"}

Action = {"组织", "策划", "团队", "领导", "公司", "俱乐部", "管理", "集团", "工作经历", "工作经验"}

workFlag = {"工作经历", "工作经验"}

Noneed = {'的', '团', '地', '了', ':', '：', '上', '.', '。', ';', '；', '，', ',',
          '、', '）', '（', '(', ')'}

Flag = {":", "："}

Charfxxk = {";", "；", "*", '.', '。', ';', '；', '，', ',',
            '、', '）', '（', '(', ')', '/', '|', '\\', "简历", "工作室", "。"}

Shit = {"大学生", "党"}

Special_rules = {"北京", "朝阳区", "健康", "旅游", "科技", "主管", "奖", "旅行", "善于", "医院", "简单", "上海", "国家", "酒店", "思想",
                 "奈森", "教育", "个人简介", "职业", "武汉", "广东", "关于", "关注", "设计", "专业", "高级", "汽车", "于是", "教育背景", "广州",
                 "游泳", "意向", "职业名称", "工具", "游戏", "江西", "苏州", "物业", "湖北", "学历", "中心", "个人背景", "个人简历", "工作", "营销",
                 "爱好", "中心", "相关", "工作"}

Noname = Sex | Location | Edu_school | Edu_level | Statue | Skills | Award | Action | Charfxxk | Phone_number | Special_rules

Noschool = Sex | Location | Statue | Skills| Award | Charfxxk | Shit

regex = r"^(19\d{2}|20\d{2}|2100)\.(0?[1-9]|1[012])\.(0?[1-9]|[12][0-9]|3[01])$"
