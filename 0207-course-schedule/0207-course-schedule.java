class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph=new ArrayList<>();

//graph creation
        for(int i=0;i<numCourses;i++)
        {
            graph.add(new ArrayList<>());
        }

int indegree[]= new int[numCourses];
//adding adjacnet nodes and adding indegree
for(int[] p: prerequisites)
{
    int course=p[0];
    int pre=p[1];

    graph.get(pre).add(course);
    indegree[course]++;
}

Queue<Integer> q=new LinkedList<>();
//take the node with indegree 0
for(int i=0;i<numCourses;i++)
{
    if(indegree[i]==0)
    {
     q.offer(i);
    }
}

//topological sort

int count=0;
while(!q.isEmpty())
{
    int check=q.poll();
    count++;

    for(int neigh:graph.get(check))
    {
        indegree[neigh]--;
        if(indegree[neigh]==0)
        {
            q.offer(neigh);
        }
    }

}

return count==numCourses;


    }
}