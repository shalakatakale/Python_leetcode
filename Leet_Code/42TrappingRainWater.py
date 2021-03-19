
# def trap(self, [0, 1, 0, 2, 1, 0, 1, 3, 2, 1]):
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1]
waterLevel = []
left = 0
for h in height:
    left = max(left, h)
    waterLevel += [left] # over-fill it to left max height
    right = 0
for i, h in reversed(list(enumerate(height))):
        right = max(right, h)
        print(i)
        waterLevel[i] = min(waterLevel[i], right) - h # drain to the right height
    # return sum(waterLevel)
# return print(waterLevel)
print(waterLevel)


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        waterlevel = []
        left = 0
        for h in height:
            left = max(left, height)
            waterlevel += [left]

        right = 0
        for i, h in reversed(list(enumerate(height))):
            right = max(right, h)
            waterlevel[i] = min(waterlevel[i], right) - h
        return sum(waterlevel)