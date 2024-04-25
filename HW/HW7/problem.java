package HW.HW7;
import java.util.Arrays;
import java.util.PriorityQueue;



public class problem {
   
    public int minMeetingRooms(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return 0;
        }
        
        
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        
        
        PriorityQueue<Integer> allocator = new PriorityQueue<Integer>(
            intervals.length, (a, b) -> a - b);
        

        allocator.add(intervals[0][1]);
        
        
        for (int i = 1; i < intervals.length; i++) {
            
            if (intervals[i][0] >= allocator.peek()) {
                allocator.poll();
            }
           
            allocator.add(intervals[i][1]);
        }
        
       
        return allocator.size();
    }
}

}
