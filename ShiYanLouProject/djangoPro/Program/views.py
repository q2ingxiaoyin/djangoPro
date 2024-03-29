import random
from pypinyin import lazy_pinyin
from django.shortcuts import render,HttpResponse
from django.shortcuts import render_to_response
from Program.models import *
# Create your views here.

def index(request):
    """
    首页
    :param request:
    :return:
    """
    return render_to_response("index.html")

def andplan(request):

    for i in range(10000):
        plan = Plan()
        plan_level = ["入门","初级工程师","中级工程师","高级工程师"]
        plan_project = ["python","java","UI","linux","php","信息安全","c++"]
        name = random.choice(plan_project)+random.choice(plan_level)
        plan.name = name
        plan.description = "%s 真是好"%name
        plan.image = "img/%s.png"%(random.randint(100,999))
        plan.save()
    return HttpResponse('注册完成了')


def addUser(request):
    for i in range(1000):
        last_name ="赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤"
        first_name = "澄邈、德泽、海超、海阳、海荣、海逸、海昌、瀚钰、瀚文、涵亮、涵煦、明宇、涵衍、浩皛、浩波、浩博、浩初、浩宕、浩歌、浩广、浩邈、浩气、浩思、浩言、鸿宝、鸿波、鸿博、鸿才、鸿畅、鸿畴、鸿达、鸿德、鸿飞、鸿风、鸿福、鸿光、鸿晖、鸿朗、鸿文、鸿轩、鸿煊、鸿骞、鸿远、鸿云、鸿哲、鸿祯、鸿志、鸿卓、嘉澍、光济、澎湃、彭泽、鹏池、鹏海、浦和、浦泽、瑞渊、越泽、博耘、德运、辰宇、辰皓、辰钊、辰铭、辰锟、辰阳、辰韦、辰良、辰沛、晨轩、晨涛、晨濡、晨潍、鸿振、吉星、铭晨、起运、运凡、运凯、运鹏、运浩、运诚、运良、运鸿、运锋、运盛、运升、运杰、运珧、运骏、运凯、运乾、维运、运晟、运莱、运华、耘豪、星爵、星腾、星睿、星泽、星鹏、星然、震轩、震博、康震、震博、振强、振博、振华、振锐、振凯、振海、振国、振平、昂然、昂雄、昂杰、昂熙、昌勋、昌盛、昌淼、昌茂、昌黎、昌燎、昌翰、晨朗、德明、德昌、德曜、范明、飞昂、高旻、晗日、昊然、昊天、昊苍、昊英、昊宇、昊嘉、昊明、昊伟、昊硕、昊磊、昊东、鸿晖、鸿朗、华晖、金鹏、晋鹏、敬曦、景明、景天、景浩、俊晖、君昊、昆琦、昆鹏、昆纬、昆宇、昆锐、昆卉、昆峰、昆颉、昆谊、昆皓、昆鹏、昆明、昆杰、昆雄、昆纶、鹏涛、鹏煊、曦晨、曦之、新曦、旭彬、旭尧、旭鹏、旭东、旭炎、炫明、宣朗、学智、轩昂、彦昌、曜坤、曜栋、曜文、曜曦、曜灿、曜瑞、智伟、智杰、智刚、智阳、昌勋、昌盛、昌茂、昌黎、昌燎、昌翰、晨朗、昂然、昂雄、昂杰、昂熙、范明、飞昂、高朗、高旻、德明、德昌、德曜、智伟、智杰、智刚、智阳、瀚彭、旭炎、宣朗、学智、昊然、昊天、昊苍、昊英、昊宇、昊嘉、昊明、昊伟、鸿朗、华晖、金鹏、晋鹏、敬曦、景明、景天、景浩、景行、景中、景逸、景彰、昆鹏、昆明、昆杰、昆雄、昆纶、鹏涛、鹏煊、景平、俊晖、君昊、昆琦、昆鹏、昆纬、昆宇、昆锐、昆卉、昆峰、昆颉、昆谊、轩昂、彦昌、曜坤、曜文、曜曦、曜灿、曜瑞、曦晨、曦之、新曦、鑫鹏、旭彬、旭尧、旭鹏、旭东、浩轩、浩瀚、浩慨、浩阔、鸿熙、鸿羲、鸿禧、鸿信、泽洋、泽雨、哲瀚、胤运、佑运、允晨、运恒、运发、云天、耘志、耘涛、振荣、振翱、中震、子辰、晗昱、瀚玥、瀚昂、瀚彭、景行、景中、景逸、景彰、绍晖、文景、曦哲、永昌、子昂、智宇、智晖、晗日、晗昱、瀚昂、昊硕、昊磊、昊东、鸿晖、绍晖、文昂、文景、曦哲、永昌、子昂、智宇、智晖、浩然、鸿运、辰龙、运珹、振宇、高朗、景平、鑫鹏、昌淼、炫明、昆皓、曜栋、文昂、恨桃、依秋、依波、香巧、紫萱、涵易、忆之、幻巧、美倩、安寒、白亦、惜玉、碧春、怜雪、听南、念蕾、紫夏、凌旋、芷梦、凌寒、梦竹、千凡、丹蓉、慧贞、思菱、平卉、笑柳、雪卉、南蓉、谷梦、巧兰、绿蝶、飞荷、佳蕊、芷荷、怀瑶、慕易、若芹、紫安、曼冬、寻巧、雅昕、尔槐、以旋、初夏、依丝、怜南、傲菡、谷蕊、笑槐、飞兰、笑卉、迎荷、佳音、梦君、妙绿、觅雪、寒安、沛凝、白容、乐蓉、映安、依云、映冬、凡雁、梦秋、梦凡、秋巧、若云、元容、怀蕾、灵寒、天薇、翠安、乐琴、宛南、怀蕊、白风、访波、亦凝、易绿、夜南、曼凡、亦巧、青易、冰真、白萱、友安、海之、小蕊、又琴、天风、若松、盼菡、秋荷、香彤、语梦、惜蕊、迎彤、沛白、雁彬、易蓉、雪晴、诗珊、春冬、晴钰、冰绿、半梅、笑容、沛凝、映秋、盼烟、晓凡、涵雁、问凝、冬萱、晓山、雁蓉、梦蕊、山菡、南莲、飞双、凝丝、思萱、怀梦、雨梅、冷霜、向松、迎丝、迎梅、雅彤、香薇、以山、碧萱、寒云、向南、书雁、怀薇、思菱、忆文、翠巧、书文、若山、向秋、凡白、绮烟、从蕾、天曼、又亦、从语、绮彤、之玉、凡梅、依琴、沛槐、又槐、元绿、安珊、夏之、易槐、宛亦、白翠、丹云、问寒、易文、傲易、青旋、思真、雨珍、幻丝、代梅、盼曼、妙之、半双、若翠、初兰、惜萍、初之、宛丝、寄南、小萍、静珊、千风、天蓉、雅青、寄文、涵菱、香波、青亦、元菱、翠彤、春海、惜珊、向薇、冬灵、惜芹、凌青、谷芹、雁桃、映雁、书兰、盼香、梅致、寄风、芳荷、绮晴、映之、醉波、幻莲、晓昕、傲柔、寄容、以珊、紫雪、芷容、书琴、美伊、涵阳、怀寒、易云、代秋、惜梦、宇涵、谷槐、怀莲、英莲、芷卉、向彤、新巧、语海、灵珊、凝丹、小蕾、迎夏、慕卉、飞珍、冰夏、亦竹、飞莲、秋月、元蝶、春蕾、怀绿、尔容、小玉、幼南、凡梦、碧菡、初晴、宛秋、傲旋、新之、凡儿、夏真、静枫、芝萱、恨蕊、乐双、念薇、靖雁、菊颂、丹蝶、元瑶、冰蝶、念波、迎翠、海瑶、乐萱、凌兰、曼岚、若枫、傲薇、雅芝、乐蕊、秋灵、凤娇、觅云、依伊、恨山、从寒、忆香、香菱、静曼、青寒、笑天、涵蕾、元柏、代萱、紫真、千青、雪珍、寄琴、绿蕊、荷柳、诗翠、念瑶、兰楠、曼彤、怀曼、香巧、采蓝、芷天、尔曼、巧蕊".split("、")
        nickname = random.choice(last_name)+random.choice(first_name)
        e_name = "".join(lazy_pinyin(nickname)).title()
        email = "%s@qq.com"%e_name
        password = e_name
        user = User()
        user.nickname = nickname
        user.email = email
        user.password = password
        user.plan = random.choice(Plan.objects.filter(id__lt=1000))
        user.save()
    return HttpResponse('注册完成了')

def addLesson(request):
    for i in range(1000):
        lesson_level = ['入门','初级','中级','高级']
        lesson_probject = ["python","java","UI","linux","php","信息安全","c++"]
        lable = random.choice(lesson_probject)+random.choice(lesson_level)
        lession = Lesson()
        lession.lable =lable
        lession.picture = "img/%s.png"%(random.randint(100,999))
        lession.show_number = random.randint(0, 99999)
        lession.save()
        for i in range(random.randint(2,7)):
            lession.plan.add(
                random.choice(Plan.objects.filter(id__lt=100))
            )
        lession.save()
    return HttpResponse('注册完成了')

def deleta(request):
    Lesson.objects.all().delete()
    return HttpResponse('删除成功')


def select(request):
    #查询所有用户
    # user_list = User.objects.all()
    # user_list = User.objects.raw("select * from Program_user")
    #查询用户的规划    多查一
    # user = User.objects.get(id=5)
    #查询拥有C++高级工程师规划的所有的用户
    # lst = []
    # plan = Plan.objects.filter(name='c++高级工程师')
    # for i in plan:
    #     for j in i.user_set.all():
    #         lst.append(j.nickname)
    #查询id=29相关联的所有用户 一查多
    # plan = Plan.objects.get(id=777)#.user_set.all()
    #查询id=40的规划所包含的课程
    plan = Plan.objects.get(id=40).lesson_set.all()
    return render_to_response("empty.html",locals())










