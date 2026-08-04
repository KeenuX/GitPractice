class Solution {   

    private int binarysearch(int[] nums, int target){
        int low=0;
        int high=nums.length-1;
        while(low<=high){
            int middle=(high+low)/2;
            if(nums[middle]==target)
                return middle;

            else if(nums[middle]>target)
                high=middle-1;
            else
                low=middle+1;
         }
         return -1;
    }

    public int[] searchRange(int[] nums, int target) {
        int[] ans=new int[2];
        int index= binarysearch(nums, target);
        if(index==-1){
            ans[0]=-1;
            ans[1]=-1;
            return ans;
        }
        int low=index;
        int high=index;
        while(low>=0 && nums[low]==target)
            low--;
        while(high<nums.length && nums[high]==target)
            high++;

        ans[0]= low+1;
        ans[1]=high-1;
        return ans;
        
    }

}