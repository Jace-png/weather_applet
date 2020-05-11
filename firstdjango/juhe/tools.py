import time,statistics
from juhe import test2
from timeit import Timer
class TimeTestTool:
    #计算函数运行时间
    @classmethod
    def calc_fucn_time(cls,func):
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        return end - start

    #统计时间
    @classmethod
    def statistic_run_time(cls,func,n):
        data = [cls.calc_fucn_time(func)for i in range(n)]
        mean =statistics.mean(data)
        sd = statistics.stdev(data,xbar=mean)
        return [data,mean,sd,max(data),min(data)]
    #对比
    @classmethod
    def compare(cls,fun1,fun2,n):
        result1 = cls.statistic_run_time(fun1,n)
        result2 = cls.statistic_run_time(fun2,n)
        print('对比\t 没有预加载 \t 预加载')
        print('平均值\t', result1[1], '\t', result2[1])
#重启电脑试试
if __name__ == '__main__':
    # DataTool.generate_fake_user_data(10000)
    TimeTestTool.compare(test2.lazy_load, test2.pre_load, 1000)

