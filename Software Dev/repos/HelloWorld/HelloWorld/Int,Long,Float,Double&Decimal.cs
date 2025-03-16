using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Remoting.Messaging;
using System.Text;
using System.Threading.Tasks;

namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            string textAge = "-23";
            int age         = Convert.ToInt32(textAge);
            Console.WriteLine(age);

            Console.WriteLine(int.MaxValue);
            Console.WriteLine(int.MinValue);

            string textBigNumber = "900000000000";
            long bigNumber = Convert.ToInt64(textBigNumber);
            Console.WriteLine(bigNumber);
            
            Console.WriteLine(long.MaxValue);
            Console.WriteLine(long.MinValue);

            double negative = -55.2D;
            Console.WriteLine(negative);
            Console.WriteLine(double.MaxValue);
            Console.WriteLine(double.MinValue);

            float precision = 5.0000001F;
            Console.WriteLine(precision);
            Console.WriteLine(double.MaxValue);
            Console.WriteLine(double.MinValue);

            decimal money = 14.00M;
            Console.WriteLine(money);
            Console.WriteLine(decimal.MaxValue);
            Console.WriteLine(decimal.MinValue);

            //int x;
            //int y;
            //int z;
            //same thing as
            //int x, y, z;

            //int x. = 10,
            //    y. = 20,
            //    z. = 30;

            Console.ReadLine();
        }
    }
}