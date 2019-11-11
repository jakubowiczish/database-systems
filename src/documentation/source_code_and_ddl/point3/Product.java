/*

import lombok.*;

import javax.persistence.*;

@Entity(name = "Products")
@Setter
@NoArgsConstructor
public class Product {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private int productId;

    private String ProductName;
    private int UnitsOnStock;

    @ManyToOne
    @JoinColumn(name = "supplierId")
    Supplier supplier;

    public Product(String productName, int unitsOnStock) {
        ProductName = productName;
        UnitsOnStock = unitsOnStock;
    }
}
*/