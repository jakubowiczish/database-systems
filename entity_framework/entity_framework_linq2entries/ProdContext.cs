using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace entity_framework_linq2entries
{
    class ProdContext : DbContext
    {
        public DbSet<Category> Categories { get; set; }
        public DbSet<Product> Products { get; set; }
        public DbSet<Customer> Customers { get; set; }

        /*protected override void OnModelCreating(DbModelBuilder model)
        {
            base.OnModelCreating(model);
            model.Entity<Product>()
                .Property(p => p.Unitprice)
                .HasColumnType("money");
        }*/
    }
}
