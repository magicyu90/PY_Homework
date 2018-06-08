from numpy import *
from texttable import Texttable

class CF:
    def __init__(self, movies, ratings, k=5, n=10):
        self.movies = movies
        self.ratings = ratings
        # 邻居个数
        self.k = k
        # 推荐个数
        self.n = n
        # 用户对电影的评分
        # 数据格式{'UserID：用户ID':[(MovieID：电影ID,Rating：用户对电影的评星)]}
        self.userDict = {}
        # 对某电影评分的用户
        # 数据格式：{'MovieID：电影ID',[UserID：用户ID]}
        # {'1',[1,2,3..],...}
        self.ItemUser = {}
        # 邻居的信息
        self.neighbors = []
        # 推荐列表
        self.recommendList = []
        self.cost = 0.0

    def recommendByUser(self, userId):
        """根据用户的推荐 根据对电影的评分计算用户之间的相似度"""
        self.formatRate()
        self.n = len(self.userDict[userId])
        self.getNeighbor(userId)
        self.getRecommendList(userId)

    def getRecommendList(self, userId):
        """获取推荐列表"""
        self.recommendList = []
        # 建立推荐字典
        recommendDict = {}
        for neighbor in self.neighbors:  # 相似用户
            ms = self.userDict[neighbor[1]]
            for movie in ms:
                if movie[0] in recommendDict:
                    recommendDict[movie[0]] += neighbor[0]
                else:
                    recommendDict[movie[0]] = neighbor[0]
        # 建立推荐列表
        for k in recommendDict:
            self.recommendList.append([recommendDict[k], k])

        self.recommendList.sort(reverse=True)
        self.recommendList = self.recommendList[:self.n]

    def getNeighbor(self, userId):
        """获取某用户的相邻用户"""
        neighbors = []
        self.neighbors = []
        # 获取userId评分的电影都有哪些其他用户评分过
        for i in self.userDict[userId]:
            for j in self.ItemUser[i[0]]:
                if j != userId and j not in neighbors:
                    neighbors.append(j)
        for neighbor in neighbors:
            dist = self.getCost(userId, neighbor)
            self.neighbors.append([dist, neighbor])

        self.neighbors.sort(reverse=True)
        self.neighbors = self.neighbors[:self.k]

    def formatuserDict(self, userId, l):
        user = {}
        for i in self.userDict[userId]:
            user[i[0]] = [i[1], 0]
        for j in self.userDict[l]:
            if j[0] not in user:  # 如果userId没有看过其他用户看过的电影
                user[j[0]] = [0, j[1]]
            else:  # 如果看过
                user[j[0]][1] = j[1]
        return user

    def getCost(self, useId, l):
        """当前用户和某一用户相似度比较"""
        user = self.formatuserDict(useId, l)
        x = 0.0
        y = 0.0
        z = 0.0
        for k, v in user.items():
            x += float(v[0]) * float(v[0])
            y += float(v[1]) * float(v[1])
            z += float(v[0]) * float(v[1])
        if(z == 0.0):
            return 0
        return z / sqrt(x * y)

    def formatRate(self):
        """将ratings转换为userDict和ItemUser"""
        self.userDict = {}
        self.ItemUser = {}
        for i in self.ratings:
            userId = i[0]
            movieId = i[1]
            temp = (movieId, float(i[2]) / 5)
            # 计算userDict {'用户ID':[('电影ID',评分),('电影ID',评分)]}
            if userId in self.userDict:
                self.userDict[userId].append(temp)
            else:
                self.userDict[userId] = [temp]
            # 计算ItemUser {'电影ID':['用户1','用户2','用户3'...]}
            if movieId in self.ItemUser:
                self.ItemUser[movieId].append(userId)
            else:
                self.ItemUser[movieId] = [userId]

    def showTable(self):
        neighbors_id = [i[1] for i in self.neighbors]
        table = Texttable()
        table.set_deco(Texttable.HEADER)
        table.set_cols_dtype(["t", "t", "t", "t"])
        table.set_cols_align(["l", "l", "l", "l"])
        rows = []
        rows.append([u"movie ID", u"Name", u"release", u"from userID"])
        for item in self.recommendList:
            fromID = []
            for i in self.movies:
                if i[0] == item[1]:
                    movie = i
                    break
            for i in self.ItemUser[item[1]]:
                if i in neighbors_id:
                    fromID.append(i)
            movie.append(fromID)
            rows.append(movie)
        table.add_rows(rows)
        print(table.draw())


def readFile(filename):
    #files = open(filename, 'r', encoding='utf-8')
    files = open(filename, "r", encoding="iso-8859-15")
    data = []
    for line in files:
        data.append(line.strip().split('::'))
    return data


if __name__ == "__main__":
    print('开始进行协同过滤...')
    movies = readFile('analyse/ml-1m/movies.dat')
    ratings = readFile('analyse/ml-1m/ratings.dat')
    cf = CF(movies, ratings, k=20)
    cf.recommendByUser("100")
    cf.neighbors
    cf.showTable()
