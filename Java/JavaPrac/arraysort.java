public class arraysort {
    public static void main(String[] args) {
        int[] array={0,0,0,0,0,0,11,22,0,44,0,55,0,0,66};
        int i=0;
        int index=0;
        while(i<array.length){
            if(array[i]!=0){
                array[index]=array[i];
                index++;
            }
            i++;
        }
        while(index<array.length){
            array[index]=0;
            index++;
        }
        for (int num : array) {
        System.out.print(num + " ");
        }
    }
    
}
