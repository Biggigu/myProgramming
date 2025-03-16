using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.NetworkInformation;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace Session2_Exercise_1_Storing_user_Data
{
    class Program
    {
        static void Main(string[] args)
        {
            //Task 1
            //Define a variable to hold your name
            //Define a variable to hold your phone number
            //Define a variable to hold your age
            //Print variables line - by - line to the screen
            //Extra: define variables usin the var keyword

            string name = "Sam";
            string number = "1234567890";
            int age = 22;

            Console.WriteLine(name);
            Console.WriteLine(number);
            Console.WriteLine(age);


            //Task 2
                /*
                Make & initalise 3 int variables
                Create a variable to hold the sum of the 3 int's
                Create a variable to hold the average of the 3 int's
                Print total and average to the screen on individual lines                         
                */

            int num1 = 1;
            int num2 = 2;
            int num3 = 3;

            int total = num1 + num2 +num3;

            int average = total / 3;
            Console.WriteLine(average);
            Console.ReadLine();

            //Task 3

            /*
                Create two strings with any values
                Output them both to the screen
             */

            string value1 = "This is the 1st string";
            string value2 = "This is the 2ns string";
            Console.WriteLine(value1);
            Console.WriteLine(value2);
            Console.ReadLine();

            //Task 4
            /*
                Create & initalise two ints
                Make a variable to work out the remainder
                Output remainder to the screen
                Change the first int variable to another number
                    * and recalculate the remainder
                    * output new remainder to the screen
            */

            int thisNum1 = 5;
            int thisNum2 = 2;
            int thisNum3 = 3;

            int remainder = thisNum1 % thisNum2;
            Console.WriteLine(remainder);
            int remainder2 = thisNum2 % thisNum3;
            Console.WriteLine(remainder2);
            Console.ReadLine();
        }
    }
}
