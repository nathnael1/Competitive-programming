class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        #going through the image in each entry and reverse each entity

        for items in image:
            items.reverse()
            for index in range(len(items)):
                items[index]^= 1
        return image