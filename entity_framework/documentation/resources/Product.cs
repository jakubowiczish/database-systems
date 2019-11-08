using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace entity_framework_linq2entries
{
    class Product
    {
        public int productId { get; set; }
        public string Name { get; set; }
        public int UnitsInStock { get; set; }

        public int CategoryID { get; set; }
        public virtual Category Category { get; set; }

        public decimal Unitprice { get; set; }
    }
}
