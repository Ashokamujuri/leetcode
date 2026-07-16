class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance = 0
        
        while mainTank >= 5:
            distance += 50      # Drive 50 km
            mainTank -= 5       # Burn 5 liters
            
            if additionalTank >= 1:
                additionalTank -= 1
                mainTank += 1   # Transfer 1 liter
                
        # Add the remaining fuel left in the main tank
        distance += mainTank * 10
        
        return distance