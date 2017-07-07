import sys
import os

def capitalize(old):
    """
    首字母大写，不改变传入字符串中其他位置的字符
    """
    return old[0].upper() + old[1:]

TEMPLATE_SERVICE_PATH = sys.path[0] + "/template/ServiceTemplate.java"
TEMPLATE_ISERVICE_PATH = sys.path[0] + "/template/IServiceTemplate.java"
TEMP_PATH = sys.path[0] + "/temp"

PACKAGE = ""
OBJECT = ""
OBJECTS = []

if __name__ == "__main__":
    # 设置包名
    while True:
        PACKAGE = input("Please input package name.").lower()
        if PACKAGE is None or PACKAGE == "":
            PACKAGE = input("Package name is None. Please input again.").lower()
        else:
            break
    # 设置对象名
    while True:
        OBJECT = input("Please input object name.")
        if OBJECT is None or OBJECT == "":
            OBJECT = input("Object name is None. Please input again.")
        else:
            break

    if OBJECT.find(","):
        OBJECTS = OBJECT.split(",")
    else:
        OBJECTS.append(OBJECT)

    # 获取 Service 模板
    serviceTemplateFile = open(TEMPLATE_SERVICE_PATH)
    serviceTemplateContent = ""
    for line in serviceTemplateFile.readlines():
        serviceTemplateContent += line
    serviceTemplateFile.close()
    # 获取 IService 模板
    ISserviceTemplateFile = open(TEMPLATE_ISERVICE_PATH)
    IServiceTemplateContent = ""
    for line in ISserviceTemplateFile.readlines():
        IServiceTemplateContent += line
    ISserviceTemplateFile.close()

    # 遍历 OBJETCS 生成文件
    for obj in OBJECTS:
        # 对模板内容进行替换
        serviceContent = serviceTemplateContent.replace("#{package}", PACKAGE).replace("#{object}", capitalize(obj)).replace("#{object_lower}", obj)
        IServiceContent = IServiceTemplateContent.replace("#{package}", PACKAGE).replace("#{object}", capitalize(obj)).replace("#{object_lower}", obj)
        GENERATOR_PATH = "%s/%s"%(TEMP_PATH, capitalize(obj))
        print("%s created."%(GENERATOR_PATH))
        if not os.path.exists(GENERATOR_PATH):
            os.mkdir(GENERATOR_PATH)
        # 创建 service 文件
        serviceFilePath = GENERATOR_PATH + "/%sService.java"%(capitalize(obj))
        serviceFile = open(serviceFilePath, "w")
        serviceFile.write(serviceContent)
        serviceFile.close()

        # 创建 IService 文件
        IServiceFilePath = GENERATOR_PATH + "/I%sService.java"%(capitalize(obj))
        IServiceFile = open(IServiceFilePath, "w")
        IServiceFile.write(IServiceContent)
        IServiceFile.close()
