#python makefile.py 20000

import os
from xml.dom.minidom import parse
import xml.dom.minidom
import sys


dict = {
    'sjes-gateway-app': '20000',
    'others': '9102',
    'others2': '3258'
}





def getPidByPort( port ):

    ret = os.popen(" netstat -lnp | grep "+port)
    resultStr = ret.read()
    # resultStr = "tcp6       0      0 :::" + port + "                :::*                    LISTEN      111/java ";
    print resultStr
    split1 = resultStr.split(' ')
    for str in split1:
        if  str.__contains__('/java'):

            pid = str.split('/')[0]
            return pid;
    return "";

def getBranch(  ):

    ret = os.popen("git branch")
    resultStr = ret.read()

    split1 = resultStr.split('\n')
    for str in split1:
        if  str.__contains__('*'):

            str = str.strip()
            return str[2:str.__len__()]
    return "";

def getPidByPort( port ):

    ret = os.popen(" netstat -lnp | grep "+port)
    resultStr = ret.read()
    # resultStr = "tcp6       0      0 :::" + port + "                :::*                    LISTEN      111/java ";
    print resultStr
    split1 = resultStr.split(' ')
    for str in split1:
        if  str.__contains__('/java'):

            pid = str.split('/')[0]
            return pid;
    return "";






def getPortByServiceName( serviceName ):
    return dict[serviceName];

def main( ):


    # serviceName ="" ;
    # port = "";
    # branch = "";
    # if len(sys.argv) == 1 :
    #     print "[error] ---- serviceName not empty "
    #     return
    #
    # isAType = False;
    # if len(sys.argv) == 2 :
    #     arg = str(sys.argv[1])
    #     if arg.__contains__(":"):
    #         sps = arg.split(":")
    #         serviceName=sps[0];
    #         port = sps[1];
    #         print "[start] ----  arg1 serviceName = "+serviceName
    #         print "[start] ----  arg1 port = "+port
    #
    #         isAType = True
    #     else:
    #         isAType = False;
    #
    # if isAType != True:
    #     if len(sys.argv) >= 2 :
    #
    #         serviceName = str(sys.argv[1])
    #         if serviceName.__contains__("/"):
    #             serviceName= serviceName[0:serviceName.__len__()-1]
    #         print "[start] ----  arg1 serviceName = "+serviceName
    #
    #     if len(sys.argv) >= 3 :
    #
    #         port = str(sys.argv[2])
    #         print "[start] ----  arg2 port = "+port
    #
    #     if len(sys.argv) == 4 :
    #
    #         branch = str(sys.argv[3])
    #         print "[start] ----  arg3 branch = "+branch




    port="";
    branch="";
    if len(sys.argv) == 2 :
        branch = str(sys.argv[1])
    # if len(sys.argv) >= 3 :
    #     branch = str(sys.argv[2])
    print port
    print branch


    DOMTree = xml.dom.minidom.parse("pom.xml")
    project = DOMTree.documentElement
    artifactIdNote = project.getElementsByTagName("artifactId")[0]
    versionNote = project.getElementsByTagName("version")[0]
    packagingNote = project.getElementsByTagName("packaging")[0]

    artifactId = artifactIdNote.childNodes[0].data
    version = versionNote.childNodes[0].data
    packaging = packagingNote.childNodes[0].data

    service = artifactId+"-"+version+"."+packaging;
    if port == "":
        port = getPortByServiceName(artifactId)


    print "[port] ---- assign port = " + port
    if branch != "" :
        print "[branch] ---- assign branch = " + branch


    pid = str(getPidByPort(port))

    print "[pid] ----  pid = " + pid

    print "[service] ----  service = "+service
    if service=="" :
        print "[error] ---- serviceName not empty "
        return

    if branch != "":
        print "[branch] ----  set branch = " + branch
        print "git -c core.quotepath=false checkout "+ branch +" --"
        os.system("git checkout "+ branch )
        os.system("git -c core.quotepath=false checkout "+ branch +" --")

    else:
        branch = getBranch()

    print "[branch] ----  git pull "+branch

    os.system("git pull")


    print "[build] ----"+" ./mvnw clean install -Dmaven.test.skip=true"

    os.system("./mvnw clean install -Dmaven.test.skip=true")


    if pid != "":
        print "[pid] ----"+" kill -9 "+pid
        os.system("kill -9 "+pid)

    print "[build] ----"+" sudo service "+service+" restart"

    os.system("sudo service "+service+" restart")


    return










if __name__ == '__main__':
    main()
