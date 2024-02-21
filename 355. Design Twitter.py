'''
https://github.com/baseballcoder1/LeetCode

LeetCode 355: Design Twitter

Difficulty: Medium
'''

class Twitter:

    def __init__(self):
        self.follows = {}
        self.tweets = {}
        self.tweetnum = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.follows:
            self.follows[userId] = {userId: 1}
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId] += [(self.tweetnum, tweetId)]
        self.tweetnum += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.follows:
            return []
        follows = list(self.follows[userId].keys())
        tweetlists = [self.tweets[user] for user in follows]
        result = []
        i = [len(l) for l in tweetlists]
        for j in range(10):
            maxtweetnum = -1
            maxtweetId = -1
            maxk = -1
            for k in range(len(tweetlists)):
                if i[k] == 0:
                    continue
                else:
                    tweetnum, tweetId = tweetlists[k][i[k]-1]
                    if tweetnum > maxtweetnum:
                        maxk = k
                        maxtweetnum = tweetnum
                        maxtweetId = tweetId
            if maxtweetnum == -1:
                break
            i[maxk] -= 1
            result.append(maxtweetId)
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        for userId in followerId, followeeId:
            if userId not in self.follows:
                self.follows[userId] = {userId: 1}
            if userId not in self.tweets:
                self.tweets[userId] = []
        self.follows[followerId][followeeId] = 1

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            return
        if followeeId not in self.follows[followerId]:
            return
        del self.follows[followerId][followeeId]

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)