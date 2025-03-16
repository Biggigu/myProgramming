using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Section3_Constrol_Flow
{
    class ConsoleIO
    {
        static public void ConsoleInput_Output()
        {
            string myName = "Biggigu";
            Console.WriteLine($"Hello my name is {myName}");

            Console.Write("Enter your name: ");

            string name = Console.ReadLine();

            Console.WriteLine($"Hello {name}");

            Console.Write("Enter your Age: ");
            string ageInput = Console.ReadLine();
            int age = Convert.ToInt32(ageInput);

            //while (!int.TryParse(Console.ReadLine(), out age))
            //{
            //    Console.WriteLine("invalid input! Enter a valid age: ");
            //}

            //Console.WriteLine($"So {name} you are {age} years old! Is that Correct? (Y/N)");

            //string isCorrect = Console.ReadLine().ToUpper();
            ////loop untill user enters Y
            //while (isCorrect != "Y")
            //{
            //    Console.Write("Enter your Age again: ");
            //    while (!int.TryParse(Console.ReadLine(), out age))
            //    {
            //        Console.WriteLine("invalid input! Enter a valid age: ");
            //    }
            //    Console.WriteLine($"So {name} you are {age} years old! Is that Correct? (Y/N)");
            //    isCorrect = Console.ReadLine().ToUpper();
            //}

            if (age == 18)
            {
                Console.WriteLine("You are 18");
            }

            if (age > 18 && age <= 24)

            {
                Console.WriteLine("You are older than 18 and youmger than 25");
            }
            else if (age >= 25)
            {
                Console.WriteLine("you are 25 or older");
            }
            if (age < 0 || age > 120)
            {
                Console.WriteLine("invalid age!");
            }

            Console.Write(($"{name} from from where do you come from?: "));
            string place = Console.ReadLine();

            Console.WriteLine($"{place}, Interesting place!");

            Console.ReadLine();

            Console.Write("Enter 1st number: ");
            string numberAInput = Console.ReadLine();
            int numberA = Convert.ToInt32(numberAInput);

            Console.Write("Enter 2nd number: ");
            string numberBInput = Console.ReadLine();
            int numberB = Convert.ToInt32(numberBInput);

            Console.Write($"Value of {numberA} x {numberB}: ");
            string answerInput = Console.ReadLine();
            int actualAnswer = Convert.ToInt32(answerInput);

            int answer = numberA * numberB;

            if (answer == actualAnswer)
            {
                Console.WriteLine("Well Done!");
            }
            else if (answer != actualAnswer)
            {
                Console.WriteLine("Your Answer is incorrect!");
            }

            Console.ReadLine();
        }
        
    }
}