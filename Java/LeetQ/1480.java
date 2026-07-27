class Solution {
    public int[] runningSum(int[] nums) {
        int[] sumnums= new int[nums.length];
        int prevsum=0;
        for(int i=0;i<nums.length;i++){
            sumnums[i]=nums[i]+prevsum;
            prevsum=sumnums[i];
        }

        return sumnums;
        
    }
}