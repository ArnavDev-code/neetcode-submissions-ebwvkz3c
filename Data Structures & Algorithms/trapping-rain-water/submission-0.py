class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
            
        # 1. Setup our pointers and our "High Score" trackers
        l = 0
        r = len(height) - 1
        
        max_left = height[l]
        max_right = height[r]
        
        total_water = 0
        
        # 2. Squeeze inward until the pointers meet
        while l < r:
            
            # 3. The Bottleneck check: Which side is limiting our water?
            if max_left < max_right:
                # The left side is the bottleneck. Move the left pointer!
                l += 1
                
                # Update our max_left high score if we found a taller wall
                if height[l] > max_left:
                    max_left = height[l]
                else:
                    # Otherwise, calculate how much water sits on this block
                    total_water += max_left - height[l]
                    
            else:
                # The right side is the bottleneck. Move the right pointer!
                r -= 1
                
                # Update our max_right high score
                if height[r] > max_right:
                    max_right = height[r]
                else:
                    # Calculate the water
                    total_water += max_right - height[r]
                    
        return total_water