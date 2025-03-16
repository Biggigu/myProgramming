using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HelloWorld
{
    class Operations
    {
        static void Main(string[] args)
        {
            int age = 23;
            Console.WriteLine(age);

            age++;
            Console.WriteLine(age);

            age = age + 1;
            Console.WriteLine(age);

            age += 1;

            age--;
            Console.WriteLine(age);

            Console.WriteLine();
            int i = 0;
            Console.WriteLine(i++);
            Console.WriteLine(i);
            Console.ReadLine();

            int firstNum = 10;
            int secondNum = 2;

            Console.WriteLine(firstNum % secondNum);

            //always even

            Console.WriteLine(1000%90);
            Console.WriteLine(100 % 10);

            Console.ReadLine();
        }
    }
}
