using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Data.Entity;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace entity_framework_linq2entries
{
    public partial class CategoryForm : Form
    {
        ProdContext context = new ProdContext();
        int? categoryId;

        public CategoryForm()
        {
            InitializeComponent();
        }

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

        private void saveItemsOnClick(object sender, EventArgs e)
        {
            context.SaveChanges();
            this.categoryDataGridView.Refresh();

        }

        private void cellContentOnClick(object sender, DataGridViewCellEventArgs e)
        {
            int rowSelected = e.RowIndex;
            Category category = (Category)categoryDataGridView.Rows[rowSelected].DataBoundItem;

            if (category != null)
            {
                this.categoryId = category.CategoryId;

                /* this.productBindingSource.DataSource = (from p in context.Products
                                                        where p.CategoryID == category.CategoryId
                                                        select p).ToList();
                 */

                this.productBindingSource.DataSource = 
                    new BindingList<Product>(
                        context.Products.Where(p => p.CategoryID == category.CategoryId)
                        .ToList());
            
            }
        }

        private void onAddOrderClick(object sender, EventArgs e)
        {
            if (isInputValid())
            {
                Order order = new Order();
                order.CustomerName = customerNameTextBox.Text;
                order.Quantity = Convert.ToInt32(quantityTextBox.Text);

                context.Orders.Add(order);
               // context.SaveChanges();
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



   

        

    }
}
