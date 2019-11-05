using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace entity_framework_linq2entries
{
    class Order
    {
        public int OrderID { get; set; }
        public int ProductID { get; set; }
        public virtual Product Product { get; set; }

        public int Quantity { get; set; }

        [Required]
        [ForeignKey("Customer")]
        public String CustomerName { get; set; }
        public virtual Customer Customer { get; set; }

    }
}
