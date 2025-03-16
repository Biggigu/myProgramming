using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Section3_Constrol_Flow
{
    class TryParse
    {
        public static  void TryparseTasks() 
        {
            bool success = true;

            while (success)
            {
                Console.WriteLine("Enter a number: ");
                string numInput = Console.ReadLine();
                //int num = Convert.ToInt32(numInput);
                
                if (int.TryParse(numInput, out int num))
                {
                    success = false; //Exits the loop when input is a valid number
                    Console.WriteLine(num);
                }
                else
                {
                    Console.WriteLine("Failed to convert!");
                }
            }
            Console.ReadLine();
        }
    }
}
