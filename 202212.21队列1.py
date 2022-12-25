class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:  # 直接排序
            return "".join(sorted(s))
        result = s
        for i in range(1, len(s)):  # 依次比较
            s = s[1:] + s[0]  # 每次循环后s都会变化,因此这里与i无关
            result = min(result, s)
        return result

ss=Solution()
s='acbed'
k=2
print("最小队列为：",ss.orderlyQueue(s,k))

 #最小排序分两种情况，一个是k>1时，队列相当于可以任意排序，直接选用sorted函数进行排序即可
 #而另一种情况k=1时，相当于对于一个长度为n的队列，有且只有n种排列方法，则可以将队列看作一个循环队列，可随意指定一个元素作为起点，去最小队列即可。