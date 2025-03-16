using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Section3_Constrol_Flow
{
    class FormatCurrency
    {
        public static void MoneyRegionTasks() 
        {
            /*
             * Ask user to input the money they wish they had
             * Convert and store as a variable (choose data type wisely)
             * Print value using formatted outputs, example: £12.34
             * If statement to check if the inputted balance is greater than 0
               * Greater than 0 print "Great goals!"
               * Else print "Interesting choice..."
             * Extra: convert if to use a conditional operator
             */


            Console.WriteLine("Enter the money you wish you had: ");
            double money = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine($"The money you wish to have is {money}. ");
            Console.WriteLine(money.ToString("C"));

            if (money > 0)
            {
                Console.WriteLine("Great goals!");
            }
            else
            {
                Console.WriteLine("interesting choice...!");
            }


            Console.WriteLine(money > 0 ? "Great Goals!" : "Interesting choice");
            
            Console.ReadLine();

        }
    }
}
