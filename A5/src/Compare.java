import java.util.Comparator;

public class MyComparator implements Comparator<node>
{
	public int compare (node a, node b)
	{
		return  a.getTime() - b.getTime();
	}
}
