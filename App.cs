using System;

namespace TestApp
{
    class App
    {
        // Simple console app entry point.
        // Usage:
        //   dotnet run -- [name]
        // Examples:
        //   dotnet run --           => "Hello, World!"
        //   dotnet run -- Alice Bob => "Hello, Alice Bob!"
        static int Main(string[] args)
        {
            if (args.Length == 0 || args[0] == "-h" || args[0] == "--help")
            {
                Console.WriteLine("Usage: dotnet run -- [name]");
                Console.WriteLine("Prints a greeting. Provide a name to personalize the message.");
                return 0;
            }

            var name = args.Length > 0 ? string.Join(" ", args) : "World";
            Console.WriteLine($"Hello, {name}!");
            return 0;
        }
    }
}