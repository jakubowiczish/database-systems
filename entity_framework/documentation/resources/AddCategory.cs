static void AddCategory(ProdContext ctx)
{
    Console.WriteLine("Enter the category name");
    string Name = Console.ReadLine();
    Category category = new Category();
    category.Name = Name;

    ctx.Categories.Add(category);
    ctx.SaveChanges();
}