#coding=utf-8
import subprocess

jps = subprocess.Popen(['jps'],stdout=subprocess.PIPE)
jps.wait()
java_pids = jps.communicate()
for data in java_pids:
    if data is not None:
        javaPidData = data.decode('utf-8')
        if javaPidData.find('org.eclipse')!=-1:
            l = javaPidData.split(' ')
            pid = l[0]
            print(pid)
            break


monitor = subprocess.Popen(['jstat','-gc',pid,'1s','3'],stdout=subprocess.PIPE)
monitor.wait()
with open('d:\monitorData.txt','w') as f:
    monitorData = monitor.communicate()
    [f.write(item) for item in map(lambda d:d.decode('utf-8'),[data for data in monitorData if data is not None])]


'''
判断是否需要GC优化，如果满足以下指标，一般不需要优化：
Minor GC执行时间不到50ms；
Minor GC执行不频繁，约10秒一次；
Full  GC执行时间不到1s；
Full  GC执行频率不算频繁，不低于10分钟1次；

GC的目的：
将转移到老年代的对象数量降低到最小；
减少full GC的执行时间；

参数说明:
S0C：年轻代中第一个survivor（幸存区）的容量 (字节) 
S1C：年轻代中第二个survivor（幸存区）的容量 (字节) 
S0U：年轻代中第一个survivor（幸存区）目前已使用空间 (字节) 
S1U：年轻代中第二个survivor（幸存区）目前已使用空间 (字节) 
EC：年轻代中Eden（伊甸园）的容量 (字节) 
EU：年轻代中Eden（伊甸园）目前已使用空间 (字节) 
OC：Old代的容量 (字节) 
OU：Old代目前已使用空间 (字节) 
PC：Perm(持久代)的容量 (字节) 
PU：Perm(持久代)目前已使用空间 (字节) 
YGC：从应用程序启动到采样时年轻代中gc次数 
YGCT：从应用程序启动到采样时年轻代中gc所用时间(s) 
FGC：从应用程序启动到采样时old代(全gc)gc次数 
FGCT：从应用程序启动到采样时old代(全gc)gc所用时间(s) 
GCT：从应用程序启动到采样时gc用的总时间(s) 
NGCMN：年轻代(young)中初始化(最小)的大小 (字节) 
NGCMX：年轻代(young)的最大容量 (字节) 
NGC：年轻代(young)中当前的容量 (字节) 
OGCMN：old代中初始化(最小)的大小 (字节) 
OGCMX：old代的最大容量 (字节) 
OGC：old代当前新生成的容量 (字节) 
PGCMN：perm代中初始化(最小)的大小 (字节) 
PGCMX：perm代的最大容量 (字节)   
PGC：perm代当前新生成的容量 (字节) 
S0：年轻代中第一个survivor（幸存区）已使用的占当前容量百分比 
S1：年轻代中第二个survivor（幸存区）已使用的占当前容量百分比 
E：年轻代中Eden（伊甸园）已使用的占当前容量百分比 
O：old代已使用的占当前容量百分比 
P：perm代已使用的占当前容量百分比 
S0CMX：年轻代中第一个survivor（幸存区）的最大容量 (字节) 
S1CMX ：年轻代中第二个survivor（幸存区）的最大容量 (字节) 
ECMX：年轻代中Eden（伊甸园）的最大容量 (字节) 
DSS：当前需要survivor（幸存区）的容量 (字节)（Eden区已满） 
TT： 持有次数限制 
MTT ： 最大持有次数限制
'''
