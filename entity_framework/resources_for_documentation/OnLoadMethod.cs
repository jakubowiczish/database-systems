protected override void OnLoad(EventArgs e)
{
    base.OnLoad(e);
    context = new ProdContext();
    context.Categories.Load();
    context.Products.Load();
    context.Customers.Load();
    context.Orders.Load();

    this.categoryBindingSource.DataSource = context.Categories.Local.ToBindingList();
    this.productBindingSource.DataSource = context.Products.Local.ToBindingList();

    this.orderBindingSource.DataSource = context.Orders.Local.ToBindingList();
}