using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace entity_framework_linq2entries
{
    class Program
    {
        static void Main(string[] args)
        {
            ProdContext ctx = new ProdContext();

            Console.WriteLine("Enter the category name");
            string Name = Console.ReadLine();
            Category category = new Category();
            category.Name = Name;

            ctx.Categories.Add(category);
            ctx.SaveChanges();

            Console.WriteLine("All available categories: ");
            foreach (Category c in ctx.Categories)
            {
                Console.WriteLine(c.Name);
            }

            CategoryForm Form = new CategoryForm();
            Form.ShowDialog();
        }
    }
}
