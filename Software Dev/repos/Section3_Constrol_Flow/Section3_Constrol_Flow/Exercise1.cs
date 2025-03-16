using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace Section3_Constrol_Flow
{
    class Exercise1
    {

        /*
            Output string to read in the current hour in 24-hour format
            Convert input and store into a int variable
            Output the time in the day using the following guidelines
            0 - 5       = Dawn
            6 - 11      = Morning
            12 - 17     = Afternoon
            18 - 23     = Evening
        */

        static public void ConsoleInput_Output1()
        {
            Console.WriteLine("What hour is it using 24-hr Format?: ");
            string hourInput = Console.ReadLine();
            int hourT = Convert.ToInt32(hourInput);

            if (hourT >= 0 && hourT <= 5)
            {
                Console.WriteLine("It is Dawn!");
            }
            else if (hourT >= 6 && hourT <= 11)
            {
                Console.WriteLine("It is Morning!");
            }
            else if (hourT >= 12 && hourT <= 17)
            {
                Console.WriteLine("It is Afternoon");
            }
            else if (hourT >= 18 && hourT <= 23)
            {
                Console.WriteLine("It is Evening!");
            }
            else
            {
                Console.WriteLine("invalid input"); 
            }
                Console.ReadLine();
        }
    }
}
