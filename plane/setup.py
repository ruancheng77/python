import sys
from cx_Freeze import setup,Executable

base = None
# 判断Windows系统
if sys.platform == 'win32':
    base = 'Win32GUI'


packages = []

for dbmodule in ['win32gui','win32api' ,'win32con' , 'cx_Freeze']:

    try:

        __import__(dbmodule)

    except ImportError:

        pass

    else:
        packages.append(dbmodule)


options = {
                'build_exe': 
                        {
                             'includes': 'atexit'
                             # 依赖的包
                             ,"packages": ["os"]
                             ,"includes":["pygame","time","sys"]
                             ,"include_files":["./img"]
                             # 额外添加的文件
                             #, 'include_files':['image_rc.py']
                            }
                
                }

executables = [
                        Executable(
                                        # 工程的 入口 
                                        'Dafeiji.py'
                                        , base=base
                                        # 生成 的文件 名字
                                        , targetName = 'Dafeiji.exe'
                                        # 生成的EXE的图标
                                       #, icon = "test_32.ico" #图标, 32*32px
                                        )
                    ]

setup(
            # 产品名称
           name='dafeiji',
            # 版本号
            version='1.0',
            # 产品说明
            description='My game-dafeiji',
            options=options,
            executables=executables
      )
