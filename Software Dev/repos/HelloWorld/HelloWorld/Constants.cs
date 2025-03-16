using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace HelloWorld
{
    class Constants
    {
        static void Main(string[] args)
        {
            const int vat = 20;
            const double percentVAT = vat / 100D;
            //because of const not vat cannot be changed vat = 10;

            int balance = 1000;

            Console.WriteLine(balance * percentVAT);

            const string version = "V1.0";
            Console.WriteLine(version);
            Console.ReadLine();


        }
    }
}
