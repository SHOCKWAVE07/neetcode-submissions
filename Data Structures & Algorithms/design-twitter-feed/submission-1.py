class Twitter:

    def __init__(self):
        self.data = defaultdict(list)     
        self.followMap = defaultdict(set)
        self.post = 0  
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.data[userId].append([self.post, tweetId])
        self.post -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        if userId in self.data:
            feed.extend(self.data[userId])
            
        for i in self.followMap[userId]:
            if i in self.data:
                feed.extend(self.data[i])
        
        top = heapq.nsmallest(10,feed)

        return [tweetid for _,tweetid in top]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        

