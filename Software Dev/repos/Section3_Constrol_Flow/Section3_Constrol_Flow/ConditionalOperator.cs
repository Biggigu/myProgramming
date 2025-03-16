using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Section3_Constrol_Flow
{
    class ConditionalOperator
    {
        public static void ConditionalOperator1() 
        {
            int age = -10;

            if (age >= 0)
            {
                Console.WriteLine("Valid");
            }
            else
            {
                Console.WriteLine("Invalid");
            }

            //Condition ? true : false
            //Conditional Operatot/ Question Mark / Ternary Operator 
            string result = age >= 0 ? "Valid" : "Invalid";
            
            Console.ReadLine();

            //lets try a task
            /*
             * Create and initialise two int variables
             * If statement to compare first and second numbers
             * Print the bigger number to the screen
             * Extra: Convert if to use a conditional operator
             */

            Console.WriteLine("Give me 1st Number: ");
            string firstNumInput = Console.ReadLine();
            int firstNum = Convert.ToInt32(firstNumInput);

            Console.WriteLine("Give me 2nd Number: ");
            string sencondNumInput = Console.ReadLine();
            int secondNum = Convert.ToInt32(sencondNumInput);

            if (firstNum == secondNum)
            {
                Console.WriteLine("Both numbers are Equal.");
            }
            else if (secondNum < firstNum)
            {
                Console.WriteLine($"{secondNum} is smaller than {firstNum}");
            }
            else if (firstNum < secondNum)
            {
                Console.WriteLine($"{firstNum} is smaller than {secondNum}");
            }
                Console.ReadLine();

            int biggest = firstNum > secondNum ? firstNum : secondNum;
            int smallest = secondNum < firstNum ? secondNum : firstNum;

            Console.WriteLine($"{biggest} is bigger than {smallest}");
        }
    }
}