//---------------------------------------------------------------------------------------------------------------------

//CMPE 365 ASSIGNMENT 5
//NAMES: KAL RADIKOV 10157529 || HENLEY CHIU 10141943
//DATE: DEC 3RD 2016

//---------------------------------------------------------------------------------------------------------------------

import java.util.Scanner;
import java.util.stream.IntStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Compare;
import java.util.PriorityQueue;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.lang.reflect.Array;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Path;

//---------------------------------------------------- Main Function ---------------------------------------------------

public class MainClass 
{
	public static void main(String[] args)
	{
		int size = 0;
		int row = 0;
		int [][] jobs = null;
		
//------------------------------------------------------ Read File -----------------------------------------------------

		try 
		{
			BufferedReader in = new BufferedReader(new FileReader("src/data40.txt"));
			String line = in.readLine();
			size = Integer.parseInt(line);
			jobs = new int [size][size];
			
			while ((line = in.readLine()) != null)
			{
				String [] intValues = line.split("\t");
				for (int i = 0; i < size; i++)
				{
					jobs[row][i] = Integer.parseInt(intValues[i]);
				}
				row++;
			}
		}
		catch (Exception e)
		{
			e.printStackTrace();
		}
		
//------------------------------------------------ B&B Algorithm Set-Up ------------------------------------------------
		
		boolean[] a = new boolean [size];
		int [] aAssign = new int[size];
		int t = 0;

		for (int i = 0; i< size; i++)
		{
			int minT = 500;
			int minI = 0;
			for (int j = 0; j < size; j++)
			{
				if ((jobs[i][j] < minT) && (a[j] == false))
				{
					minT = jobs[i][j];
					minI = j;
				}
			}
			a[minI] = true;
			aAssign[minI] = i;
			t = t + minT;
		}
		
//---------------------------------------------------- B&B Algorithm ---------------------------------------------------

		Node upperBound = new Node(t, aAssign, a);
		System.out.println("Greedy Algorithm: " + t);
		
		Arrays.fill(a, false);
		Arrays.fill(aAssign, -1);
		
		boolean[] p = new boolean [size];
		int [] pAssign = new int[size];
		Arrays.fill(pAssign, -1);
		int permT = 0;
		t = 0;
		Compare<Node> compare = new Compare();
		PriorityQueue<Node> ts = new PriorityQueue<Node>(size, compare);
		
		for (int n = 0; n < size; n++)
		{
			for (int i = 0; i < size; i++)
			{
				if (p[i] == false)
				{
					System.arraycopy(pAssign, 0, aAssign, 0, pAssign.length);
					System.arraycopy(p, 0, a, 0, p.length);
					a[i] = true;
					aAssign[i] = n;
					t = permT + jobs[n][i]; 
					
					for (int k = 0; k < size; k++)
					{
						int minT = 500;
						int minI = 0;
						if (! inArr(aAssign, k))
						{
							for (int m = 0; m < size; m++)
							{
								if ((jobs[k][m] < minT) && (a[m] == false) && p[i] == false)
								{
									minT = jobs[k][m];
									minI = m;
								}
							}
							a[minI] = true;
							aAssign[minI] = k;
							t = t + minT;
						}
					}
					
//------------------------------------- Put partial solution in structure ---------------------------------------------

					Node partial = new Node(t, aAssign, a);
					ts.add(partial);
					Arrays.fill(a, false);
					Arrays.fill(aAssign, -1);
					t = 0;
				}
			}
			Node partialBest = ts.poll();
			int j = iArr(partialBest.getaTo(), n);
			p[j] = true;
			pAssign[j] = n;
			permT = permT + jobs[n][j];
			ts.clear();
		}
		
//-------------------------------------------------- Print Statements ------------------------------------------------

		System.out.println("Total time: " + permT);
		System.out.println("Job assignments:");
		for (int i = 0; i < size; i++)
		{
			System.out.println("Person " + i + " is assigned job " + iArr(pAssign, i));
		}
	}
	
//------------------------------------------------ Other Functions ---------------------------------------------------

	public static boolean inArr(int[] a, int b)
	{
		int i = 0;
		while( i < a.length)
		{
			if (a[i] == b)
			{
				return true;
			}
			i++;	
		}
		return false;
	}
	
	public static int iArr(int[] a, int b)
	{
		int i = 0;
		while( i < a.length)
		{
			if (a[i] == b)
			{
				return i;
			}
			i++;	
		}
		return -1;
	}
}
