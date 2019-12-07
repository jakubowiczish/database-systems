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
            //ProdContext ctx = new ProdContext();

            //AddCategory(ctx);
            //AddProduct(ctx);
            //ShowAllAvailableCategories(ctx);
            //ShowAllAvailableProducts(ctx);
            ShowCategoryForm();
        }

        static void ShowCategoryForm()
        {
            CategoryForm Form = new CategoryForm();
            Form.ShowDialog();
        }

        static void AddCategory(ProdContext ctx)
        {
            Console.WriteLine("Enter the category name");
            string Name = Console.ReadLine();
            Category category = new Category();
            category.Name = Name;

            ctx.Categories.Add(category);
            ctx.SaveChanges();
        }

        static void AddProduct(ProdContext ctx)
        {
            Console.WriteLine("Enter product name");
            string Name = Console.ReadLine();
            Console.WriteLine("Enter product category");
            int CategoryId = Convert.ToInt32(Console.ReadLine());
            Product product = new Product();
            product.Name = Name;
            product.CategoryID = CategoryId;

            ctx.Products.Add(product);
            ctx.SaveChanges();
        }

        static void ShowAllAvailableCategories(ProdContext ctx)
        {
            Console.WriteLine("All available categories: ");
            foreach (Category c in ctx.Categories)
            {
                Console.WriteLine(c.Name);
            }
        }

        static void ShowAllAvailableProducts(ProdContext ctx)
        {
            Console.WriteLine("All available products: ");
            foreach (Product p in ctx.Products)
            {
                Console.WriteLine(p.Name);
            }
        }

        static void ShowCategoriesAndProducts(ProdContext ctx)
        {
            Console.WriteLine("List of products:");
            foreach (Product p in ctx.Products)
            {
                ctx.Entry(p)
                    .Reference(e => e.Category)
                    .Load();

                if (null != p.Category)
                {
                    Console.WriteLine("Product: {0} {1} in category: {2}", p.productId, p.Name, p.Category.Name);
                }
                else
                {
                    Console.WriteLine("Product: {0} {1} without category", p.productId, p.Name, p.Category.Name);
                }
            }
        }
    }
}
