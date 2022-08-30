class Solution:
    def ffill(self, old_color, new_color, i, j, image):
        # Check if i and j are in the image, and check that the pixel at this position has the old color
        if i < len(image) and i >= 0 and j < len(image[0]) and j >= 0 and image[i][j] == old_color:
        # Update this pixel to the new color and look for other pixels to color up, down, left, and right
            image[i][j] = new_color
            self.ffill(old_color, new_color, i, j+1, image)
            self.ffill(old_color, new_color, i+1, j, image)
            self.ffill(old_color, new_color, i-1, j, image)
            self.ffill(old_color, new_color, i, j-1, image)
        #Modify image inplace to save memory
        return image
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if image[sr][sc] == color:
            return image
        
        else:
            return self.ffill(image[sr][sc], color, sr, sc, image)
        