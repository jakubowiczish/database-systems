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