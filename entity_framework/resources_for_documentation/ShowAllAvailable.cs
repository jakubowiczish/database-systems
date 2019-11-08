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