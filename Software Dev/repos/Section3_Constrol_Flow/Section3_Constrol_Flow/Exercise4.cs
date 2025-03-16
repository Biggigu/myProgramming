using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Section3_Constrol_Flow
{
    class Exercise4
    {
        public static void ConsoleInput_Output4() 
        {
            /*
                Create int variable for the total
                Write for loop that loops 10 times from 1 till 10
                Add up the for loop counter
                This will give us the summation of 1-10
                Output total to the console after the for loop
            */
            Console.Write("Write a number: ");
            string dVariableInput = Console.ReadLine();
            int dVariable = Convert.ToInt32(dVariableInput);

            int total = 0;

            if (dVariable <= 0)
            {
                Console.WriteLine("Please write a number higher than 0");
            }
            else
            {
                for (int i = 1; i <= 10; i++)
                {
                    total += dVariable + i;
                }
                Console.WriteLine($"The sum of {dVariable} from 1 to 10 is {total}.");
            }
        }
    }
}
