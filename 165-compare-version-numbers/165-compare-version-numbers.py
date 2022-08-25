class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_list = version1.split('.')
        version2_list = version2.split('.')
        
        version1_length = len(version1_list)
        version2_length = len(version2_list)
        
        max_length = max(version1_length, version2_length)
        
        for i in range(max_length):
            if i < version1_length and i < version2_length:
                version1_val = int(version1_list[i])
                version2_val = int(version2_list[i])
            
            elif i >= version1_length:
                version1_val = 0
                version2_val = int(version2_list[i])
            
            else:
                version1_val = int(version1_list[i])
                version2_val = 0
                            
            if version1_val < version2_val:
                return -1
            
            elif version1_val > version2_val:
                return 1
            
        return 0
