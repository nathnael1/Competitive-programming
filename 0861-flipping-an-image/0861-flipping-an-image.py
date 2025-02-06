class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        #going through the image in each entry and reverse each entity

        for items in image:
            items.reverse()
            for index,entity in enumerate(items):
                if entity == 1:
                    items[index] = 0
                else:
                    items[index] = 1
        return image