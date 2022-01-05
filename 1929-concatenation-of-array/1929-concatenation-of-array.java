class Solution {
    public int[] getConcatenation(int[] nums) {      
        int length = nums.length;
        int[] ans = new int[2*length];
        // ans = nums;
            
        for(int i=0, j = 0; i < 2*length; i++, j++){
            if(j == length)
                j = 0;
            
            ans[i] = nums[j];
        }
         
        return ans;
    }
}