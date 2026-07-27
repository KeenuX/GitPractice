public class linearsearch {
    public static void main(String[] args) {
        int[] array={1,4,7,2,9,1};
        int target=4;
        boolean isfound=false;
        for(int i=0;i<array.length;i++){
            if(array[i]==target){
            isfound=true;
            System.out.println("Element found at index "+i);
            break;
            }
        }
        if(!isfound) System.out.println("Element not found");
    
    }
}
