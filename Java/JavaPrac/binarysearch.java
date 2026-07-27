import java.util.Arrays;

public class binarysearch {
    public static void main(String[] args) {
        int[] array = { 14, 3, 29, 8, 35, 1, 22, 17, 10, 31, 6, 25, 13, 36, 4, 19, 28, 11, 33, 2, 24, 9, 15, 30, 5, 21,
                18, 34, 7, 27, 12, 26, 32, 16, 20, 23 };
        int[] sorted = array.clone();
        int target = 3;
        int first = 0;
        int index = -1;
        int last = sorted.length - 1;
        boolean isfound = false;
        Arrays.sort(sorted);
        while (first <= last) {
            int middle = first + (last - first) / 2;
            if (sorted[middle] == target) {
                isfound = true;

                break;
            } else if (sorted[middle] > target)
                last = middle - 1;
            else
                first = middle + 1;
        }

        for (int i = 0; i < array.length; i++) {
            if (target == array[i]) {
                index = i;
                break;
            }
        }

        if (isfound)
            System.out.println("Element found at index " + index);
        else
            System.out.println("Element not found");

    }
}
