# spring-boot-AutoRunScript


将一系列springboot 编译启动的命令写进python脚本:
git pull
./mvnw clean install -Dmaven.test.skip=true
kill -9 {{pid}}
sudo service xxx-1.0.0-RELEASE.jar restart

使用方式：将文件拷贝到spring boot 工程下，cd 到当前工程目录，
输入命令 python makefile.py {{port，非必输}}，
     1. 根据当前branch更新代码
     2. 查找port的端口号占用的进程pid
     3. clean chche，compile code，kill pid ，restart service
或者在makefile.py 配置如下，就不要输入port。
    dict = {
     'xxx': '20000'
    }
测试：运行稳定。
后续：
    1. 如果有10个spring boot 服务，每个spring boot 工程下都放置一个makefile.py,可以批量一键部署系统。
    2. 增加自动输入密码模块，用expect模块自动输入密码，不需要手输，一键启动。但需要每台服务器安装Pexpect模块。

附： 因为现在linux大多数内置python 2.0+，部署不需要安装额外软件，所以python的版本也是2.0+。