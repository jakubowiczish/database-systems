private void onAddOrderClick(object sender, EventArgs e)
{
    if (isInputValid())
    {
        Order order = new Order();
        order.CustomerName = customerNameTextBox.Text;
        order.Quantity = Convert.ToInt32(quantityTextBox.Text);

        context.Orders.Add(order);
        context.SaveChanges();
    }

}

private bool isInputValid()
{
    return customerNameTextBox.Text != null && isNumeric(quantityTextBox.Text);
}

private bool isNumeric(string s)
{
    return !string.IsNullOrEmpty(s) && s.All(Char.IsDigit);
}
