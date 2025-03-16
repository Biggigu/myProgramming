using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Section3_Constrol_Flow
{
    class Exercise3
    {
        static public void ConsoleInput_Output3()
        {
            //for (int i = 0; i < 5; i++)
            //{
            //    Console.WriteLine(i);
            //}
            //Console.ReadLine();

            //for (int i = 0; i <= 10; i+=2)
            //{
            //    Console.WriteLine(i);
            //}
            //Console.ReadLine();

            Console.WriteLine("What word/s do you wanna repeat? ");
            string word2Rep = Console.ReadLine();

            Console.WriteLine($"How many times do you want to repeat '{word2Rep}' for? ");
            int loopCounter = Convert.ToInt32(Console.ReadLine());

            if (loopCounter <= 0)
            {
                Console.WriteLine("Sorry, please enter a value above 0");
            }
            else
            {
                for (int i = 0; i < loopCounter; i++)
                {
                    Console.WriteLine(word2Rep);
                } 
            }
            Console.ReadLine(); 
        }
    }
}
