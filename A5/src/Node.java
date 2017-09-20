import java.util.ArrayList;

public class node 
{
	int time;
	int [] job = null;
	boolean [] jobArray = null;
	node(int tt, int[] ja, boolean[] jad)
	{
		job = new int[ja.length];
		jobArray = new boolean[jad.length];
		for (int i = 0; i < ja.length; i++)
		{
			jobArray[i] = jad[i];
			job[i] = ja[i];
		}
		time = tt;	
	}
	
	public int getTime()
	{
		return time;
	}
	
	public int [] getAssignedTo()
	{
		return job;
	}
	
	public boolean [] getjobArray()
	{
		return jobArray;
	}
}
