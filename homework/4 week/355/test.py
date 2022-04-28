import heapq
class Twitter:

    def __init__(self):
        self.user = {}
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        if userId not in self.user:
            self.user[userId] = {"follow":set(),"twitter":[]}
        box = [{"id":tweetId,"time":self.time}] + self.user[userId]["twitter"][:]
        self.user[userId]["twitter"] = box[:10]


    def getNewsFeed(self, userId: int) :
        if userId not in self.user:
            return []
        queue = []
        box = self.user[userId]["twitter"][:]
        for i in self.user[userId]["follow"]:
            if i in self.user:
                box += self.user[i]["twitter"][:]
        for i in box:
            heapq.heappush(queue,(-1 * i["time"],i["id"]))
        ans = []
        while queue:
            ans.append(heapq.heappop(queue)[1])
        return ans[:10]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user:
            self.user[followerId] = {"follow":set(),"twitter":[]}
        self.user[followerId]["follow"].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user:
            self.user[followerId] = {"follow":set(),"twitter":[]}
        if followeeId in self.user[followerId]["follow"]:
            self.user[followerId]["follow"].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)