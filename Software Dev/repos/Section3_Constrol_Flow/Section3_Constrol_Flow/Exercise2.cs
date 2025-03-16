using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace Section3_Constrol_Flow
{
    class Exercise2
    {
        static public void ConsoleInput_Output2()
        {
            Console.WriteLine("Enter a day of the Week from 1 - 7: ");
            int day = Convert.ToInt32(Console.ReadLine());
            Console.ReadLine();

            //if (day == 1)
            //{
            //    Console.WriteLine("Monday");
            //}
            //else if (day == 2)
            //{
            //    Console.WriteLine("Tuesday");
            //}
            //else if (day == 3)
            //{
            //    Console.WriteLine("Wednesday");
            //}
            //else if (day == 4)
            //{
            //    Console.WriteLine("Thursday");
            //}
            //else if (day == 5)
            //{
            //    Console.WriteLine("Friday");
            //}
            //else if (day == 6)
            //{
            //    Console.WriteLine("Saturday");
            //}
            //else if (day == 5)
            //{
            //    Console.WriteLine("Sunday");
            //}
            //Console.WriteLine(day);

            switch (day)
            {
                case 1:
                    Console.WriteLine("Mon");
                    break;
                case 2:
                    Console.WriteLine("Tue");
                    break;
                case 3:
                    Console.WriteLine("Wed");
                    break;
                case 4:
                    Console.WriteLine("Thur");
                    break;
                case 5:
                    Console.WriteLine("Fri");
                    break;
                case 6:
                    Console.WriteLine("Sat");
                    break;
                case 7:
                    Console.WriteLine("Sun");
                    break;
                default:
                    Console.WriteLine("Invalid option, enter a vailue between 1 and 7");
                    break;
            }

            Console.ReadLine();

            //Task 2

            /* Create a char variuable with calue from A - D
             * Switch statement on that char variable
             * In each case, print the following:
             * A        = Excellent
             * B        = Very Good
             * C        = Good
             * D        = Pass
             * Default  = Unknown Grade.
             */

            Console.WriteLine("Enter your result letter from A to D: ");
            string grade = Console.ReadLine().ToUpper();

            switch (grade)
            {
                case "A":
                    Console.WriteLine("Excellent");
                    break;
                case "B":
                    Console.WriteLine("Very Good");
                    break;
                case "C":
                    Console.WriteLine("Good");
                    break;
                case "D":
                    Console.WriteLine("Pass");
                    break;
                default : Console.WriteLine("Unknown Grade");
                    break;
            }
        }
    }
}
