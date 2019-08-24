'''
Your Verkada security camera has captured a funny video of a hummingbird. You'd like to post the clip on your social media account, but there were some people visible in the background. Since the image on a Verkada camera is so sharp and crisp, their faces are clearly identifiable, which you think might be an invasion of privacy. So you've decided to blur their faces before posting the clip
You are given an image, represented as a matrix of integers, where each integer corresponds to a color. The number in the ith (0-based) row and jth (0-based) column represents the color of the pixel in the ith row and jth column of the image.
Your task is to blur the image. In order to do that, you need to replace each number of the matrix with the average of the numbers in the neighboring cells. We assume that two cells are neighbors if they share at least one corner. The cell itself is not considered part of the average; only the 8 surrounding neighbors (or fewer if the cell is against an edge).
*Example:
For img = [[1, 4], [7, 10]], the output should be blurFaces(img) = [[7, 6], [5, 4]].
newImg[0][0] = (4 + 7 + 10) / 3 = 21 / 3 = 7
newImg[0][1] = (1 + 7 + 10) / 3 = 18 / 3 = 6
newImg[1][0] = (1 + 4 + 10) / 3 = 15 / 3 = 5
newImg[1][1] = (1 + 4 + 7) / 3 = 12 / 3 = 4
For img = [[3, 0, 2, 5], [1, 2, 3, 4], [2, 3, 2, 3]], the output should be blurFaces(img) = [[1, 2.2, 2.8, 3], [2, 2, 2.625, 3], [2, 2, 3, 3]].
newImg[0][0] = (0 + 1 + 2) / 3 = 3 / 3 = 1
newImg[0][1] = (1 + 2 + 2 + 3 + 3) / 3 = 11 / 5 = 2.2
newImg[0][2] = (0 + 2 + 3 + 4 + 5) / 3 = 14 / 5 = 2.8
newImg[0][3] = (2 + 3 + 4) / 3 = 9 / 3 = 3
newImg[1][0] = (0 + 2 + 2 + 3 + 3) / 3 = 10 / 5 = 2
newImg[1][1] = (0 + 1 + 2 + 2 + 2 + 3 + 3 + 3) / 3 = 16 / 8 = 2
newImg[1][2] = (0 + 2 + 2 + 2 + 3 + 3 + 4 + 5) / 3 = 21 / 8 = 2.625
newImg[1][3] = (2 + 2 + 3 + 3 + 5) / 3 = 15 / 5 = 3
newImg[2][0] = (1 + 2 + 3) / 3 = 6 / 3 = 2
newImg[2][1] = (1 + 2 + 2 + 2 + 3) / 3 = 10 / 5 = 2
newImg[2][2] = (2 + 3 + 3 + 3 + 4) / 3 = 15 / 5 = 3
newImg[2][3] = (2 + 3 + 4) / 3 = 9 / 3 = 3
'''
def blurFaces(img):

    x=[[0 for i in range(len(img[0]))] for j in range(len(img))]
    l=len(img)
    l1=len(img[0])
    for i in range(l):
        for j in range(l1):
            c=0
            e=-1
            for k in range(-1,2):
                for t in range(-1,2):
                    if 0<=k+i<l and 0<=t+j<l1:
                        c+=img[k+i][t+j]
                        e+=1
            x[i][j]=(c-img[i][j])/e
    return x
