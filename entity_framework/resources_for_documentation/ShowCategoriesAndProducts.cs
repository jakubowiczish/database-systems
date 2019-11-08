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