using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Section3_Constrol_Flow
{
    class DoWhileLoops
    {
        static public void ConsoleInput_Output5() 
        {
            int i = 0;
            
            while (i < 10)
            {
               Console.WriteLine(i);
                i++;
            }

            int answer;  // Stores user input
            int actualAnswer;  // Stores correct answer

            Console.Write("Enter 1st number: ");
            int numberA = Convert.ToInt32(Console.ReadLine());

            Console.Write("Enter 2nd number: ");
            int numberB = Convert.ToInt32(Console.ReadLine());

            actualAnswer = numberA * numberB; // Compute the correct answer

            Console.Write($"What's the value of {numberA} x {numberB}? ");

            do
            {
                string answerInput = Console.ReadLine();
                answer = Convert.ToInt32(answerInput);

                if (answer == actualAnswer)
                {
                    Console.WriteLine("✅ Well Done! You got it right.");
                }
                else
                {
                    Console.WriteLine("❌ Your answer is incorrect! Try again.");
                }
            } while (answer != actualAnswer);  // Keep looping until the answer is correct

            Console.ReadLine();
        }
    }
}
