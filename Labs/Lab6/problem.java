import java.util.LinkedList;
import java.util.Queue;

public class CourseScheduler {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] inDegree = new int[numCourses];
        LinkedList<Integer>[] graph = new LinkedList[numCourses];
        for (int i = 0; i < numCourses; i++) {
            graph[i] = new LinkedList<>();
        }
        for (int[] pair : prerequisites) {
            inDegree[pair[0]]++;
            graph[pair[1]].add(pair[0]);
        }
        
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) {
                queue.add(i);
            }
        }
        
        int count = 0;
        while (!queue.isEmpty()) {
            int course = queue.poll();
            count++;
            for (int nextCourse : graph[course]) {
                inDegree[nextCourse]--;
                if (inDegree[nextCourse] == 0) {
                    queue.add(nextCourse);
                }
            }
        }
        
        return count == numCourses;
    }

    public static void main(String[] args) {
        CourseScheduler scheduler = new CourseScheduler();
        System.out.println(scheduler.canFinish(2, new int[][]{{1, 0}})); // true
        System.out.println(scheduler.canFinish(2, new int[][]{{1, 0}, {0, 1}})); // false
    }
}
