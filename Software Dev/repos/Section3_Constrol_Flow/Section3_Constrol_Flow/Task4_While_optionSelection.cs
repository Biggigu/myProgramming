using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace Section3_Constrol_Flow
{
    class Task4_While_optionSelection
    {
        public static void Task4()
        {
            /*
             * * Print 3 options:
                * 1. Buy
                * 2. Sell
                * 3. Swap

            * Output a message to choose a value (1-3)
            * Convert the string input and store in an int variable
            * Write while loop to check the menu selection
                * While loop condition should be a range check
                * If it's outside the range you should ask the user again
            * If statement to output what menu option they selected
                * 1 = Buy
                * 2 = Sell
                * 3 = Swap
            */

            Console.WriteLine("Choose a menu option by inputting 1, 2 or 3: ");
            string UserInputString = Console.ReadLine();
            int UserInput = Convert.ToInt32(UserInputString);

            Console.WriteLine("1. Buy");
            Console.WriteLine("2. Sell");
            Console.WriteLine("3. Swap");


            do
            {
                Console.WriteLine("Invalid Option! choose between 1 & 3; ");
                Console.WriteLine("Choose a menu option by inputting 1, 2 or 3: ");
                UserInput = Convert.ToInt32(Console.ReadLine());
            }
            while (UserInput < 1 || UserInput > 3);

                switch (UserInput)
                {
                    case 1:
                        Console.WriteLine($"You have chosen {UserInput}.");
                        Console.WriteLine("You have chosen the 'Buy' option.");
                        break;
                    case 2:
                        Console.WriteLine($"You have chosen {UserInput}.");
                        Console.WriteLine("You have chosen the 'Sell' option.");
                        break;
                    case 3:
                        Console.WriteLine($"You have chosen {UserInput}.");
                        Console.WriteLine("You have chosen the 'Swap' option.");
                        break;
                    default: Console.WriteLine("Invalid Choice!");  break;
                }
                Console.ReadLine(); 
        }

    }
}
